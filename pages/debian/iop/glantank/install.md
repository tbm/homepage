---
title: Installing Debian on GLAN Tank
nav: Installing Debian
description: Installation instructions for Debian on GLAN Tank
keywords: [IOP, GLAN Tank, Supertank, SOTO-HDLGW, IO-Data, ARM, Debian, installation]
---

<div class="alert alert-danger">

Intel's IOP platform is no longer supported in Debian.

</div>

While the GLAN Tank is supported in Debian 7 (wheezy), it is no longer
supported in Debian 8 (jessie) or later releases.

<h2>Requirements</h2>

In order to install Debian on a GLAN Tank, you need the following:

<ul>

<li>A GLAN Tank (SOTO-HDLGW).  In theory, devices from the HDL-Gxxx,
HDL-GWxxx and HDL-GZxxx series are very similar and might work but in
practice only the GLAN Tank is tested.</li>

<li>An IDE hard drive for the installation.</li>

<li>Either an external USB enclosure for the hard drive or a PC in which
you can temporarily put the hard drive.  This is needed because you have to
prepare the hard drive for installation.</li>

<li>Another machine on which you have an SSH client.  Every Linux
distribution includes an OpenSSH client and there is <a href =
"http://www.chiark.greenend.org.uk/~sgtatham/putty/download.html">PuTTY</a>
for Windows.</li>

<li>Ideally, you'd have another machine on which you can run a DHCP server
but this is not strictly necessary.</li>

</ul>

<h2>Preparations</h2>

Since the GLAN Tank can only boot from an internal hard drive (and not, for
example, from the network) you need to manually put some files needed to
start Debian's installer on the hard drive you wish to use for the GLAN
Tank.  The easiest way to do this is to put the IDE hard drive into an USB
enclosure and connect it to your PC.  Alternatively, you can also put the
hard drive directly into your PC.

Once your hard drive is connected to your PC, you need to partition it.
The specific layout doesn't matter because you will re-partition the hard
drive during the installation anyway, but for now you need one partition
(`hda1`, the first primary partition on the IDE drive) on which to put the
installation files.

Using `fdisk` or a similar utility, you can create one partition on your
disk with about 100 MB.  Note that when you put the drive into an USB
enclosure, it will be detected as `sda` or `sdb`.  In the following
example, we have an empty 8 GB disk on which we create one partition with
100 MB:

<div class="code">
<pre>
sudo fdisk /dev/sdb
...
Command (m for help): <span class="input">p</span>

Disk /dev/sdb: 8700 MB, 8700346368 bytes
255 heads, 63 sectors/track, 1057 cylinders
Units = cylinders of 16065 * 512 = 8225280 bytes

   Device Boot      Start         End      Blocks   Id  System

Command (m for help): <span class="input">n</span>
Command action
   e   extended
   p   primary partition (1-4)
<span class="input">p</span>
Partition number (1-4): <span class="input">1</span>
First cylinder (1-1057, default 1): <span class="input">1</span>
Last cylinder or +size or +sizeM or +sizeK (1-1057): <span class="input">+100M</span>

Command (m for help): <span class="input">write</span>
The partition table has been altered!

Calling ioctl() to re-read partition table.
Syncing disks.
</pre>
</div>

Now that the partition has been created, we can format and mount it:

<div class="code">
<pre>
sudo mke2fs /dev/sdb1
...
sudo mount /dev/sdb1 /mnt
</pre>
</div>

Now you need to download the files needed for the installation and copy
them to the hard drive:

<div class="code">
<pre>
cd $HOME
wget http://ftp.uk.debian.org/debian/dists/wheezy/main/installer-armel/current/images/iop32x/network-console/glantank/initrd.gz
wget http://ftp.uk.debian.org/debian/dists/wheezy/main/installer-armel/current/images/iop32x/network-console/glantank/zImage
sudo cp initrd /mnt
sudo cp zImage /mnt
</pre>
</div>

Finally, you can unmount the drive, take it out of your USB enclosure or PC
and put it in the GLAN Tank.

<h2>Starting the installation</h2>

You can perform the installation of Debian by connecting to your GLAN Tank
via SSH.  The files you have just copied to the hard drive include an
installer image that will start a SSH server and allow you to connect over
the network.  By default, the installer will ask a DHCP server in your
network for an IP configuration.  Ideally, you would have a DHCP server
which provides the GLAN Tank with all necessary information, such as IP and
gateway, as well as information such as the hostname.  If the installer
cannot find a DHCP server on your network, it will fall back to a static
configuration, namely the IP address `192.168.1.77` and a gateway and name
server at `192.168.1.1`.  If neither DHCP is available to you nor will
these static values work in your case, you need to <a href =
"../preseed/">preseed other values</a> into your installer image.

After you turn your GLAN Tank on, you have to wait for about 5 minutes
before you can connect via SSH.  Once SSH is available, you can connect
with the following command and log in with the password `install`:

<div class="code">
<pre>
ssh installer@<span class="input">192.168.1.77</span>
</pre>
</div>

<h2>Installing Debian</h2>

The installation itself should be pretty standard and you can follow the <a
href = "http://www.debian.org/releases/wheezy/armel/">installation
guide</a>.  The only thing you have to keep in mind is that the GLAN Tank
requires a `/boot` partition as `hda1` and assumes that the root partition
is on `hda2`.  If you following the guided partitioning, which I recommend,
the installer will create an appropriate partition layout for you:

<p><img src = "../images/partman-guided.png" class="border" alt = "Guided Partitioning" width="802" height="482" /></p>

<p><img src = "../images/partman-disk.png" class="border" alt = "Guided Partitioning: choosing the disk" width="802" height="482" /></p>

<p><img src = "../images/partman-overview.png" class="border" alt = "Partitioning: overview" width="802" height="482" /></p>

The whole installation will take about one hour.  After the installation is
complete, you will be able to log in as `root`.

After the installation, you can login to your newly installed Debian system
as `root` or the user you created during the installation via SSH.

<h3>Status</h3>

Note that kernel support is still very basic.  It lacks support for:

<ul>

<li>Fan control</li>

<li>LEDs</li>

<li>Beeper</li>

</ul>

