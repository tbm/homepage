---
title: Upgrading u-boot on SheevaPlug
nav: Upgrading U-Boot
description: Upgrading u-boot on SheevaPlug
keywords: [SheevaPlug, Marvell, Kirkwood, u-boot]
---

<% content_for :right do %>
<img src = "../images/r_sheevaplug_hand.jpg" class="border" alt="SheevaPlug in my hand" width="148" height="129" />
<% end %>

<h1>Upgrading U-Boot on SheevaPlug and other plug computers</h1>

This page describes how to install a new version of U-Boot on your plug
computer.  U-Boot is the boot loader used on plug computers.

First of all, check which version of U-Boot is installed on your plug
computer to find out whether you have to perform this upgrade.  Connect to
U-Boot using the serial console and type:

<div class="code">
<pre>
version
</pre>
</div>

This will show the version of U-Boot on your plug computer.  Two different
(and slightly incompatible) variants of U-Boot are commonly used on plug
computers.  When Marvell introduced the first plug computers a few years
ago, they created their own variant of U-Boot to add support for plug
computers.  This work has been integrated into the official U-Boot variant
in the meantime.  The advantages of the official U-Boot variant (sometimes
known as DENX) is that it is much more rapidly developed and therefore
offers features and bug fixes not found in the Marvell variant.  We will
use the DENX variant.

When you type `version` in U-Boot, you can easily spot if you're using the
Marvell version.  It shows the U-Boot version 1.1.4 plus a separate Marvell
version, as in this example:

<div class="code">
<pre>
U-Boot 1.1.4 (Dec 27 2009 - 22:03:21) Marvell version: 3.4.27
</pre>
</div>

On the other hand, the version string of the DENX variant looks like this:

<div class="code">
<pre>
U-Boot 2014.10+dfsg1-5 (Apr 07 2015 - 21:57:04)
</pre>
</div>

In other words, U-Boot is followed by a date and there is no Marvell
version.

If your plug computer is using the Marvell variant of U-Boot, you have to
upgrade since the installation guide assumes that you're using the DENX
variant.  If you're already using the DENX variant, you can upgrade in case
your U-Boot is older than the one above (i.e. older than 2014.10).

If you're upgrading from the Marvell to the DENX variant, issue the
following command and write down your MAC address.  This step is important
because all U-Boot configuration data (including your MAC address) is lost
when upgrading from the Marvell to the DENX U-Boot.

<div class="code">
<pre>
print ethaddr
</pre>
</div>

Obtain the U-Boot binary for your device and save it as `u-boot.kwb`.
Please note that since the boot loader interacts with the hardware, you
have to use the correct u-boot binary for your device.  If your device is
not listed on this page, it is <em>not</em> safe to use another u-boot
binary listed here!

<ul>

<li><a href =
"http://ftp.debian.org/debian/dists/stable/main/installer-armel/current/images/kirkwood/u-boot/sheevaplug/u-boot.kwb">SheevaPlug
(the original SheevaPlug, the eSATA SheevaPlug and the Ionics Nimbus 100)</a></li>

<li><a href =
"http://ftp.debian.org/debian/dists/stable/main/installer-armel/current/images/kirkwood/u-boot/dreamplug/u-boot.kwb">DreamPlug</a></li>

<li><a href =
"http://ftp.debian.org/debian/dists/stable/main/installer-armel/current/images/kirkwood/u-boot/guruplug/u-boot.kwb">GuruPlug
(GuruPlug Server Standard and GuruPlug Server Plus)</a></li>

<li><a href =
"http://ftp.debian.org/debian/dists/stable/main/installer-armel/current/images/kirkwood/u-boot/dockstar/u-boot.kwb">Seagate
FreeAgent DockStar</a></li>

</ul>

You have to complete three steps in order to install the new U-Boot.
First, you have to load the new U-Boot to your plug computer, either via
USB or TFTP:

<ul>

<li>

USB: First of all, copy the U-Boot binary `u-boot.kwb` to a USB stick
formatted with the FAT filesystem.  Then plug the USB stick into your plug
computer, connect the serial console and type the following commands:

<div class="code">
<pre>
usb start
fatload usb <span class="input">0:1</span> 0x0800000 u-boot.kwb
</pre>
</div>

On the GuruPlug and DreamPlug, you likely have to replace `0:1` with `2:1`.
See the explanation on <a href = "../troubleshooting/#dev-part">how to find
out your devices and partitions</a> in case your device does not boot with
`0:1` or `2:1`.

</li>

<li>

TFTP: If you have a TFTP server, copy the file `u-boot.kwb` to your TFTP
server.  Then start your plug computer, connect the serial console and type
the following commands:

<div class="code">
<pre>
setenv serverip 192.168.1.2 # IP of your TFTP server
setenv ipaddr 192.168.1.200
tftpboot 0x0800000 u-boot.kwb
</pre>
</div>

</li>

</ul>

Second, you have to flash the new U-Boot:

<ul>

<li>SheevaPlug (and SheevaPlug variants) and GuruPlug:

<div class="code">
<pre>
nand erase 0x0 0x80000
nand write 0x0800000 0x0 0x80000
</pre>
</div>

</li>

<li>DreamPlug:

<div class="code">
<pre>
sf probe 0
sf erase 0x0 0x80000
sf write 0x0800000 0x0 0x80000
</pre>
</div>

</li>

</ul>

Finally, you now have to restart your machine to activate the new version
of U-Boot:

<div class="code">
<pre>
reset
</pre>
</div>

If you upgraded from the Marvell to the DENX variant, you now have to set
your MAC address (replace the MAC address in the example with the one you
wrote down before):

<div class="code">
<pre>
setenv ethaddr <span class="input">00:50:43:01:c0:ab</span>
saveenv
reset
</pre>
</div>

Go back to my <a href = "..">Debian on Plug Computer</a> page.

<%= render "paypal", :desc => "Debian on Plug Computer donation" %>

