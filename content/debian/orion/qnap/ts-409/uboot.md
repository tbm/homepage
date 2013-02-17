---
title: U-Boot on the QNAP TS-409
nav: U-Boot
description: Using U-Boot on the QNAP TS-409
keywords: [Debian, QNAP, TS-409, serial, console, uboot, U-Boot]
---

<% content_for :right do %>
<%= render 'adsense-wideskyscaper-right' %>
<% end %>

<h1>Using U-Boot on the QNAP TS-409</h1>

If you have a <a href = "../serial">serial console</a> for your QNAP
TS-409, you can use U-Boot, the boot loader used on the TS-409, to restore
the original QNAP firmware or load images via the network.

<h2><a id = "load">Loading the installer image</a></h2>

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
tftpboot 0x0800000 initrd.gz
tftpboot 0x400000 kernel
bootm 0x400000
</pre>
</div>

If you'd like to load a kernel image you saved from `/boot`, please see the
<a href = "#prepare">instructions on how to prepare the image</a>.

<h2><a id = "restore">Restoring the QNAP firmware</a></h2>

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
<a href = "../deinstall">second step described on the restore page</a> and
run QNAP Finder to install the QNAP software to disk.

<h2><a id = "prepare">Preparing Debian images from `/boot` to load</a></h2>

If you copy your Debian kernel and ramdisk from `/boot` to another machine
for backup, you can load them via TFTP as described above after making some
small modifications to the kernel and ramdisk images.

You have to make two modifications to the kernel.  First, you have to set
the machine ID of your QNAP device by prepending a few bytes to the kernel
image.  This can easily be done with the `devio` command in Debian.
Second, you have to generate a U-Boot image from the kernel image.  Let's
take the `2.6.32-5` kernel as an example:

<div class="code">
<pre>
tmp=$(tempfile)
devio &gt; $tmp 'wl 0xe3a01c06,4' 'wl 0xe3811041,4' # TS-409
cat /boot/vmlinuz-2.6.32-5-orion5x &gt;&gt; $tmp
mkimage -A arm -O linux -T kernel -C none -a 0x00008000 -e 0x00008000 -d $tmp vmlinuz-2.6.32-5-orion5x.uboot
</pre>
</div>

Next, you have to pad the initrd image so it will be exactly 4 MB:

<div class="code">
<pre>
dd if=/boot/initrd.img-2.6.32-5-orion5x of=initrd.img-2.6.32-5-orion5x.padded ibs=4194304 conv=sync
</pre>
</div>

Now copy `vmlinuz-2.6.32-5-orion5x.uboot` and
`initrd.img-2.6.32-5-orion5x.padded` to your TFTP server and load them in
memory or write them to flash as described above.

<div class="bbf">
<%= render 'adsense-banner-before-footer' %>
</div>

