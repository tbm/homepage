---
title: Debian installer for plug computer
nav: Installation
description: Installation guide of Debian on plug computer
keywords: [SheevaPlug, Marvell, Kirkwood, Debian, installer, ARM, GuruPlug]
---

<div class="right">
<img src = "../images/r_sheevaplug_hand.jpg" class="border" alt="SheevaPlug in my hand" width="148" height="129" />
</div>

This page describes how to install Debian 12 (bookworm) on plug computers,
such as the SheevaPlug and GuruPlug.

The following devices are currently supported:

<ul>

<li>DreamPlug</li>

<li>GuruPlug Server Standard</li>

<li>GuruPlug Server Plus</li>

<li>SheevaPlug (the SheevaPlug Development Kit)</li>

<li>SheevaPlug with eSATA</li>

<li>Seagate FreeAgent DockStar (<a href = "../plugs/#limited">limited
support</a>: only if you added a serial console)</li>

</ul>

Please read the <a href = "../plugs/">plug variants</a> page to find out
about the status of other plug computers.

The Debian installer doesn't currently support installations to on-board
flash storage, but you can use it to install to USB, SD or eSATA.  In order
to proceed, you will therefore need either a USB stick (or disk), an SD
card or an external disk with an eSATA port.

<h2 id="prepare">Preparation</h2>

Make sure to connect an Ethernet cable to your plug computer (if you
haven't already) because the installer will download files from the
Internet for the installation.

<h2 id="uboot">Upgrading U-Boot</h2>

You have to upgrade the u-boot boot loader before you can install Debian.
Please visit the page describing the <a href = "../uboot-upgrade/">u-boot
upgrade process</a> to ensure that you have the right version of u-boot
before proceeding with the installation of Debian.

<h2 id="starting">Starting the Installer</h2>

First of all, you have to download the installer.  Download the uImage and
uInitrd files and store them either on a USB stick, MMC/SD card or a TFTP
server:

* DreamPlug: <a href =
"http://ftp.debian.org/debian/dists/bookworm/main/installer-armel/current/images/kirkwood/netboot/marvell/dreamplug/uImage">uImage</a>
and <a href =
"http://ftp.debian.org/debian/dists/bookworm/main/installer-armel/current/images/kirkwood/netboot/marvell/dreamplug/uInitrd">uInitrd</a>
* GuruPlug: <a href =
"http://ftp.debian.org/debian/dists/bookworm/main/installer-armel/current/images/kirkwood/netboot/marvell/guruplug/uImage">uImage</a>
and <a href =
"http://ftp.debian.org/debian/dists/bookworm/main/installer-armel/current/images/kirkwood/netboot/marvell/guruplug/uInitrd">uInitrd</a>
* SheevaPlug without eSATA: <a href =
"http://ftp.debian.org/debian/dists/bookworm/main/installer-armel/current/images/kirkwood/netboot/marvell/sheevaplug/uImage">uImage</a>
and <a href =
"http://ftp.debian.org/debian/dists/bookworm/main/installer-armel/current/images/kirkwood/netboot/marvell/sheevaplug/uInitrd">uInitrd</a>
* SheevaPlug with eSATA: <a href =
"http://ftp.debian.org/debian/dists/bookworm/main/installer-armel/current/images/kirkwood/netboot/marvell/sheevaplug-esata/uImage">uImage</a>
and <a href =
"http://ftp.debian.org/debian/dists/bookworm/main/installer-armel/current/images/kirkwood/netboot/marvell/sheevaplug-esata/uInitrd">uInitrd</a>
* Seagate FreeAgent DockStar: <a href =
"http://ftp.debian.org/debian/dists/bookworm/main/installer-armel/current/images/kirkwood/netboot/seagate/dockstar/uImage">uImage</a>
and <a href =
"http://ftp.debian.org/debian/dists/bookworm/main/installer-armel/current/images/kirkwood/netboot/marvell/sheevaplug-esata/uInitrd">uInitrd</a>

Now connect the install medium (USB stick, SD card or eSATA disk) to your
plug computer and connect a mini-USB connector in order to access the
serial console.  Start your plug computer and a few seconds later you
should be able to connect to `/dev/ttyUSB1` with 115200 baud.  When you get
serial output, press a key to interrupt the boot process so you can load
the installer.

The instructions for loading the installer depend on where you want to load
the installer from.  Also note that you may have to replace `fatload` with
`ext2load` in case you used the ext2 or ext3 filesystem on your USB stick
or MMC card.

Note for GuruPlug and DreamPlug users: MMC/SD cards show up as USB devices.
Therefore, if you're using a MMC/SD card, make sure to follow the
instructions for USB devices and not for MMC/SD.  Furthermore, you'll have
to use a different device ID: `0:1` is the internal microSD, `1:1` the
external SD card and `2:1` an external USB device, like a USB stick.

<ul>

<li>USB: If you stored the installer on a USB stick, please use:

<div class="code">
<pre>
usb start
fatload usb <span class="input">0:1</span> 0x00800000 /uImage
fatload usb <span class="input">0:1</span> 0x01100000 /uInitrd
</pre>
</div>

</li>

<li>SD: for MMC/SD cards, use:

<div class="code">
<pre>
fatload mmc 0:1 0x00800000 /uImage
fatload mmc 0:1 0x01100000 /uInitrd
</pre>
</div>

</li>

<li>TFTP: if you want to load the installer via the network from a TFTP
server, use this:

<div class="code">
<pre>
setenv serverip 192.168.1.2
setenv ipaddr 192.168.1.147
tftpboot 0x00800000 uImage
tftpboot 0x01100000 uInitrd
</pre>
</div>

Of course, you have to replace <code>192.168.1.2</code> with the IP address of your
TFTP server.

</li>

</ul>

Finally, start the installer:

<div class="code">
<pre>
setenv bootargs console=ttyS0,115200n8 base-installer/initramfs-tools/driver-policy=most
bootm 0x00800000 0x01100000
</pre>
</div>

<h2 id="install">The Installation</h2>

The installation itself should be pretty standard and you can follow the <a
href = "http://www.debian.org/releases/bookworm/armel/">installation
guide</a>.  The installer knows about all supported plug computers and will
create a bootable kernel and ramdisk at the end of the installation.  The
installer will also offer a partition layout that is known to work.  If you
want to choose a different layout, make sure that you create a small (ca.
150 MB) `/boot` partition with the `ext2` filesystem.

When the installation is done, you have to configure u-boot so it will
automatically boot Debian.  Interrupt the boot process of u-boot and enter
the following commands.  For USB, use this:

<div class="code">
<pre>
setenv bootargs_console console=ttyS0,115200
setenv bootcmd_usb 'usb start; ext2load usb 0:1 0x00800000 /uImage; ext2load usb 0:1 0x01100000 /uInitrd'
setenv bootcmd 'setenv bootargs ${bootargs_console}; run bootcmd_usb; bootm 0x00800000 0x01100000'
saveenv
</pre>
</div>

If you're using an SD card, use these commands instead:

<div class="code">
<pre>
setenv bootargs_console console=ttyS0,115200
setenv bootcmd_mmc 'ext2load mmc 0:1 0x00800000 /uImage; ext2load mmc 0:1 0x01100000 /uInitrd'
setenv bootcmd 'setenv bootargs ${bootargs_console}; run bootcmd_mmc; bootm 0x00800000 0x01100000'
saveenv
</pre>
</div>

Finally, use these commands to boot from eSATA:

<div class="code">
<pre>
setenv bootargs_console console=ttyS0,115200
setenv bootcmd_sata 'ide reset; ext2load ide 0:1 0x00800000 /uImage; ext2load ide 0:1 0x01100000 /uInitrd'
setenv bootcmd 'setenv bootargs ${bootargs_console}; run bootcmd_sata; bootm 0x00800000 0x01100000'
saveenv
</pre>
</div>

The commands above use `0:1` to refer to your boot partition.  This
indicates device `0` and partition `1`.  Depending on your configuration
and device, you may have to specify a different boot partition.  Please
refer to the explanation on <a href = "../troubleshooting/#dev-part">how to
find out your boot partition</a> in case your device does not boot with
`0:1`.

Your plug computer is now ready to boot Debian from USB, SD or eSATA
and it will automatically do so whenever you turn on the plug
computer.  You can now type the following command to boot:

<div class="code">
<pre>
run bootcmd
</pre>
</div>

<h2>Additional packages</h2>

On the DreamPlug, you need the non-free `firmware-libertas` package for
WiFi and Bluetooth.

