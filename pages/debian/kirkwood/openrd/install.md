---
title: Debian installer for OpenRD
nav: Installation
description: Installation guide of Debian on OpenRD
keywords: [OpenRD, OpenRD-Base, OpenRD-Client, OpenRD-Ultimate, Marvell, Kirkwood, Debian, installer, ARM]
---

This page explains how to use the Debian installer to install Debian 11
(bullseye) on the OpenRD platform (OpenRD-Base, OpenRD-Client and
OpenRD-Ultimate).

The OpenRD has 512 MB flash memory and SATA, USB and MMC/SD card
interfaces.  The Debian installer doesn't currently support installations
to MTD flash, but you can use it to install to a SATA disk, USB stick or
MMC/SD card.  In order to proceed, you will therefore need either a SATA
disk (connected internally or via eSATA) or a USB stick (or disk).  While
USB sticks work fine, the version of u-boot (the boot loader on the
OpenRD) shipped with this device seems to have some trouble with USB hard disks... they will work
but you may have to restart the device several times so u-boot will find
the disk.  There are also problems booting from USB when more than one USB
device is connected.

<h2 id="prepare">Preparation</h2>

Make sure to connect an Ethernet cable to the `GbE 0` port of your OpenRD
(if you haven't already) because the installer will download files from the
Internet for the installation.

<h2 id="uboot">Upgrading U-Boot</h2>

You have the option to install a new version of the u-boot boot loader but
this step is optional.  Please visit the page describing the <a href =
"../uboot-upgrade/">u-boot upgrade process</a> if you want to use a modern
u-boot provided by Debian.

<h2 id="starting">Starting the Installer</h2>

First of all, you have to download the installer and store them either on a
USB stick or a TFTP server.  Please download the installer images for your
device:

* OpenRD-Base:
[uImage](http://ftp.debian.org/debian/dists/bullseye/main/installer-armel/current/images/kirkwood/netboot/marvell/openrd-base/uImage)
and
[uInitrd](http://ftp.debian.org/debian/dists/bullseye/main/installer-armel/current/images/kirkwood/netboot/marvell/openrd-base/uInitrd)
* OpenRD-Client:
[uImage](http://ftp.debian.org/debian/dists/bullseye/main/installer-armel/current/images/kirkwood/netboot/marvell/openrd-client/uImage)
and
[uInitrd](http://ftp.debian.org/debian/dists/bullseye/main/installer-armel/current/images/kirkwood/netboot/marvell/openrd-client/uInitrd)
* OpenRD-Ultimate:
[uImage](http://ftp.debian.org/debian/dists/bullseye/main/installer-armel/current/images/kirkwood/netboot/marvell/openrd-ultimate/uImage)
and
[uInitrd](http://ftp.debian.org/debian/dists/bullseye/main/installer-armel/current/images/kirkwood/netboot/marvell/openrd-ultimate/uInitrd)

Now connect a mini-USB connector to `System Debug` in order to access the
serial console.  Start your OpenRD and a few seconds later you should be able to connect to
`/dev/ttyUSB1` with 115200 baud.

When you get serial output, press a key to interrupt the boot process.

If you use the original Marvell u-boot (but not if you use [modern DENX
u-boot](../uboot-upgrade/)), you have to configure u-boot so the device
will boot the kernel which is used by Debian:

* If you have an OpenRD-Base, please issue the following commands:

        setenv mainlineLinux yes
        setenv arcNumber 2325
        saveenv
        reset

* If you have an OpenRD-Client, please issue the following commands:

        setenv mainlineLinux yes
        setenv arcNumber 2361
        saveenv
        reset

* If you have an OpenRD-Ultimate, please issue the following commands:

        setenv mainlineLinux yes
        setenv arcNumber 2884
        saveenv
        reset

These commands will put in the correct settings and then restart the device
so the changes will take effect.

Now you can load the installer.  The instructions will depend on where you
want to load the installer from.  Also note that you may have to replace
`fatload` with `ext2load` in case you used the ext2 or ext3 filesystem on
your USB stick.

<ul>

<li>USB: If you stored the installer on a USB stick, please use:

<div class="code">
<pre>
usb start
fatload usb 0:1 0x01100000 /uInitrd
fatload usb 0:1 0x00800000 /uImage
</pre>
</div>

</li>

<li>TFTP: if you want to load the installer via the network from a TFTP
server, use this:

<div class="code">
<pre>
setenv serverip 192.168.1.2
setenv ipaddr 192.168.1.147
tftpboot 0x01100000 uInitrd
tftpboot 0x00800000 uImage
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
href = "http://www.debian.org/releases/bullseye/armel/">installation
guide</a>.  The installer knows about the OpenRD and will create a bootable
kernel and ramdisk at the end of the installation.  The installer will also
offer a partition layout that is known to work.  If you want to choose a
different layout, make sure that you create a small (ca. 150 MB) `/boot`
partition with the `ext2` filesystem.

When the installation is done, you have to configure u-boot so it will
automatically boot Debian.  Interrupt the boot process of u-boot and enter
the following commands.

If you're using a SATA disk, use these commands:

<div class="code">
<pre>
setenv bootargs_console console=ttyS0,115200
setenv bootcmd_sata 'ide reset; ext2load ide 0:1 0x01100000 /uInitrd; ext2load ide 0:1 0x00800000 /uImage'
setenv bootcmd 'setenv bootargs ${bootargs_console}; run bootcmd_sata; bootm 0x00800000 0x01100000'
saveenv
</pre>
</div>

For USB, use this:

<div class="code">
<pre>
setenv bootargs_console console=ttyS0,115200
setenv bootcmd_usb 'usb start; ext2load usb 0:1 0x01100000 /uInitrd; ext2load usb 0:1 0x00800000 /uImage'
setenv bootcmd 'setenv bootargs ${bootargs_console}; run bootcmd_usb; bootm 0x00800000 0x01100000'
saveenv
</pre>
</div>

USB support in u-boot is quite flaky, so if there are problems booting from
your USB device you can add `; reset` at the end of `bootcmd`.  This will
cause the OpenRD to reboot when it fails to load the image and try again,
until it finally manages to load it.

For MMC/SD, use this:

<div class="code">
<pre>
setenv bootargs_console console=ttyS0,115200
setenv bootcmd_mmc 'ext2load mmc 0:1 0x01100000 /uInitrd; ext2load mmc 0:1 0x00800000 /uImage'
setenv bootcmd 'setenv bootargs ${bootargs_console}; run bootcmd_mmc; bootm 0x00800000 0x01100000'
saveenv
</pre>
</div>

If you use the original Marvell u-boot, you have to add `mmcinit` to `bootcmd_mmc`:

<div class="code">
<pre>
setenv bootcmd_mmc 'mmcinit; ext2load mmc 0:1 0x01100000 /uInitrd; ext2load mmc 0:1 0x00800000 /uImage'
saveenv
</pre>
</div>

Please note that you may have to replace `/uInitrd` and `/uImage` with
`/boot/uInitrd` and `/boot/uImage` depending on the way you installed
Debian.  By default, Debian will create a separate boot partition, so the
full path to the kernel is `/uImage`.  However, if you choose to put
everything on the same partition, you have to use `/boot/uImage`.

Your OpenRD is now ready to boot Debian from the USB stick, MMC/SD card or SATA
disk and it will automatically do so whenever you turn on your device.  You can
now type the following command to boot:

<div class="code">
<pre>
run bootcmd
</pre>
</div>

<h2>Success</h2>

You should now have a complete Debian system running on your OpenRD.  You
can use `apt` and other tools to install additional software.  The
OpenRD is an ARM based device and the `armel` architecture is fully
supported by Debian.

Finally, make sure to read the <a href = "../tips/">tips and tricks</a>
about running Debian on the OpenRD.

