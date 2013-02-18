---
title: Installing Debian on the Kurobox Pro
nav: Installing Debian
description: Installation instructions for Debian on the Kurobox Pro
keywords: [Buffalo, Revogear, Kurobox Pro, installation]
---

<% content_for :right do %>
<img src = "../images/r_kuroboxpro_front.jpg" class="border" alt="Kurobox Pro from the front" width="148" height="231" />

<%= render "adsense-wideskyscaper-right" %>
<% end %>

<h1>Installing Debian on the Kurobox Pro</h1>

<h2>by Per Andersson and Martin Michlmayr</h2>

In a nutshell, the installation of Debian works like this: you partition
the disk that you will use in the device with `ext2` and put the installer
images on that disk and run a script which effectively will change the
environment for the u-boot boot loader so that it boots from disk rather
than flash.  When you restart your device, the Debian installer starts and
allows you to login via SSH to perform the installation.  Debian will then
be installed to disk.

Following this procedure, Debian will be installed to your SATA disk.  The
Buffalo firmware will remain untouched in flash memory.  If you want to use
the Buffalo firmware again, all you have to do is to change the u-boot
environment and tell it to boot from flash.

<h2>Requirements and Preparation</h2>

In order to install Debian on a Kurobox Pro, you need the following:

<ul>

<li>A Kurobox Pro, obviously.</li>

<li>An internal SATA disk in the device.</li>

<li>A network connection.</li>

<li>Another machine on which you have an SSH and a telnet client.</li>

</ul>

<h2>Making a Backup</h2>

You have to make a backup of all the data stored on your disk before
starting with the installation of Debian since the whole disk will be
formatted during the installation.

<h2>Starting the Installer</h2>

Start your Kurobox Pro and let it boot into the Buffalo firmware.  You'll
hear a short melody when you turn on the device and after about a minute
you'll here another short beep.  You can now connect to your device with
telnet:

<div class="code">
<pre>
telnet <span class="input">192.168.11.150</span>
</pre>
</div>

You have to replace `192.168.11.150` with the actual IP address of your
device.  Use `root` as login name and `kuroadmin` as password.

First of all, you have to change the way the Buffalo firmware does name
resolution.  By default the original firmware only resolves names based on
files (in this case /etc/hosts).  To be able to utilize name servers (DNS)
you will have to change this behaviour.  This is done by altering the file
`/etc/nsswitch.conf` and changing the default line

<div class="code">
<pre>
hosts: files
</pre>
</div>

to

<div class="code">
<pre>
hosts: files dns
</pre>
</div>

This change can be done with the following command:

<div class="code">
<pre>
echo "hosts: files dns" &gt; /etc/nsswitch.conf
</pre>
</div>

Now that you have DNS working, you can set the system clock based on a time
server on the Internet.  On new Kurobox Pro devices, the system clock is
not set properly, which can cause problems later.  Issue the following two
commands in order to obtain the current time from a time server:

<div class="code">
<pre>
rdate -s pool.ntp.org
hwclock -w
</pre>
</div>

Now we can actually start to prepare the disk for the installer.  First you
have to partition the hard disk so the installer image can be stored on the
disk.  For now, we just need a small partition to store the installer.  The
disk will be partitioned again during the actual installation, so don't
worry about partitioning for now.  Let's make a 256 MB partition:

<div class="code">
<pre>
<span class="input">fdisk /dev/sda</span>
Command (m for help): <span class="input">n</span>
Command action
   e   extended
   p   primary partition (1-4)
<span class="input">p</span>
Partition number (1-4): <span class="input">1</span>
First cylinder (1-19457, default 1):<span class="input">press return</span>
Using default value 1
Last cylinder or +size or +sizeM or +sizeK (1-19457, default 19457):
<span class="input">+256M</span>
<span class="input">w</span>
</pre>
</div>

Now format the hard disk with the `ext2` filesystem:

<div class="code">
<pre>
mkfs.ext2 /dev/sda1
</pre>
</div>

Next mount the newly created file system and change the directory to where
you mounted it.

<div class="code">
<pre>
mount -t ext2 /dev/sda1 /mnt/disk1
cd /mnt/disk1
</pre>
</div>

Now you can download the Debian installer images from the web using the
`wget` command:

<div class="code">
<pre>
wget http://ftp.nl.debian.org/debian/dists/stable/main/installer-armel/current/images/orion5x/network-console/buffalo/kuroboxpro/config-debian
wget http://ftp.nl.debian.org/debian/dists/stable/main/installer-armel/current/images/orion5x/network-console/buffalo/kuroboxpro/initrd.buffalo
wget http://ftp.nl.debian.org/debian/dists/stable/main/installer-armel/current/images/orion5x/network-console/buffalo/kuroboxpro/uImage.buffalo
</pre>
</div>

This will download the Debian kernel, the installer ramdisk and a script to
configure the u-boot environment.  Finally, you can run the script by
executing the following command:

<div class="code">
<pre>
sh config-debian
</pre>
</div>

When the command has completed, you should make a copy of `ubootenv.bak` to
a USB stick (rather than to the hard drive since the installation of Debian
will format the disk again).  Apparently the Buffalo firmware doesn't
include the VFAT module, so you have to create the `ext2` filesystem on
your USB stick.  In addition to making a copy of `ubootenv.bak` (a copy of
the u-boot configuration environment before we modified it), you should
make a copy of `/dev/mtdblock1`.  This is the flash partition where the
kernel is stored.  While the installation of Debian won't modify the flash
content, a copy of the kernel may come in handy if you have to use the <a
href = "../recovery">recovery mode</a>.  Follow these steps to make the
backup:

<div class="code">
<pre>
mount -t ext2 /dev/sdb1 /mnt/usbdisk1
cp ubootenv.bak /mnt/usbdisk1
cat /dev/mtdblock1 &gt; /mnt/usbdisk1/mtd1
umount /mnt/usbdisk1
</pre>
</div>

When the command has completed, you can shut down or reboot your device.
The next time you power it on again, the Debian installer will start.

<h2>The Installation</h2>

After you have put the installer images on hard disk, configured u-boot to
boot from the hard disk and restarted your device, the Debian installer
will start.  Since the Kurobox Pro doesn't have any IO device, SSH will be
used for the installation.  The installer will bring up the network, start
the OpenSSH server and you can then connect to the device using SSH.  You
have to wait a few minutes after starting the system before you can
connect.  While the installer is setting up the network and starting SSH,
the power LED will blink.  When the installer is ready and you can login
via SSH, the power LED will become solid and you'll hear a short beep.

Since the Kurobox doesn't have a LCD display, the installer cannot tell you
which IP address to connect to or which password to use.  With regards to
the IP address, the following strategy is used:

<ul>

<li>If your original Buffalo firmware is configured to use DHCP (the
default from Buffalo firmware), Debian installer will try to acquire an IP
address with DHCP.  You can use the MAC address of your device to tell your
DHCP server to give out a specific IP address to your machine.</li>

<li>If you configured a static address in your Buffalo firmware, this
configuration will be used.  However, if your network configuration was
incomplete (e.g. IP address or DNS were missing), the installer will use
DHCP instead.</li>

<li>If DHCP is used but your DHCP server does not respond, the device will
use the fallback address `192.168.11.150`.  If you are unsure what the
address of your device is, unplug the Ethernet cable, start the machine
again, wait until Debian installer is ready for SSH and then plug the cable
back in and connect to this fallback address.</li>

</ul>

Please make sure that the device is on a local network to which only you
have access since the installer uses a very generic password, namely
`install`.  The user is `installer`.  Connect to the installer (again,
replacing the address in the example with the actual IP address of your
device):

<div class="code">
<pre>
ssh installer@<span class="input">192.168.11.150</span>
</pre>
</div>

The installation should be pretty standard and you can follow the <a href =
"http://www.debian.org/releases/stable/armel">installation guide</a>.  The
installer knows about the Kurobox Pro and at the end of the installation it
install a kernel and ramdisk that will automatically boot Debian.  It will
also install the `micro-evtd` package that can be used to control the fan,
LEDs, buzzer and buttons on your device.

The only thing to consider is the partition layout of your disk.  Since we
configured the Kurobox Pro to boot from disk, you have to make sure that
the first primary partition of your disk is the `/boot` partition, that the
bootable flag is set for this partition and that is uses the `ext2`
filesystem.  Again, the installer knows about these requirements and if you
use guided partitioning it will automatically create an appropriate
partition layout.  Please note that the partitioner will default to `Guided
- use the largest continuous free space`, but in most cases you want to
choose `Guided - use entire disk`.

When you get confirmation that the installation has finished, confirm and
wait for the installer to finish.  Once your SSH session terminates, wait a
few minutes before you can connect to your newly installed system via SSH.
You will be able to log in as root or your newly created user.

<h2>Success</h2>

You should now have a complete Debian system running on your device.  You
can use `apt-get` and other tools to install additional software.  The
Kurobox Pro is an ARM based device and the `armel` architecture is fully
supported by Debian.

Go back to my <a href = "..">Debian on Kurobox Pro</a> page.

<div class="bbf">
<%= render "adsense-banner-before-footer" %>
</div>

