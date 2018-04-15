---
title: Debian tar ball for Linksys NSLU2
nav: Installation
description: Manual installation guide of Debian on NSLU2
keywords: [Debian, squeeze, NSLU2, ARM]
---

<div class="right">
<img src = "../images/r_nslu2_front.jpg" class="border" alt="A NSLU2 from the front" width="148" height="218" />
</div>

If you want to run Debian on your NSLU2, you can manually unpack a tar
ball which I have prepared for these systems.  You simply have to attach
the USB drive to a PC running Linux first to prepare it according to the
following instructions.  If you're not running Linux on your PC, you can
use a Linux live CD, such as Knoppix or Debian Live.

<h2>Preparing the hard drive</h2>

First, you have to partition the disk (we'll use `/dev/sdb` in the
following examples but you have to replace this with the device name of
your disk).  I have used the partition scheme where a separate partition is
used for `/home`.  Therefore, you need to create `/dev/sdb1` for the boot
partition, `/dev/sdb2` for the root partition, `/dev/sdb3` as an extended
partition from which swap (`sdb5`) and home (`sdb6`) are created.  You can
use a different layout but in this case you need to adapt `/etc/fstab`
after unpacking the tar ball.  The root partition <em>has</em> to be the
2nd primary partition (i.e. `/dev/sdb2` in this example) since the root
device is hard-coded in the ramdisk.

I used the following layout:

<div class="code">
<pre>
   Device Boot      Start         End      Blocks   Id  System
/dev/sdb1   *           1          31      248976   83  Linux
/dev/sdb2              32         882     6835657+  83  Linux
/dev/sdb3             883        9729    71063527+   5  Extended
/dev/sdb5             883         913      248976   82  Linux swap
/dev/sdb6             914        9729    70814488+  83  Linux
</pre>
</div>

Use `fdisk` to partition your disk (let's call the disk `sdb` for now).
Mark `sdb1` as a bootable partition (press the key `a` in `fdisk`) and make
sure that the partition is labelled as a Linux partition (type 83).  Make
sure that the root partition is large enough to install all the
applications you're interested in (at least 2-3 GB on a hard drive, and
whatever you can spare if you're using a USB stick).  Now format the drive:

<div class="code">
<pre>
mkfs.ext2 /dev/sdb1
mkfs.ext3 /dev/sdb2
mkfs.ext3 /dev/sdb6
mkswap /dev/sdb5
</pre>
</div>

Mount the disk somewhere:

<div class="code">
<pre>
mount /dev/sdb2 /mnt
mkdir /mnt/boot
mount /dev/sdb1 /mnt/boot
</pre>
</div>

<h2>Downloading and installing the Debian base system</h2>

You have to download the compressed base system.  The tar ball contains a
basic system with a standard set of Debian packages.  You can choose
between a tar ball containing Debian 6 (squeeze) and Debian 7 (wheezy):

<ul>

<li>Debian 6 (squeeze): this tar ball is about 150 MB and takes about 465
MB of disk space when you unpack it.  It contains Debian 6.0.7 as of
2013-06-16.

<div class="code">
<pre>
wget http://people.debian.org/~tbm/nslu2/squeeze/base.tar.bz2
wget http://people.debian.org/~tbm/nslu2/squeeze/base.tar.bz2.asc
</pre>
</div>

</li>

<li>Debian 7 (wheezy): this tar ball is about 175 MB and takes about 550 MB
of disk space when you unpack it.  It contains Debian 7.1 as of 2013-06-16.

<div class="code">
<pre>
wget http://people.debian.org/~tbm/nslu2/wheezy/base.tar.bz2
wget http://people.debian.org/~tbm/nslu2/wheezy/base.tar.bz2.asc
</pre>
</div>

</li>

</ul>

Please be aware that these tar balls are not up-to-date and therefore lack
important security updates.  Please upgrade to the latest Debian release
(jessie, version 8) immediately after the installation.

Verify that the GPG signature matches:

<div class="code">
<pre>
gpg --keyserver subkeys.pgp.net --recv-key 68FD549F
gpg --verify base.tar.bz2.asc base.tar.bz2
</pre>
</div>

Now untar this system onto the drive as the `root` user and unmount the
disk:

<div class="code">
<pre>
cd /mnt
tar -xjvf ~/base.tar.bz2
cd /
umount /mnt/boot
umount /mnt
</pre>
</div>

<h2>Boot the system</h2>

Now you have to write the Debian firmware image to your NSLU2.  You can do
this with <a href =
"http://www.nslu2-linux.org/wiki/Main/UpSlug2">`upslug2`</a>, a tool for
Linux and Unix which can be used to write a firmware image to the NSLU2 via
the network (the software is packaged for Debian).

First, you have to put your NSLU2 in upgrade mode:

<ol>

<li>Disconnect any disks and/or devices from the USB ports.</li>

<li>Power off the NSLU2</li>

<li>Press and hold the reset button (accessible through the small hole on
the back just above the power input).</li>

<li>Press and release the power button to power on the NSLU2.</li>

<li>Wait for 10 seconds watching the ready/status LED.  After 10 seconds it
will change from amber to red (old older NSLU2) or dark orange (on newer
machines).  Immediately release the reset button.</li>

<li>The NSLU2 ready/status LED will flash alternately dark orange and green
(there is a 1 second delay before the first green).  The NSLU2 is now in
upgrade mode.</li>

</ol>

Download the firmware image:

* <a href = "http://www.cyrius.com/debian/nslu2/files/armel/sda2-2.6.32-5">Debian 6
(squeeze)</a> (md5sum: `3c1457de133ac0f3a8b1a1423f7d0c2c`)
* <a href = "http://www.cyrius.com/debian/nslu2/files/armel/sda2-3.2.0-4">Debian 7
(wheezy)</a> (md5sum: `adb46e8e114834ef840bc50011361c4b`)

Write the firmware file to your NSLU2 using upslug2:

<div class="code">
<pre>
upslug2 -i sda2-<span class="input">version</span>
</pre>
</div>

Connect your hard drive immediately when upslug2 is done and then your
device will reboot.  The first time you boot, the system will probably
check your drives.  Please wait patiently until this is over.  When the
drive check is done, your NSLU2 will reboot again and directly boot into
your new Debian system.

The system includes support for the Intel IXP4xx network chip (including
the proprietary microcode that is required for operation) and will try to
obtain an IP address via DHCP on eth0.  SSH is installed and remote root
logins are allowed.  The password is <i>root</i>.  There are no users yet.
The RSA key of the host is:

<div class="code">
<pre>
ec:d7:79:86:a1:f9:98:00:3c:df:63:b2:a5:19:00:83
</pre>
</div>

<h2>What to do now</h2>

You now have a working system.  There are a few things you should do,
though:

<ul>

<li>change the root password</li>

<li>add normal user accounts</li>

<li>regenerate the SSH key (since the private key is included in the base
system on my web page) by running:

<div class="code">
<pre>
rm /etc/ssh/ssh_host*
dpkg-reconfigure openssh-server
</pre>
</div>

</li>

<li>edit `/etc/apt/sources.list` and use a Debian mirror close to you and
then type: `apt-get update`</li>

<li>run `ntpdate pool.ntp.org` to make sure the clock is always up-to-date;
otherwise attempts to install new packages might fail due to GPG
verification errors (for the first time, you'll probably have to setup the
clock manually using the `date` command).</li>

<li>upgrade your system using `apt-get dist-upgrade` to make sure you have
the latest updates.</li>

<li>change the timezone with `dpkg-reconfigure tzdata`</li>

<li>setup locales with `dpkg-reconfigure locales`</li>

<li>edit `/etc/hostname` to change the hostname.</li>

<li>edit `/etc/hosts` and change the hostname and domain in the second line.</li>

</ul>

<h2>Troubleshooting</h2>

If you run into any problems installing or running Debian on your Linksys
NSLU2, please read the <a href = "../troubleshooting/">troubleshooting
page</a>.

{{% paypal desc="Debian/NSLU2 donation" %}}

