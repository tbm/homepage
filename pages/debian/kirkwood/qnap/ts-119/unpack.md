---
title: Debian lenny tar ball for QNAP TS-110/TS-119
nav: Manual Installation
description: Manual installation guide of Debian on QNAP TS-110/TS-119
keywords: [Debian, lenny, QNAP, TS-110, TS-119, ARM, armel]
---

<div class="right">
<img src = "../images/r_qnap_ts110.jpg" class="border" alt="QNAP TS-110 from the front" width="148" height="206" />
</div>

<p><b>This page is deprecated.  Please use <a href = "../install/">the
installer</a> instead.</b></p>

This page describes how to manually unpack a tar ball of Debian 5.0 (lenny)
for the QNAP TS-110 and TS-119.  However, please note that the
user-friendly <a href = "../install/">user-friendly Debian installer</a> is
recommended for new installations.

Even though this procedure doesn't require a serial console, I suggest
you only install Debian this way if you can make a serial console for
your QNAP in case something goes wrong.  Note that this procedure will
<em>replace</em> the QNAP firmware in flash with Debian and erase all
your data on your disk.

<h2>Preparing the hard drive</h2>

Start your QNAP device and login via SSH.  Some time after you start your
machine, you will hear a beep and a bit later you'll hear a longer beep.
Wait for a few more seconds and then connect to the machine via SSH.  The
username is `admin` and the password is `admin` too.

Now you can start preparing your disk for Debian.  First of all, you have
to partition the disk.  I have used the partition scheme where a separate
partition is used for `/home`.  Therefore, you need to create `/dev/sda1`
for the boot partition, `/dev/sda2` for the root partition, `/dev/sda3` as
an extended partition from which swap (`sda5`) and home (`sda6`) are
created.  You can use a different layout but in this case you need to adapt
`/etc/fstab` after unpacking the tar ball.

I used the following layout.  There's no particular reason for using this
partitioning layout.  I simply used something similar to what
debian-installer would create but you're welcome to use a different layout,
although root has to be `/dev/sda2` since this is hard-coded in the
ramdisk.

<div class="code">
<pre>
   Device Boot      Start         End      Blocks   Id  System
/dev/sda1   *           1          31      248976   83  Linux
/dev/sda2              32         882     6835657+  83  Linux
/dev/sda3             883        9729    71063527+   5  Extended
/dev/sda5             883         928      369463+  82  Linux swap
/dev/sda6             929        9729    70694001   83  Linux
</pre>
</div>

You have to use `fdisk` to partition your disk.  Run `fdisk /dev/sda` and
then remove all existing partitions (yes, this will destroy all your data,
so make sure you have a backup!).  You can do this with `d` followed by the
partition number (e.g. `d 6 d 5` etc).  Now run `p` to make sure there are
no partitions and write out the changes to disk with `w`.  If you installed
the QNAP firmware to disk previously, you have to restart now so the
changes will take effect.  After the reboot, login as `admin` again.

Okay, now you can go ahead and create the partitions as described above
(press `h` if you need help to see what the commands are).  In my case, I
issues the following commands:

<div class="code">
<pre>
n p 1 1 +512M
n p 2 enter +6G
n e 3 enter enter
n l enter +512M
n l enter enter
t 5 82
a 1
p
w
</pre>
</div>

Now you can format the drive:

<div class="code">
<pre>
mke2fs -T ext2 /dev/sda1
mke2fs -T ext3 -j /dev/sda2
</pre>
</div>

Mount the disk somewhere:

<div class="code">
<pre>
mount /dev/sda2 /mnt/ext
mkdir /mnt/ext/boot
mount /dev/sda1 /mnt/ext/boot
cd /mnt/ext
</pre>
</div>

<h2>Downloading and installing the Debian base system</h2>

Download the compressed base system (about 110 MB) and unpack it.  This
contains a basic system with a standard set of packages of Debian 5.0.3
(lenny, 2009-10-08).

<div class="code">
<pre>
busybox wget http://people.debian.org/~tbm/ts-219/lenny/base.tar.bz2
tar -xjvf base.tar.bz2
</pre>
</div>

Format the remaining partitions:

<div class="code">
<pre>
mount -o bind /dev /mnt/ext/dev
chroot .
cd /dev
MAKEDEV sda
mkfs.ext3 /dev/sda6
mkswap /dev/sda5
exit
umount /mnt/ext/dev
</pre>
</div>

Now we'll make a backup of the flash content:

<div class="code">
<pre>
cat /dev/mtdblock0 &gt; /mnt/ext/root/mtd0
cat /dev/mtdblock1 &gt; /mnt/ext/root/mtd1
cat /dev/mtdblock2 &gt; /mnt/ext/root/mtd2
cat /dev/mtdblock3 &gt; /mnt/ext/root/mtd3
cat /dev/mtdblock4 &gt; /mnt/ext/root/mtd4
cat /dev/mtdblock5 &gt; /mnt/ext/root/mtd5
</pre>
</div>

We're getting close.  Let's download the new flash images and write them to
flash:

<div class="code">
<pre>
busybox wget http://people.debian.org/~tbm/ts-219/lenny/mtd1.bz2
busybox wget http://people.debian.org/~tbm/ts-219/lenny/mtd2.bz2
bzip2 -d mtd*
cat mtd1 &gt; /dev/mtdblock1
cat mtd2 &gt; /dev/mtdblock2
</pre>
</div>

Debian is on disk and in flash now.  Let's clean up and unmount the disk:

<div class="code">
<pre>
rm mtd*
rm base.tar.bz2
cd
umount /mnt/ext/boot
umount /mnt/ext
</pre>
</div>

On the QNAP TS-11x, the MAC address is stored in two locations: the QNAP
firmware will read the MAC address from a special location in flash but the
u-boot configuration also contains a (different) MAC address.  Debian and
QNAP's recovery mode will use the MAC address from u-boot and so it will be
different to what it was with the QNAP firmware.  In order to avoid this
problem, you can update the MAC address stored in the u-boot configuration:

<div class="code">
<pre>
ubootcfg -b 0 -f /dev/mtdblock4 -o - | sed "s/^ethaddr=.*/ethaddr=`get_mac`/" &gt; /tmp/uboot
ubootcfg -b 0 -f /dev/mtdblock4 -i  /tmp/uboot
</pre>
</div>

Finally, restart the machine:

<div class="code">
<pre>
reboot
exit
</pre>
</div>

<h2>Boot the system</h2>

Your machine will start Debian from disk now.  After about 2 minutes, you
should hear a beep and the status light will become green.  You can now
connect to Debian via SSH.  Note that the user name is `root` rather than
`admin` now and that the password is `root` too!  There are no normal users
yet.  The RSA key of the host is:

<div class="code">
<pre>
ae:60:d5:ba:ec:35:62:75:b8:06:5e:a7:e5:30:86:fd
</pre>
</div>

<h2>What to do now</h2>

You now have a working system.  There are a few things you should do,
though:

<ul>

<li>copy the files `/root/mtd*` to another PC and put them in your backup.
You might need them later.</li>

<li>change the root password</li>

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
then type: `apt update`</li>

<li>run `ntpdate pool.ntp.org` to make sure the clock is always up-to-date;
otherwise attempts to install new packages might fail due to GPG
verification errors (for the first time, you'll probably have to setup the
clock manually using the `date` command).</li>

<li>upgrade your system using `apt dist-upgrade` to make sure you have
the latest updates.</li>

<li>change the timezone with `dpkg-reconfigure tzdata`</li>

<li>setup locales with `dpkg-reconfigure locales`</li>

<li>edit `/etc/hostname` to change the hostname.</li>

</ul>

Go back to my <a href = "..">Debian on QNAP TS-11x</a> page.

{{% paypal desc="Debian/QNAP TS-11x donation" %}}

