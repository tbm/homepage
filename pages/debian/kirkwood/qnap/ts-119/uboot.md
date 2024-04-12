---
title: U-Boot on QNAP TS-11x/TS-12x
nav: U-Boot
description: Using U-Boot on the QNAP TS-11x/TS-12x
keywords: [Debian, QNAP, TS-110, TS-112, TS-112P, TS-119, TS-120, TS-121, serial, console, uboot, U-Boot]
---

If you have a <a href = "../serial/">serial console</a> for your QNAP
device, you can use U-Boot, the boot loader used on the TS-11x/TS-12x, to restore
the original QNAP firmware or load images via the network.

<h2 id="load">Loading the installer image</h2>

You can load the Debian installer image (or other images) via TFTP.  First
of all, configure the IP address of the TFTP server and of your QNAP:

<div class="code">
<pre>
setenv serverip 192.168.1.2
setenv ipaddr 192.168.1.139
</pre>
</div>

Then specify the command line that should be passed to the kernel.  This
tells the kernel that the serial console should be activated and that
there's a ramdisk that is 9 MB in size.

<div class="code">
<pre>
setenv bootargs console=ttyS0,115200n8 root=/dev/ram rw initrd=0xa00000,0x8fffff
</pre>
</div>

Finally, load the image via the network with TFTP and start it:

<div class="code">
<pre>
tftpboot 0xa00000 initrd
tftpboot 0x800000 kernel
bootm 0x800000
</pre>
</div>

If you'd like to load a kernel image you saved from `/boot`, please see the
<a href = "#prepare">instructions on how to prepare the image</a> below.

<h2 id="prepare">Preparing Debian images from `/boot` to load</h2>

You can copy the Debian kernel and ramdisk from your system to another
machine for backup.  This way, you can load them via TFTP as described
above.  However, the files from `/boot` cannot be used directly but
require some modifications before you can use them.  You don't have to
make these modifications manually since `flash-kernel` already performs
these steps as part of the kernel upgrade process. You can obtain a copy
of what's actually written to flash from `/var/backups/flash-kernel`.
You can therefore take the files from that location and use them to boot
via TFTP.

`mtd1` corresponds to the kernel while `mtd2` is the initrd.  Therefore,
the correct TFTP commands are:

<div class="code">
<pre>
tftpboot 0xa00000 mtd2
tftpboot 0x800000 mtd1
bootm 0x800000
</pre>
</div>

<h2 id="recovery">Recovery mode</h2>

QNAP devices have a <a href = "../recovery">recovery mode</a>.  If you have
u-boot, you can run the commands directly if you wish.

However, be very careful because you can brick your device if you make a
mistake.

The commands to run are:

<div class="code">
<pre>
tftpboot 0x800000 ${bootfile}
protect off bank 1; erase 0xf8200000 0xf8ffffff; cp.b 0xa00000 0xf8200000 e00000; protect on bank 1
</pre>
</div>

But don't believe me.  It's better if you verify it yourself.  Take `mtd0`
(the u-boot partition) and run `strings` on it to find the recovery
commands.

If something goes wrong, don't blame me.

