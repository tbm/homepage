---
title: Upgrading u-boot on OpenRD
nav: Upgrading U-Boot
description: Upgrading u-boot on OpenRD
keywords: [OpenRD, Marvell, Kirkwood, u-boot]
---

<h1>Upgrading U-Boot on OpenRD</h1>

This page describes how to install a new version of U-Boot on your OpenRD.

First of all, check which version of U-Boot is installed on your plug
computer to find out whether you should perform this upgrade.  Connect to
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
U-Boot 1.1.4 (Oct 27 2009 - 21:57:24) Marvell version: 3.4.19
</pre>
</div>

On the other hand, the version string of the DENX variant looks like this:

<div class="code">
<pre>
U-Boot 2016.03+dfsg1-6 (Jun 28 2016 - 07:38:27 +0000)
</pre>
</div>

In other words, U-Boot is followed by a date and there is no Marvell
version.

If your OpenRD is using the Marvell variant of U-Boot, you may want to
upgrade.  On the other hand, you may want to stay on the Marvell version
if it works for you.

If you're upgrading from the Marvell to the DENX variant, issue the
following command and write down your MAC address.  This step is important
because all U-Boot configuration data (including your MAC address) is lost
when upgrading from the Marvell to the DENX U-Boot.

<div class="code">
<pre>
print ethaddr
print eth1addr  # On Client and Ultimate
</pre>
</div>

In fact, it's best to store a copy of your whole U-Boot configuration:

<div class="code">
<pre>
printenv
</pre>
</div>

Obtain the U-Boot binary for your device and save it as `u-boot.kwb`.
Please note that since the boot loader interacts with the hardware, you
have to use the correct u-boot binary for your device.

* [OpenRD-Base](https://d-i.debian.org/daily-images/armel/daily/kirkwood/u-boot/openrd-base/u-boot.kwb)
* [OpenRD-Client](https://d-i.debian.org/daily-images/armel/daily/kirkwood/u-boot/openrd-client/u-boot.kwb)
* [OpenRD-Ultimate](https://d-i.debian.org/daily-images/armel/daily/kirkwood/u-boot/openrd-ultimate/u-boot.kwb)

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

<div class="code">
<pre>
nand erase 0x0 0x60000
nand write 0x0800000 0x0 0x60000
</pre>
</div>

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

You also have to restore `eth1addr` on OpenRD-Client and OpenRD-Ultimate.

In order to boot Debian, you have to set `bootcmd`, `bootargs_console` and
one of `bootcmd_sata`, `bootcmd_usb` or `bootcmd_mmc`.  Please see the
[installation page](../install#install) for detailed instructions.

Go back to my <a href = "..">Debian on Plug Computer</a> page.

<%= render "paypal", :desc => "Debian on Plug Computer donation" %>

