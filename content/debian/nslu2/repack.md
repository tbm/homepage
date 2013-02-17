---
title: Modify NSLU2 image
nav: Modify Image
description: Modify NSLU2 image
keywords: [NSLU2, Linksys NSLU2, Debian, modify, image]
---

<% content_for :right do %>
<img src = "../images/r_nslu2_front.jpg" class="border" alt="A NSLU2 from the front" width="148" height="218" />

<%= render 'adsense-wideskyscaper-right' %>
<% end %>

<h1>How to modify a NSLU2 flash image</h1>

The Linksys NSLU2 has a nice feature that allows users to write a firmware
image to flash to the NSLU2 via the network.  The tool `upslug2` can be
used under Linux to write an image to a NSLU2.  The firmware image consists
of the Linux kernel, a ramdisk and some other components.  This page
describes how to take an existing firmware image, unpack it, make changes
and then pack it again.  This is useful for a number of reasons, for
example to add the NPE microcode to an installer image or to change
`oldsys-preseed` (the tool creating the network configuration for the
Debian installer based on the settings from the NSLU2 firmware) so it will
use different network settings.

In order to modify a NSLU2 image, you have to install some tools:

<div class="code">
<pre>
apt-get install slugimage devio
</pre>
</div>

Now download a NSLU2 image and save it as `nslu2.bin`.  You can now unpack
this image:

<div class="code">
<pre>
sudo rm -rf initrd
rm -rf new-nslu2.img new-initrd*
slugimage -u -i nslu2.bin
devio '&lt;&lt; ramdisk.gz; xp $ 4' &gt; ramdisk-swap.gz
mkdir initrd; cd initrd
zcat ../ramdisk-swap.gz | sudo cpio -i
</pre>
</div>

The image is now unpacked and you can make changes.  For example, to add
the NPE microcode you'd have to do this:

<div class="code">
<pre>
sudo mkdir lib/firmware
sudo cp ~/NPE-B.01020201 lib/firmware
sudo ln -s NPE-B.01020201 lib/firmware/NPE-B
</pre>
</div>

Now that you have made some changes, you can generate a new image:

<div class="code">
<pre>
find . | sudo cpio --quiet -o -H newc &gt; ../new-initrd
cd ..
gzip -9 new-initrd
dd if=new-initrd.gz of=new-initrd.gz.padded ibs=6291440 conv=sync
devio "&lt;&lt;"new-initrd.gz.padded &gt; new-initrd.gz.swapped "xp $,4"
slugimage -p -o new-nslu2.img -k vmlinuz -L apex.bin -r new-initrd.gz.swapped
</pre>
</div>

You now have a new image called `new-nslu2.img` and you can use `upslug2`
to write it to your NSLU2.

<div class="bbf">
<%= render 'adsense-banner-before-footer' %>
</div>

