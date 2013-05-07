---
title: Debian lenny tar ball for SheevaPlug
nav: Manual Installation
description: Manual installation guide of Debian on SheevaPlug
keywords: [SheevaPlug, Marvell, Kirkwood, Debian, lenny, ARM]
---

<% content_for :right do %>
<img src = "../images/r_sheevaplug_hand.jpg" class="border" alt="SheevaPlug in my hand" width="148" height="129" />

<%= render "adsense-wideskyscaper-right" %>
<% end %>

<h1>Manually unpacking a tar ball of Debian on SheevaPlug</h1>

Since the Debian installer can only be used to install Debian testing
(squeeze), here is a description of how to manually unpack a tar ball of
Debian stable (lenny, version 5.0) for the SheevaPlug.  You need a PC
running Linux to perform this installation but you can use a Linux live CD,
such as Knoppix or Debian Live, if Linux is not installed on your PC.

The SheevaPlug has 512 MB flash memory and a USB and SD card interface.
Debian can, in theory, be installed to any of them but currently only
installations to a USB stick or disk as well as to an SD card are described
here.  Please note that while USB sticks work fine, the current version of
u-boot (the boot loader on the SheevaPlug) seems to have <a href =
"http://openplug.org/plugforum/index.php?topic=131.0">some trouble</a> with
USB hard disks... they will work but you may have to restart the device
several times so u-boot will find the disk.  There are also problems
booting from USB when more than one USB device is connected.

In order to proceed, you will either need a USB stick (or disk) or an SD
card with at least 512 MB storage.  If you're running a version of u-boot
older than 3.4.19 you have to <a href = "../uboot-upgrade/">upgrade
u-boot</a> before proceeding with this installation!  Version 3.4.19 adds
SD support and improves USB support.

<h2>Preparing the USB stick or SD card</h2>

First, you have to partition the USB stick or SD card. (Note: if you want
to install to SD card but don't have an SD card reader in your PC, you can
install to a USB stick and then use the SheevaPlug to prepare the SD card.)
I have used a small partition for `/boot`, one large partition for the
system and other data and one for swap.  Therefore, you need to create
three partitions: the first physical partition (something like `/dev/sda1`
for USB and `/dev/mmcblk0p1` for SD) for the boot partition, `/dev/sda2`
(or `/dev/mmcblk0p2`) for the system partition and the third physical
partition (`/dev/sda3` or `/dev/mmcblk0p3`) for swap.  You can use a
different layout but in this case you need to adapt `/etc/fstab` after
unpacking the tar ball (and later adapt the command line passed to the
kernel).  If you change the layout, I suggest you still create a small
`/boot` partition because otherwise u-boot might have trouble loading
Debian.

I used the following layout:

<div class="code">
<pre>
   Device Boot      Start         End      Blocks   Id  System
/dev/sda1   *           1          14      112423+  83  Linux
/dev/sda2              15         210     1574370   83  Linux
/dev/sda3             211         251      329332+  82  Linux swap
</pre>
</div>

Use `fdisk` to partition your disk (let's call the disk `sda` for now;
remember, if you want to use an SD card, you have to use `/dev/mmcblk0`).
Mark `sda1` as a bootable partition (press the key `a` in `fdisk`) and make
sure that the partition is labelled as a Linux partition (type 83).  Mark
the third partition as a swap partition (type 82).  Now format the drive:

<div class="code">
<pre>
% mkfs.ext2 -I 128 /dev/sda1
% mkfs.ext2 /dev/sda2
% mkswap /dev/sda3
</pre>
</div>

Mount the disk somewhere:

<div class="code">
<pre>
% mount /dev/sda2 /mnt
% mkdir /mnt/boot
% mount /dev/sda1 /mnt/boot
</pre>
</div>

<h2>Downloading and installing the Debian base system</h2>

Download the compressed base system (about 125 MB; it will require about
365 MB of disk space when you unpack it).  This contains a basic system
with a standard set of packages of Debian 5.0.4 (lenny, 2010-06-13).

<div class="code">
<pre>
% wget http://people.debian.org/~tbm/sheevaplug/lenny/base.tar.bz2
% wget http://people.debian.org/~tbm/sheevaplug/lenny/base.tar.bz2.asc
</pre>
</div>

Verify that the GPG signature matches:

<div class="code">
<pre>
% gpg --keyserver subkeys.pgp.net --recv-key 68FD549F
% gpg --verify base.tar.bz2.asc base.tar.bz2
</pre>
</div>

Now untar this system onto the USB stick or SD card as the `root` user:

<div class="code">
<pre>
% cd /mnt
% tar -xjvf ~/base.tar.bz2
</pre>
</div>

If you're using an SD card, you have to edit `/mnt/etc/fstab` and replace
`/dev/sdaX` with `/dev/mmcblk0pX` (for each partition).  If you're using a
USB stick, you don't have to edit this file.

Finally, unmount the device:

<div class="code">
<pre>
% cd /
% umount /mnt/boot
% umount /mnt
</pre>
</div>

<h2>Boot the system</h2>

Now connect the USB stick to your SheevaPlug or enter the SD card and
connect a mini-USB connector in order to access the serial console.  Start
your SheevaPlug and a few seconds later you should be able to connect to
`/dev/ttyUSB1` with 115200 baud.  If you need help accessing the serial
console, check out <a href =
"http://www.plugcomputer.org/Documentation/howtos/serial-terminal/">this
guide</a> on the Plug Computer wiki.

When you get serial output, press a key to interrupt the boot process.  We
now have to configure the boot loader.  First of all, you have to change a
setting so the device will boot the kernel which is used by Debian:

<div class="code">
<pre>
setenv mainlineLinux yes
setenv arcNumber 2097
saveenv
reset
</pre>
</div>

These command will put in the correct settings and then restart the device
so the changes will take effect.  Now you can configure your machine to
boot.  If you're using a USB device, execute these commands so it will
boot:

<div class="code">
<pre>
setenv bootargs_console console=ttyS0,115200
setenv bootargs_root 'root=/dev/sda2 rootdelay=10'
setenv bootcmd_usb 'usb start; ext2load usb 0:1 0x00800000 /uImage; ext2load usb 0:1 0x01100000 /uInitrd'
setenv bootcmd 'setenv bootargs $(bootargs_console) $(bootargs_root); run bootcmd_usb; bootm 0x00800000 0x01100000'
saveenv
</pre>
</div>

If you're using an SD card, use these commands instead:

<div class="code">
<pre>
setenv bootargs_console console=ttyS0,115200
setenv bootargs_root 'root=/dev/mmcblk0p2'
setenv bootcmd_mmc 'mmc init; ext2load mmc 0:1 0x00800000 /uImage; ext2load mmc 0:1 0x01100000 /uInitrd'
setenv bootcmd 'setenv bootargs $(bootargs_console) $(bootargs_root); run bootcmd_mmc; bootm 0x00800000 0x01100000'
saveenv
</pre>
</div>

Your SheevaPlug is now ready to boot Debian from the USB stick or SD card
and it will automatically do so whenever you turn on the SheevaPlug.
Before you start Debian for the first time, I suggest you disconnect the
Ethernet cable.  This is because Debian has been configured with a default
root password, so it is a good idea to change the password before you
connect the machine to the network.

Disconnect the Ethernet cable and then type the following command to boot:

<div class="code">
<pre>
run bootcmd
</pre>
</div>

Your SheevaPlug will now boot Debian.  Please note that you will see some
scary errors about `mtdblock1` during the boot process.  You can simply
ignore those errors.

When Debian has started, you can login as user `root` with the password
`root`.  Please change the password and then plug the Ethernet cable back
in.  SSH is installed and remote root logins are allowed.  The RSA key of
the host is:

<div class="code">
<pre>
ae:60:d5:ba:ec:35:62:75:b8:06:5e:a7:e5:30:86:fd
</pre>
</div>

<h2>What to do now</h2>

You now have a working system.  There are a few things you should do,
though:

<ul>

<li>add normal user accounts</li>

<li>regenerate the SSH key (since the private key is included in the base
system on my web page) by running:

<div class="code">
<pre>
rm /etc/ssh/ssh_host*
ssh-keygen -t dsa -f /etc/ssh/ssh_host_dsa_key -N ""
ssh-keygen -t rsa -f /etc/ssh/ssh_host_rsa_key -N ""
</pre>
</div>

</li>

<li>edit `/etc/apt/sources.list` and use a Debian mirror close to you and
then type: `apt-get update`</li>

<li>run `ntpdate pool.ntp.org` to make sure the clock is always up-to-date;
otherwise attempts to install new packages might fail due to GPG
verification errors.</li>

<li>upgrade your system using `apt-get dist-upgrade` to make sure you have
the latest updates.  If a new kernel gets installed, make sure to run
`flash-kernel` in order to activate it.</li>

<li>change the timezone with `dpkg-reconfigure tzdata`</li>

<li>setup locales with `dpkg-reconfigure locales`</li>

<li>edit `/etc/hostname` to change the hostname.</li>

<li>Download the GPG key I use to sign the kernel repository so you won't
get any warning from `apt-get`:

<div class="code">
<pre>
gpg --keyserver pgp.earth.li --recv-keys 68FD549F
gpg --export -a 68FD549F | apt-key add -
</pre>
</div>

</li>

</ul>

Go back to my <a href = "..">Debian on SheevaPlug</a> page.

<%= render "paypal", :desc => "Debian on Plug Computer donation" %>

<div class="bbf">
<%= render "adsense-banner-before-footer" %>
</div>

