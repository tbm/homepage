---
title: Troubleshooting Debian on Plug Computer
nav: Troubleshooting
description: Troubleshooting Debian on Plug Computer
keywords: [Debian, SheevaPlug, plug, troubleshooting, problems]
---

<% content_for :right do %>
<img src = "../images/r_sheevaplug_hand.jpg" class="border" alt="SheevaPlug in my hand" width="148" height="129" />

<%= render "adsense-wideskyscaper-right" %>
<% end %>

<h1>Troubleshooting</h1>

This page describes common problems that users of Debian on plug computers
have run into.  If you have any problems with your plug computer, either
while trying to install Debian or when running Debian, please look through
this page carefully to see whether you can find a solution.  If your
problem is not covered here, feel free to contact the <a href =
"http://lists.debian.org/debian-arm/">debian-arm list</a> for help.  Always
include the full boot log as well as the output of `printenv` from U-Boot.

<h2><a id = "u-boot">U-Boot</a></h2>

<h3><a id = "serial">Cannot connect to serial console</a></h3>

If you cannot connect to the serial console of your plug computer, make
sure that your device is working correctly.  It has been reported that the
power supply for SheevaPlug devices can stop working after continued use,
so this might be the reason why you cannot connect to the serial console.

If your device is working correctly but you get a "permission denied" error
when connecting to the serial console, make sure that your user is in the
`dialout` group.  This is the group associated with the `/dev/ttyUSBx`
device nodes.

<h3><a id = "uncompress">No output after "Uncompressing Linux..."</a></h3>

You get no output after seeing this line:

<div class="code">
<pre>
Uncompressing Linux... done, booting the kernel.
</pre>
</div>

If you've just upgraded from Debian 6.0 (squeeze) to Debian 7 (wheezy),
your version of u-boot is too old.  You need 2011.12-3 (or higher).  Please
<a href = "../uboot-upgrade/">upgrade u-boot</a> and everything will work
again.  There's no need to re-install Debian!

<h3><a id = "bad-magic">Error "Bad Magic Number" when loading image</a></h3>

Some users report that they get the following error when booting:

<div class="code">
<pre>
## Booting image at 00400000 ...
Bad Magic Number
</pre>
</div>

In most cases, the problem is not with the image itself but with loading
the image.  Take a look at the whole boot log and you'll probably find an
earlier error, typically related to loading the image (maybe you specified
a wrong location for the boot image; maybe the TFTP server didn't respond;
maybe U-Boot failed to load the image from your USB stick).  Look for the
first problem in your boot log and you'll probably be able to figure out
the solution.

<h3><a id = "dev-part">Error "** Unable to read "/uImage" from usb 0:1 **" when booting</a></h3>

If you receive the error message `Unable to read "/uImage" from usb 0:1`
when booting the first time, it's likely that `0:1` is not the correct boot
partition.  `0:1` refers to device `0` and partition `1` but it's possible
that your boot partition is on a different device or partition.

In order to find out the correct device, you can use `usb dev` (for USB) or
`ide dev` (for SATA) to see all devices.  (Unfortunately, it's not possible
to list devices and partitions for MMC/SD cards with the current version of
u-boot.)  In the following example, there is a single USB device (device
`0`):

<div class="code">
<pre>
Marvell&gt;&gt; <span class="input">usb dev</span>

USB device 0: Vendor: A-JET    Prod.: USB 2.0 0812     Rev: 1.00
            Type: Removable Hard Disk
            Capacity: 1970.0 MB = 1.9 GB (4034560 x 512)
</pre>
</div>

You can now display all partitions for this device with the `usb part`
command (or `ide part` for SATA devices):

<div class="code">
<pre>
Marvell&gt;&gt; <span class="input">usb part 0</span>

Partition Map for USB device 0  --   Partition Type: DOS

Partition     Start Sector     Num Sectors     Type
    1                 2048          317440      83
    2               319488         3211264      83
    3              3532798          499714       5 Extd
    5              3532800          499712      82
</pre>
</div>

There are two partitions with the ext2/ext3 filesystem (type 83) and one
extended partition for swap (type 82).  The first partition (partition `1`)
is the boot partition.

In the example, the device is device `0` and the boot partition is
partition `1`.  Therefore, the correct path is `0:1`.  However, in your
case it might be something else.

<h3><a id = "tftp-timeout">Output "T T T T" when loading via TFTP</a></h3>

Some users report that they get the following output when loading an image
via TFTP:

<div class="code">
<pre>
T T T T
</pre>
</div>

This means that the TFTP server doesn't respond.  Ensure that you specified
the right IP address of the TFTP server and location of the image.

Also note that resetting the U-Boot environment may cause the plug computer
to try to load an image via TFTP.  If you unexpectedly see the `T T T`
messages, check your U-Boot configuration with `printenv` to ensure it's
loading the image from the right location.

<h3><a id = "usb-lvm">Boot fails with LVM on USB drive</a></h3>

If you have installed Debian on a USB drive and put the root device on a
LVM volume it's possible that the system won't boot because Debian tries to
access the LVM volume before the USB drive is recognized.  To avoid this
problem, pass a `rootdelay` parameter to the kernel.  For example, issue
the following commands in U-Boot to give the USB drive 10 seconds to
appear:

<div class="code">
<pre>
bootargs_console console=ttyS0,115200 rootdelay=10
</pre>
</div>

<h3><a id = "fat">Loading image from a USB stick with FAT fails</a></h3>

U-Boot may have problems loading an image from a FAT32 filesystem whereas
FAT works.  I believe you can make a FAT filesystem under Linux with the
following command:

<div class="code">
<pre>
mkfs.vfat -F 16
</pre>
</div>

<h2><a id = "installer">Debian installer</a></h2>

<h3><a id = "partman-stuck">Formatting the disk is stuck at 33%</a></h3>

Formatting the disk may take a long time, especially if you have a large
disk.  Unfortunately, the progress bar is not updated while the disk is
being formatted so you may think that it is stuck (at 33%).  If this
happens, just be patient.  The installer is in fact formatting your disk.

<h3><a id = "esata-sheevaplug">eSATA disk not found on eSATA SheevaPlug</a></h3>

If your eSATA disk is not recognized on your eSATA SheevaPlug when booting
Debian or the Debian installer, it's probably due to a missing u-boot
configuration.  On eSATA SheevaPlug devices (but not other devices), you
have to configure u-boot like this:

<div class="code">
<pre>
setenv machid a76
saveenv
reset
</pre>
</div>

These commands will put in the correct settings and then restart the device
so the changes will take effect.

<%= render "paypal", :desc => "Debian on Plug Computer donation" %>

<div class="bbf">
<%= render "adsense-banner-before-footer" %>
</div>

