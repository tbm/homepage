---
title: De-installing Debian on the D-Link DNS-323
nav: De-installing Debian
description: Restoring the original Firmware on the D-Link DNS-323
keywords: [Debian, D-Link, DNS-323, Conceptronic, CH3SNAS, original firmware]
---

<% content_for :right do %>
<img src = "../images/r_ch3snas_front.jpg" class="border" alt="Conceptronic CH3SNAS from the front" width="148" height="146" />

<%= render "adsense-wideskyscaper-right" %>
<% end %>

<h1>Restoring the original firmware</h1>

If you want to restore the original firmware for some reason, you can
follow the instructions below.  Please note that this will only work if
your Debian system is still working.  If your Debian system is broken but
the machine itself works, it is possible to restore the original firmware
using a <a href = "../recovery">serial console</a>.

You first have to download the firmware image from D-Link or Conceptronic
and then unpack it.  You can unpack it with <a href =
"http://theshed.hezmatt.org/dns323-firmware-tools/">dns323-firmware-tools</a>
(version 0.3 or higher):

<div class="code">
<pre>
splitdns323fw -k uKernel -i uRamdisk vendor-firmware
</pre>
</div>

Now that you've extracted the kernel and ramdisk from the vendor firmware
image, you can write them to flash:

<div class="code">
<pre>
cat uKernel &gt; /dev/mtdblock2
cat uRamdisk &gt; /dev/mtdblock3
</pre>
</div>

When you restart your machine, the original firmware will start.  The
original firmware will offer you to format your disk.

Please note that simply starting the original firmware will destroy your
Debian installation on disk (even if you don't choose to format the disk)!

<div class="bbf">
<%= render "adsense-banner-before-footer" %>
</div>

