---
title: Recovery mode of the Kurobox Pro
nav: Recovery mode
description: Recovery mode of the Kurobox Pro
keywords: [Buffalo, Revogear, Kurobox Pro, recovery, emergency, rescue]
---

<% content_for :right do %>
<img src = "../images/r_kuroboxpro_front.jpg" class="border" alt="Kurobox Pro from the front" width="148" height="231" />

<%= render "adsense-wideskyscaper-right" %>
<% end %>

<h1>Recovery mode of the Kurobox Pro</h1>

If the Kurobox Pro is configured to boot from disk but there is no disk,
the device will request the files `uImage.buffalo` and `initrd.buffalo` via
TFTP.  The Kurobox Pro will use the IP address `192.168.11.150` and request
the images from the TFTP server with the address `192.168.11.1`.  However,
it's possible to change these values in the u-boot configuration
environment.

<h2>Loading the original Buffalo firmware</h2>

If you made a copy of `/dev/mtdblock1` (the kernel) of your Kurobox Pro,
you can put the kernel on the TFTP server and start the Buffalo firmware
that is stored in flash.  You first have to extract the kernel from the
`mtd1` file:

<div class="code">
<pre>
dd if=mtd1 of=uImage.buffalo bs=131072 skip=1
</pre>
</div>

Next, you have to generate a ramdisk.  Even though we don't need one, the
recovery mode wants to load one.  So we can generate an empty ramdisk:

<div class="code">
<pre>
mkdir x ; cd x
find . | cpio --quiet -o -H newc &gt; ../x2
cd ..
mkimage -A arm -O linux -T ramdisk -C gzip -a 0x0 -e 0x0 -d x2 initrd.buffalo
rmdir x ; rm -f x2
</pre>
</div>

Alternatively, you can download the <a href =
"../files/initrd.buffalo-empty">empty initrd</a> from my server.

When you put these two files (`uImage.buffalo` and `initrd.buffalo`) on
your TFTP server and boot without a hard drive, the original Buffalo
firmware will be started.  You can then <a href = "../deinstall/">configure
the u-boot environment</a> so the Kurobox Pro will start from flash.  You
can then put the disk back into your device, boot into the Buffalo firmware
and hopefully fix what's broken.

<h2>Loading the Debian installer</h2>

You can also load the Debian installer via the recovery mode, although I'm
not sure how useful it is since the recovery mode only works when the SATA
disk is not connected.

In any case, you have to download the kernel and ramdisk from the <a href =
"http://ftp.nl.debian.org/debian/dists/stable/main/installer-armel/current/images/orion5x/network-console/buffalo/kuroboxpro/">Debian installer pages</a> and then pad the ramdisk to 20M because the recovery
mode has some strange assumptions:

<div class="code">
<pre>
dd if=initrd.buffalo-debian of=x bs=64 skip=1 # extract ramdisk
dd if=x of=x2 ibs=20971520 conv=sync # pad to 20 MB
mkimage -A arm -O linux -T ramdisk -C gzip -a 0x0 -e 0x0 -d x2 initrd.buffalo
rm -f x x2
</pre>
</div>

Now you can use new `initrd.buffalo` file and the `uImage.buffalo` file you
downloaded in order to start the Debian installer.

Go back to my <a href = "..">Debian on Kurobox Pro</a> page.

<div class="bbf">
<%= render "adsense-banner-before-footer" %>
</div>

