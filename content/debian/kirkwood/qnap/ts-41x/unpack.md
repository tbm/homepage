---
title: Debian lenny tar ball for QNAP TS-41x
nav: Manual Installation
description: Manual installation guide of Debian on QNAP TS-41x
keywords: [Debian, lenny, QNAP, TS-410, TS-410U, TS-419, TS-419P, TS-419U, ARM, armel]
---

<% content_for :right do %>
<img src = "../images/r_qnap_ts419p.jpg" class="border" alt="QNAP TS-419P from the front" width="148" height="148" />
<% end %>

<p><b>This page is deprecated.  Please use <a href = "../install/">the
installer</a> instead.</b></p>

<h1>Manually unpacking a tar ball of Debian on QNAP TS-41x</h1>

This page describes how to manually unpack a tar ball of Debian 5.0 (lenny)
for the QNAP TS-41x class devices, i.e. QNAP TS-410, TS-410U, TS-419P and
TS-419U.  However, please note that the user-friendly <a href =
"../install/">user-friendly Debian installer</a> is recommended for new
installations.

Even though this procedure doesn't require a serial console, I suggest you
only install Debian this way if you can make a serial console for your QNAP
in case something goes wrong.  Note that this procedure will
<em>replace</em> the QNAP firmware in flash with Debian and erase all your
data on your disk.

For this procedure, you'll need a QNAP TS-41x device with one or more hard
drives, a USB stick with 1 GB and an SSH client.

Before you start, please ensure that your Ethernet cable is connected to
<em>eth0</em> (i.e. the first Ethernet port) rather than <em>eth1</em> (the
second Ethernet port).  On the TS-419, Ethernet port numeration differs
between the QNAP firmware and Debian.  On Debian, <em>eth0</em> is the
<em>lower</em> (and not the upper) connector!

<h2>Preparing the hard drive</h2>

If you have previously installed the QNAP firmware to disk, you have to
<em>remove</em> all disks before starting your TS-41x device.  Now start
your QNAP device and wait for it to boot.  After a while you you will hear
a beep and a bit later you'll hear a longer beep.  Wait for a few more
seconds and then connect to the machine via SSH.  On the TS-419P, you can
easily find out when to connect by waiting for the IP address to be
displayed on the LCD.  The username is `admin` and the password is `admin`
too.

First of all, put your SATA disks back into your TS-41x and make sure you
put them into the device in the right order, i.e. hdd1 first, then hdd2,
etc.  Then put the USB into the QNAP and wait for the QNAP firmware to
mount the stick.  Presumably, it's formatted with VFAT which won't work for
us.  So unmount the stick and format it:

<div class="code">
<pre>
umount /share/external/sdi1
mke2fs -T ext2 /dev/sdi1
mount /dev/sdi1 /share/external/sdi1
</pre>
</div>

Now you can download a tar ball of Debian lenny and extract it:

<div class="code">
<pre>
cd /share/external/sdi1
busybox wget http://people.debian.org/~tbm/ts-219/lenny/base.tar.bz2
tar -xjvf base.tar.bz2
</pre>
</div>

On the QNAP TS-41x, the MAC address is stored in two locations: the QNAP
firmware will read the MAC address from a special location in flash but the
u-boot configuration also contains a (different) MAC address.  Debian and
QNAP's recovery mode will use the MAC address from u-boot and so it will be
different to what it was with the QNAP firmware.  In order to avoid this
problem, you can update the MAC address stored in the u-boot configuration:

<div class="code">
<pre>
cd /share/external/sdi1/root
ubootcfg -b 0 -f /dev/mtdblock4 -o uboot.orig
busybox wget http://people.debian.org/~tbm/ts-41x/lenny/fix-mac
sh fix-mac
ubootcfg -b 0 -f /dev/mtdblock4 -o uboot.new
</pre>
</div>

Let's make a backup of the QNAP firmware from flash:

<div class="code">
<pre>
cat /dev/mtdblock0 &gt; mtd0
cat /dev/mtdblock1 &gt; mtd1
cat /dev/mtdblock2 &gt; mtd2
cat /dev/mtdblock3 &gt; mtd3
cat /dev/mtdblock4 &gt; mtd4
cat /dev/mtdblock5 &gt; mtd5
</pre>
</div>

Before we enter the Debian chroot, let's copy the network configuration
over:

<div class="code">
<pre>
cp /etc/resolv.conf /share/external/sdi1/etc/
</pre>
</div>

And let's generate udev rules for the network that work with your device:

<div class="code">
<pre>
busybox wget http://people.debian.org/~tbm/ts-41x/lenny/gen-udev-rules
sh gen-udev-rules
</pre>
</div>

Let's enter the Debian system on USB disk to prepare the SATA disk:

<div class="code">
<pre>
cd /tmp
unset LANG
unset LC_ALL
unset LC_CTYPE
mount -t proc none /share/external/sdi1/proc
mount -o bind /dev /share/external/sdi1/dev
chroot /share/external/sdi1
cd /dev
MAKEDEV sda sdb sdc sdd
</pre>
</div>

Now you have to partition and format your SATA disks.  You can use `fdisk`
to partition them.  The RAID and LVM2 tools are available but make sure to
generate a valid `/etc/mdadm.conf` configuration file if you want to use
RAID.  Finally, you should format the partitions with ext2/3.

After you've formatted your disks, you can mount the root filesystem:

<div class="code">
<pre>
mount /dev/whatever /mnt
</pre>
</div>

Unpack the tar ball to the disk:

<div class="code">
<pre>
cd /mnt
apt-get install bzip2
tar -xjvf /base.tar.bz2
</pre>
</div>

Now you have to fix a few things with the tar ball.  First of all, change
the configuration of qcontrol:

<div class="code">
<pre>
rm /mnt/etc/qcontrol.conf
ln -s qcontrol/ts41x.lua /mnt/etc/qcontrol.conf
</pre>
</div>

Copy the network udev rules file over:

<div class="code">
<pre>
mv /root/70-persistent-net.rules /mnt/etc/udev/rules.d/
</pre>
</div>

Finally, edit `/mnt/etc/fstab` and adapt it to your partition layout.

Now we're done with the disk and can unmount it:

<div class="code">
<pre>
umount /mnt
</pre>
</div>

Now we have to obtain the Debian files that have to be written to flash:

<div class="code">
<pre>
mkdir /root/debian
cd /root/debian
wget http://people.debian.org/~tbm/ts-41x/lenny/mtd1.bz2
wget http://people.debian.org/~tbm/ts-41x/lenny/mtd2.bz2
bzip2 -d mtd*
</pre>
</div>

We have to unpack the initramfs and change the root device:

<div class="code">
<pre>
mkdir i
cd i
zcat ../mtd2 | cpio -i
rm -f conf/conf.d/resume
</pre>
</div>

Now edit `conf/param.conf` and replace the root device with the device
where you keep the root filesystem.  <b>Note</b>: if you use LVM, you
<em>have</em> to use the format `/dev/mapper/foo-bar`!  Something like
`/dev/foo/bar` will <em>not</em> work.

OK, let's create the new initramfs:

<div class="code">
<pre>
find . | cpio --quiet -o -H newc &gt; ../new-initrd
cd ..
rm -rf i
gzip -9 new-initrd
dd if=new-initrd.gz of=new-initrd.gz.padded ibs=9437184 conv=sync
</pre>
</div>

Now write the Debian kernel and ramdisk to flash:

<div class="code">
<pre>
cat mtd1 &gt; /dev/mtdblock1
cat new-initrd.gz.padded &gt; /dev/mtdblock2
</pre>
</div>

Leave the chroot and unmount the USB stick:

<div class="code">
<pre>
exit
umount /share/external/sdi1/proc
umount /share/external/sdi1/dev
umount /share/external/sdi1
</pre>
</div>

Now remove the USB stick and restart the machine:

<div class="code">
<pre>
reboot
</pre>
</div>

Put the USB in your PC and make a backup of the `mtd` files from `/root`.

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

<li>Download the GPG key I use to sign the kernel repository so you won't
get any warning from `apt-get`:

<div class="code">
<pre>
gpg --keyserver pgp.earth.li --recv-keys 68FD549F
gpg --export -a 68FD549F | apt-key add -
</pre>
</div>

</li>

<li>Email me at tbm@cyrius.com and let me know that you installed Debian on
your TS-41x -- since Debian on the TS-41x is work in progress, I'd like to
be able to let you know of important updates.</li>

</ul>

Go back to my <a href = "..">Debian on QNAP TS-41x</a> page.

<%= render "paypal", :desc => "Debian/QNAP TS-41x donation" %>

