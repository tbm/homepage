---
title: Boot process of Debian on the Linksys NSLU2
nav: Boot Process
description: Boot process of Debian on the Linksys NSLU2
keywords: [NSLU2, Linksys NSLU2, boot process, boot]
---

<% content_for :right do %>
<img src = "../images/r_nslu2_front.jpg" class="border" alt="A NSLU2 from the front" width="148" height="218" />

<%= render "adsense-wideskyscaper-right" %>
<% end %>

<h1>The Boot Process of the Linksys NSLU2 running Debian</h1>

This page describes the complete boot process of a Linksys NSLU2 running
Debian.  While the information from this document is not needed to run
Debian on your NSLU2, some users might find it interesting to know what's
going on behind the scenes.

<h2>Getting the NSLU2 to boot Debian</h2>

The boot process of a Linksys NSLU2 running Debian is actually quite
complicated.  The reason for this is that we have to work around several
limitations of and deal with some peculiarities of the NSLU2.  The Linksys
NSLU2 uses the RedBoot boot loader plus some extensions.  For example, the
NSLU2's RedBoot has been extended with functionality which allows you to
put the device into upgrade mode and then upgrade the firmware via the
network.  There's a utility in Debian called `upslug2` which can do this.
Unlike other systems running RedBoot, the NSLU2 also requires a special
header (the Sercomm header) on each flash partition to indicate the size of
the stored data.  The NSLU2-wiki contains more information about the <a
href = "http://www.nslu2-linux.org/wiki/Info/BootFlash">boot flash and
required headers</a> of the NSLU2.

RedBoot supports a partition table for flash (the FIS directory).
Unfortunately, the NSLU2 does not use this partition table to refer to the
kernel and ramdisk.  Instead, it uses the following hard-coded values:

<table>

<tr>
<th>Partition</th>
<th>Location</th>
</tr>

<tr>
<td>Kernel</td>
<td>0x00060000</td>
</tr>

<tr>
<td>Ramdisk</td>
<td>0x00160000</td>
</tr>

</table>

As you can see, it loads the kernel from 0x60000 and the ramdisk from
0x160000.  This means that the size of the kernel can only be 0x100000
(0x160000 - 0x60000) or 1 MB (in fact, slightly less because every
partition requires a 16 byte Sercomm header).  This is not enough for
modern Linux kernels so we had to work around this limitation.  We chose to
use the APEX boot loader as a second stage boot loader.  This means that
APEX is stored where RedBoot expects to find the Linux kernel.  When
RedBoot starts it will boot APEX and APEX in turn loads the Linux kernel
and ramdisk.  This approach is viable because APEX is very flexible and
could be adapted to our requirements.  (It helps that the developer of
APEX, Marc Singer, is a Debian developer!)

In order to use APEX, we added a new flash partition called `Loader`
(located where RedBoot expects to find the kernel).  Rod Whitby extended
the tool `slugimage`, which we use to generate the NSLU2 firmware image, to
support the `Loader` partition.  The flash layout used by Debian is the
following:

<table>

<tr>
<th>Partition</th>
<th>Location</th>
<th>Size</th>
</tr>

<tr>
<td>Loader</td>
<td>0x00060000</td>
<td>128 KB</td>
</tr>

<tr>
<td>Kernel</td>
<td>0x00080000</td>
<td>11 * 128 KB (1.375 MB)</td>
</tr>

<tr>
<td>Ramdisk</td>
<td>0x001e0000</td>
<td>6 MB</td>
</tr>

</table>

When RedBoot starts, it will load APEX from 0x60000 and the ramdisk from
0x160000.  APEX in turn will then read the kernel from 0x80000 and the
ramdisk from 0x1e0000.  There is one further complication with this: when
RedBoot reads the ramdisk from 0x160000, it expects to find the Sercomm
header indicating the size of the data to be loaded.  With our new flash
layout, 0x160000 is right in the middle of the kernel partition.  If
RedBoot finds strange data at 0x160000, it will crash.  Therefore, we had
to implement a further workaround, namely to split the kernel into two
pieces: the first one goes from 0x80010 (not 0x80000: remember the 16 byte
Sercomm header) to 0x15ffff, and the second one goes from 0x160010 to
0x1dffff.  At 0x160000 we add the 16 byte Sercomm header indicating that
only 128 KB should be read as ramdisk by RedBoot (we specify 128 KB rather
than zero because RedBoot doesn't accept a value of zero; in reality, we
don't really care what RedBoot is loading since APEX will load the real
ramdisk for us).  This leaves us with 1.375 MB - 32 bytes (the two Sercomm
headers) for the kernel.  (Yes, this is not much either but a few years ago
it felt like enough.)

If this sounds complicated, this is because it is.  Fortunately, users
don't have to worry about these details at all.  The tools `slugimage` (to
create the firmware image) and `flash-kernel` (to write the kernel and
ramdisk to flash) will automatically take care of everything.  You may
wonder why we bother working around RedBoot like this when we could simply
replace RedBoot with APEX (instead of keeping RedBoot and using APEX as a
second stage boot loader).  The reason is that you can brick your machine
when replacing the original boot loader.  By keeping the original boot
loader, we ensure that you can always use RedBoot's recovery mode to flash
a working firmware image to your NSLU2.

<h2>Booting Debian</h2>

So what happens when you boot Debian?  When you start the NSLU2, RedBoot is
started and will load APEX as described above.  APEX will then load the
Debian kernel and ramdisk from flash and execute them.  At this point, the
boot process is very similar to that of any Debian system: the ramdisk
(generated by `initramfs-tools`) will load all necessary modules (like
USB), mount the disk and start the boot process from disk.

Here is an overview of the LED activity you see during the boot process:

* Status LED is solid amber: RedBoot is running.
* Green, cycling down all the LEDs from top to bottom: APEX is loading the
kernel and ramdisk.
* Status LED is solid amber and both disk LEDs are solid green: the kernel
has been executed.
* All lights turn off (except Ethernet): the ramdisk has been loaded.
* Disk becomes solid green: `/dev` is being populated and USB has been
loaded.
* A moment later, the Ethernet LED will turn off.  The Ethernet module has
now been loaded.
* Ethernet LED becomes green: the microcode `/lib/firmware/NPE-B` has been
loaded.
* Status LED is blinking green and amber: runlevel 2 has been entered.
Services like `sshd` and `crond` are now being started.
* Status LED is solid green: the NSLU2 has booted.  SSH is ready now.

There are some tools that ensure a good operation of Debian on the NSLU2:

* `nslu2-utils`: this package contains tools to control the LED.  It also
contains init scripts that will set the LED when runlevel 2 is entered and
when the boot process has completed.
* `flash-kernel`: this package contains a tool to write the kernel and
ramdisk to flash.  It also contains a hook script for `initramfs-tools`
that ensures that the name of the root device is written into the ramdisk
(this explains why you never had to change the boot loader to specify your
root device).

This pretty much sums up the boot process of Debian on the Linksys NSLU2.

Go back to the <a href = "..">Debian on NSLU2</a> page.

<%= render "paypal", :desc => "Debian/NSLU2 donation" %>

<div class="bbf">
<%= render "adsense-banner-before-footer" %>
</div>

