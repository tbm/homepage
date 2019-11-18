---
title: Troubleshooting Debian on QNAP TS-41x/TS-42x
nav: Troubleshooting
description: Troubleshooting Debian on QNAP TS-41x/TS-42x
keywords: [Debian, QNAP, NAS, TS-410, TS-410U, TS-412, TS-419P, TS-419U, TS-420, TS-421, troubleshooting, problems]
---

<div class="right">
<img src = "../images/r_qnap_ts419p.jpg" class="border" alt="QNAP TS-419P from the front" width="148" height="148" />
</div>

This page describes common problems that users of Debian on the QNAP
TS-410, TS-410U, TS-412, TS-419P, TS-419P+, TS-419P II, TS-419U, TS-420 and TS-421 have run into.  If
you have any problems with your QNAP device, either while trying to install
Debian or when running Debian, please look through this page carefully to
see whether you can find a solution.  If your problem is not covered here,
feel free to contact the <a href =
"http://lists.debian.org/debian-arm/">debian-arm list</a> for help.

<h2 id="installer">Debian installer</h2>

<h3 id="connect">Cannot connect to Debian installer</h3>

If you cannot connect to the Debian installer via SSH, make sure that you
connect the Ethernet cable to the correct port.  Ethernet port numeration
differs between the QNAP firmware and Debian.  Under Debian, `eth0` is the
port marked with "LAN2".  On the TS-419P, this is the lower (and not the
upper) connector!

<h3 id="partman-stuck">Formatting the disk is stuck at 33%</h3>

Formatting the disk may take a long time, especially if you have a large
disk.  Unfortunately, the progress bar is not updated while the disk is
being formatted so you may think that it is stuck (at 33%).  If this
happens, just be patient.  The installer is in fact formatting your disk.

<h2 id="debian">Debian</h2>

<h3 id="no-boot">My QNAP no longer boots</h3>

There can be many reasons why a QNAP running Debian no longer boots,
ranging from a broken disk, to a bad upgrade or configuration.
Unfortunately, it's often impossible to say what the problem is without the
use of a serial console.  The best solution is to connect a serial console
to see what the problem is but not everyone can do that.

Before you do anything, you should listen.  Maybe your QNAP is performing
its regular filesystem check and this will delay the boot process.  This
delay can be considerable if you have a large disk.  If you can hear that
your hard drive is being accessed, just wait for a few hours.

If your hard drive is quiet and Debian doesn't start, you should try is to
connect your USB drive to another PC and to check the log files:

<div class="code">
<pre>
sudo mount /dev/sda2 /mnt
</pre>
</div>

Now you can look at the files in `/mnt/var/log`, in particular at the file
`syslog`.  If this file doesn't contain any information about the last boot
attempt (which is quite likely), you can enable `bootlogd` which will
record early boot messages:

<div class="code">
<pre>
sudo sed -i "s/BOOTLOGD_ENABLE=No/BOOTLOGD_ENABLE=yes/" /mnt/etc/default/bootlogd
sudo umount /mnt
</pre>
</div>

Connect the drive to your QNAP, boot it, wait a few minutes, then turn it
off and connect the drive to your PC again and mount it.  Now look at the
file `/mnt/var/log/boot` which might tell you more.

One common cause for boot problems is related to filesystem checks and
running `fsck` over all partitions may help.  There are several reasons why
this might help.  For example, the Linux ext3 filesystem has to be checked
periodically.  Even though Debian has been configured not to prompt the
user during the filesystem check, it might still do so in case of serious
errors.  Without a serial console, this prompt means that your QNAP will
hang waiting for user input.

Turn your QNAP off, connect the disk to another machine running Linux and
run `fsck` over all partitions containing data.  On a normal Debian
installation, this includes `sda1` (`/boot`), `sda2` (`/`) and `sda6`
(`/home`):

<div class="code">
<pre>
sudo fsck /dev/sda1
sudo fsck /dev/sda2
sudo fsck /dev/sda6
</pre>
</div>

If none of this helps, I'm afraid you probably have to connect <a href =
"../serial/">a serial console</a> or use the <a href =
"../recovery/">recovery mode</a> to flash the Debian installer and to
perform a new installation.

<h3 id="ramdisk-space">Not enough space for initrd in MTD</h3>

When upgrading your system, you might get an error message like this:

    Not enough space for initrd in MTD 'RootFS1' (need 9670100 but is actually 9437184).

The kernel and initramfs (the initial ramdisk that loads Debian from
disk) are stored in MTD flash.  There's only 9 MB available for the
initramfs.  This might not be enough if you use LVM or RAID.

If this is the case, you can apply the following workaround:

    echo "COMPRESS=xz" | sudo tee /etc/initramfs-tools/conf.d/compress

This configures initramfs-tools to use XZ compression, which achieves
higher compression.  Hopefully your ramdisk will not fit in flash.  If
it still doesn't fit, there's unfortunately not much you can do.

The initramfs in Debian buster is larger than in previous releases
[due to the inclusion of OpenSSL](http://bugs.debian.org/930752)
and unfortunately there's no fix or workaround for that issue.

