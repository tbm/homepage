---
title: Cloning a NSLU2
nav: Clone
description: Cloning a NSLU2
keywords: [NSLU2, Linksys NSLU2, Debian, clone]
---

<div class="right">
<img src = "../images/r_nslu2_front.jpg" class="border" alt="A NSLU2 from the front" width="148" height="218" />
</div>

When you have installed Debian on one Linksys NSLU2, it is relatively easy
to clone your installation for a second NSLU2.  This pages describes the
steps necessary to clone an existing NSLU2.

Before you start, I have to mention one complication: as of Debian 6.0,
device names like `/dev/sdaX` are no longer used in `/etc/fstab` and UUIDs
are used instead.  UUIDs are unique IDs that identify a partition.  While
the use of UUIDs has certain advantages (for example, you can connect more
than one disk to your NSLU2 without Linux confusing which disk is which),
it makes cloning a NSLU2 harder.  There are two ways around this problem:

1. Convert `/etc/fstab` to use device names: edit `/etc/fstab` and replace
all UUIDs with `/dev/sdaX` device names.  Then run `update-initramfs -u` to
generate a new ramdisk.
2. Make sure that the second disk uses the same UUIDs: After formatting a
partition with the ext2/3 filesystem, you can set the UUID with `tune2fs
-U`.  When creating swap, use `mkswap -U` to set the UUID.

In the following example, we'll assume that you are using `/dev/sdaX`
device names in `/etc/fstab`.

In order to clone your NSLU2, start your first NSLU2 and make a copy of the
flash content:

<div class="code">
<pre>
cat /dev/mtdblock* &gt; nslu2-backup
</pre>
</div>

Copy the file `nslu2-backup` to another machine and turn your NSLU2 off.
Now connect the USB drive from your first NSLU2 to your PC and make a tar
ball of the whole disk (the following examples assume the standard Debian
layout):

<div class="code">
<pre>
mount /dev/sda2 /mnt
mount /dev/sda1 /mnt/boot
mount /dev/sda6 /mnt/home
cd /mnt
tar -cjpf ~/nslu2.tar.bz2 .
</pre>
</div>

Now disconnect this drive and connect the drive from the second NSLU2.  You
have to partition and format the disk.  Please see the <a href =
"../unpack/">manual installation of Debian</a> for more information on how
to partition and format the disk.  Make sure to use exactly the same layout
as the first disk.  Now format it:

<div class="code">
<pre>
mkfs.ext2 /dev/sdb1
mkfs.ext3 /dev/sdb2
mkfs.ext3 /dev/sdb6
mkswap /dev/sdb5
</pre>
</div>

And mount the disk:

<div class="code">
<pre>
mount /dev/sda2 /mnt
mkdir /mnt/boot /mnt/home
mount /dev/sda1 /mnt/boot
mount /dev/sda6 /mnt/home
</pre>
</div>

Now you can unpack the tar file:

<div class="code">
<pre>
cd /mnt
tar -xjvf ~/nslu2.tar.bz2
</pre>
</div>

You have to make some changes to the disk.  Edit
`/mnt/etc/udev/rules.d/70-persistent-net.rules` and replace the existing
content with the following line:

<div class="code">
<pre>
SUBSYSTEM=="net", ACTION=="add", DRIVERS=="ixp4xx_eth", ATTR{type}=="1", KERNEL=="eth*", NAME="eth0"
</pre>
</div>

This is important because this file will contain the MAC address of your
first NSLU2 and is therefore not appropriate for your new NSLU2.  The new
configuration doesn't specify a MAC and will work with any NSLU2.

Finally unmount the disk:

<div class="code">
<pre>
cd /
umount /mnt/home
umount /mnt/boot
umount /mnt
</pre>
</div>

Connect the new disk to your new NSLU2 and upload the firmware image
previously generated (`nslu2-backup`) with upslug2.  Your second NSLU2
should now run Debian as well!

