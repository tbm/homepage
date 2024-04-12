---
title: U-Boot on the QNAP TS-409
nav: U-Boot
description: Using U-Boot on the QNAP TS-409
keywords: [Debian, QNAP, TS-409, serial, console, uboot, U-Boot]
---

If you have a <a href = "../serial/">serial console</a> for your QNAP
TS-409, you can use U-Boot, the boot loader used on the TS-409, to restore
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
there's a ramdisk that is 4 MB in size.

<div class="code">
<pre>
setenv bootargs console=ttyS0,115200n8 root=/dev/ram rw initrd=0x800000,0x3fffff
</pre>
</div>

Finally, load the image via the network with TFTP and start it:

<div class="code">
<pre>
tftpboot 0x0800000 initrd
tftpboot 0x400000 kernel
bootm 0x400000
</pre>
</div>

If you'd like to load a kernel image you saved from `/boot`, please see the
<a href = "#prepare">instructions on how to prepare the image</a>.

<h2 id="restore">Restoring the QNAP firmware</h2>

If you want to restore the original QNAP firmware when your Debian is no
longer working, you can put the backup you made of your QNAP firmware into
flash via U-Boot.  First, specify the IP address of your TFTP server and of
your QNAP device:

<div class="code">
<pre>
setenv serverip 192.168.1.4
setenv ipaddr 192.168.1.139
</pre>
</div>

Then load the backup you made of `mtd1` (the QNAP kernel) and write it to
flash:

<div class="code">
<pre>
tftpboot 0x400000 mtd1
erase 0xff800000 0xff9fffff
cp.b 0x400000 0xff800000 ${filesize}
</pre>
</div>

Finally, load the backup you made of `mtd2` (the QNAP ramdisk) and write it
to flash:

<div class="code">
<pre>
tftpboot 0x0800000 mtd2
erase 0xffa00000 0xffdfffff
cp.b 0x0800000 0xffa00000 ${filesize}
</pre>
</div>

And restart the machine:

<div class="code">
<pre>
reset
</pre>
</div>

Once you have restored the QNAP firmware in flash, you have to follow the
<a href = "../deinstall/">second step described on the restore page</a> and
run QNAP Finder to install the QNAP software to disk.

<h2 id="prepare">Preparing Debian images from <code>/boot</code> to load</h2>

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
tftpboot 0x0800000 mtd2
tftpboot 0x400000 mtd1
bootm 0x400000
</pre>
</div>

<h2 id="deinstall">Installing the original QNAP firmware</h2>

You can restore the original QNAP firmware directly from u-boot if you
no longer want to run Debian.  First of all, obtain the [firmware
image from the QNAP web
site](https://wiki.qnap.com/wiki/System_Recovery_Mode#Operating_Guideline_of_System_Recovery_Mode).
Unzip the file and you'll get an `.img` file.  Save that file as
`qnapimg.bin` on your TFTP server.

Now you can write this image to flash.  This is exactly what the
[recovery mode](../recovery) does.

<div class="code">
<pre>
setenv serverip 192.168.0.2
setenv ipaddr 192.168.0.100
tftp 0x400000 qnapimg.bin
protect off 0xff000000 0xff6fffff
erase 0xff000000 0xff6fffff
cp.b 0x400000 0xff000000 0x700000
</pre>
</div>

Afterwards you have to run QNAP Finder to install your system.

