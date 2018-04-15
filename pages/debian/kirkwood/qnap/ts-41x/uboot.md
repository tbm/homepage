---
title: U-Boot on the QNAP TS-41x/TS-42x
nav: U-Boot
description: Using U-Boot on the QNAP TS-41x/TS-42x
keywords: [Debian, QNAP, TS-410, TS-410U, TS-412, TS-419P, TS-419U, TS-420, TS-421, serial, console, uboot, U-Boot]
---

<div class="right">
<img src = "../images/r_qnap_ts419p.jpg" class="border" alt="QNAP TS-419P from the front" width="148" height="148" />
</div>

<h1>Using U-Boot on the QNAP TS-410, TS-410U, TS-412, TS-419P, TS-419P+, TS-419P II, TS-419U, TS-420 and TS-421</h1>

If you have a <a href = "../serial/">serial console</a> for your QNAP
device, you can use U-Boot, the boot loader used on the TS-41x/TS-42x, to restore
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

