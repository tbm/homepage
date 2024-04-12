---
title: Boot process of Debian on plug computers
nav: Boot Process
description: Boot process of Debian on plug computers
keywords: [SheevaPlug, GuruPlug, Marvell, Kirkwood, Debian, boot process, boot]
---

<div class="right">
<img src = "../images/r_sheevaplug_hand.jpg" class="border" alt="SheevaPlug in my hand" width="148" height="129" />
</div>

This page describes the complete boot process of plug computers (such as
SheevaPlug) running Debian.  While the information from this document is
not needed to run Debian on your plug computer, some users might find it
interesting to know what's going on behind the scenes.

<h2>Debian Variants</h2>

Since Debian is a very popular distribution for plug computers, there are a
lot of different instructions on the Internet explaining how to install
Debian.  Furthermore, some plug computers come with a variant of Debian
pre-installed.  While these systems are variants of Debian, they can differ
quite significantly to the Debian you get when you use the official
installation method, Debian's installer (known as debian-installer).  This
page covers installations made with Debian's installer.

Since a lot of pre-installed Debian variants replace the Linux kernel
shipped by Debian with their own, a good way to verify that you're running
a Debian system created by Debian's installer is to check whether you're
running a Debian kernel.  To check the kernel version, issue this command:

<pre>
uname -r
</pre>

If the result is in the form `2.6.XX` or `2.6.XX.YY`, then you're not
running a Debian kernel and the description of the boot process on this
page will not apply to your device.

The correct result for the official Debian kernel is in the form
`4.XX.YY-Z-marvell` (or `3.XX.YY-Z-kirkwood` for older versions): `4.XX.YY`
indicates the upstream version of the Linux kernel, `Z` indicates the
kernel ABI in Debian and `marvell` is the name of the kernel flavour.  The
kernel ABI is changed whenever we make an incompatible change to the
kernel.  In addition to the kernel ABI, the Debian kernel also has a
version.  The specific version of the kernel you're running can be found in
`/proc/version`.  This file contains the string `Debian 4.XX.YY-ZZ` in
brackets where `ZZ` is the revision of the Debian kernel.

<h2>Booting Debian</h2>

The boot loader used on plug computers is called u-boot.  When you turn
your plug computer on, u-boot is called and will initialize the hardware.
It will then call the commands listed in the `bootcmd` environment variable
in order to boot.  The settings of this variable depends on the type of
storage device you're booting from.  Let's use USB as an example to explain
the u-boot variables used to boot Debian.  There are three variables
(`bootargs_console`, `bootcmd_usb` and `bootcmd`) that are relevant:

<table class="table table-hover">

<thead>
<tr>
<th>Variable</th>
<th>Setting</th>
</tr>
</thead>

<tbody>
<tr>
<td><code>bootargs_console</code></td>
<td><code>console=ttyS0,115200</code></td>
</tr>

<tr>
<td><code>bootcmd_usb</code></td>
<td><code>usb start; ext2load usb 0:1 0x00800000 /uImage; ext2load usb 0:1 0x01100000 /uInitrd</code></td>
</tr>

<tr>
<td><code>bootcmd</code></td>
<td><code>setenv bootargs ${bootargs_console}; run bootcmd_usb; bootm 0x00800000 0x01100000</code></td>
</tr>
</tbody>

</table>

During the boot process, each command listed in `bootcmd` is
executed.  There are three commands:

1. The first command (`setenv bootargs ${bootargs_console}`) sets the
`bootargs` variable to the value of the `bootargs_console` variable.  In
the example, `bootargs_console` is set to `console=ttyS0,115200` so
`bootargs` will receive this setting.  When the Linux kernel is booted,
this `bootargs` variable is passed to the kernel.  As a result,
`console=ttyS0,115200` will be passed to the Linux kernel and this will
ensure that the serial console will work under Linux.
Typically we would also set a `root` parameter to indicate the root
device.  However, this is usually not necessary for Debian on plug
computers since we put the name of the root device into the ramdisk (see
below).  You only have to set a `root` parameter when you want to move your
installation to another storage device.
2. Second, the command `run bootcmd_usb` causes the commands listed in the
`bootcmd_usb` variable to be executed (or similar commands for SATA and
MMC/SD).  This variable consists of three commands: The first command (`usb
start`) initializes the USB system (or SATA/MMC).  The second command
(`ext2load usb 0:1 0x00800000 /uImage`) loads the kernel(`/uImage`) from
USB partition `0:1` to RAM (at location `0x00800000`).  Finally, the
ramdisk (`/uInitrd`) is loaded to RAM (at location `0x01100000`).
3. Finally, the `bootm` command tells u-boot to execute the Linux kernel
and ramdisk from RAM.  A ramdisk is a small Linux system that is executed
in RAM and which is used to boot the full Debian system from disk.  The
ramdisk includes drivers that are required to boot Debian from disk, such
as filesystem and storage modules.

At this point, the boot process is the same as with any other Debian
system.  The only difference is that the ramdisk on plug computers contains
the name of the root device (but it can be overridden with a `root`
parameter passed to the kernel).

<h2>Upgrading the Linux kernel in Debian</h2>

When you install a new version of the Debian kernel package, a number of
steps are performed automatically in order to make sure you can boot the
new kernel:

1. When you install a kernel package, the file `/boot/vmlinuz-$VERSION` is
installed and modules are installed under `/lib/modules/$VERSION` ($VERSION
indicates the output of `uname`&nbsp;`-r` from the new kernel).
2. The program `initramfs-tools` is called to generate the ramdisk on disk
(`/boot/initrd.img-$VERSION`).  During the ramdisk generation, the script
`/usr/share/initramfs-tools/hooks/flash_kernel_set_root` is called on plug
computers to write the name of the root device to the ramdisk.
3. Finally, `flash-kernel` is called to activate the new kernel.  Despite
the name, `flash-kernel` does not write the kernel to flash on plug
computers.  Instead, it takes the kernel (`/boot/vmlinuz`) and ramdisk
(`/boot/initrd.img`) and generates u-boot images (`/boot/uImage` and
`/boot/uInitrd`, respectively) out of them with the help of `mkimage`.
This step is required because u-boot cannot load the kernel and ramdisk
directly and requires special images made with `mkimage`.

