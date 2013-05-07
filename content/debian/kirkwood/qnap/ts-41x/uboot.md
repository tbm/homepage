---
title: U-Boot on the QNAP TS-41x
nav: U-Boot
description: Using U-Boot on the QNAP TS-41x
keywords: [Debian, QNAP, TS-410, TS-410U, TS-412, TS-419P, TS-419U, serial, console, uboot, U-Boot]
---

<% content_for :right do %>
<img src = "../images/r_qnap_ts419p.jpg" class="border" alt="QNAP TS-419P from the front" width="148" height="148" />

<%= render "adsense-wideskyscaper-right" %>
<% end %>

<h1>Using U-Boot on the QNAP TS-410, TS-410U, TS-412, TS-419P, TS-419P+ and TS-419U</h1>

If you have a <a href = "../serial/">serial console</a> for your QNAP
TS-41x, you can use U-Boot, the boot loader used on the TS-41x, to restore
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
there's a ramdisk that is 9 MB in size.

<div class="code">
<pre>
setenv bootargs console=ttyS0,115200n8 root=/dev/ram rw initrd=0xa00000,0x8fffff
</pre>
</div>

Finally, load the image via the network with TFTP and start it:

<div class="code">
<pre>
tftpboot 0xa00000 initrd.gz
tftpboot 0x800000 kernel
bootm 0x800000
</pre>
</div>

If you'd like to load a kernel image you saved from `/boot`, please see the
<a href = "#prepare">instructions on how to prepare the image</a> below.

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
devio &gt; $tmp 'wl 0xe3a01c09,4' 'wl 0xe38110c6,4' # TS-41x
cat /boot/vmlinuz-2.6.32-5-kirkwood &gt;&gt; $tmp
mkimage -A arm -O linux -T kernel -C none -a 0x00008000 -e 0x00008000 -d $tmp vmlinuz-2.6.32-5-kirkwood.uboot
</pre>
</div>

Next, you have to pad the initrd image so it will be exactly 9 MB:

<div class="code">
<pre>
dd if=/boot/initrd.img-2.6.32-5-kirkwood of=initrd.img-2.6.32-5-kirkwood.padded ibs=9437184 conv=sync
</pre>
</div>

Now copy `vmlinuz-2.6.32-5-kirkwood.uboot` and
`initrd.img-2.6.32-5-kirkwood.padded` to your TFTP server and load them in
memory as described above.

<div class="bbf">
<%= render "adsense-banner-before-footer" %>
</div>

