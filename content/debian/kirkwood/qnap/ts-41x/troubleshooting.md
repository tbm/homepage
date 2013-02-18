---
title: Troubleshooting Debian on QNAP TS-41x
nav: Troubleshooting
description: Troubleshooting Debian on QNAP TS-41x
keywords: [Debian, QNAP, NAS, TS-410, TS-410U, TS-412, TS-419P, TS-419U, troubleshooting, problems]
---

<% content_for :right do %>
<img src = "../images/r_qnap_ts419p.jpg" class="border" alt="QNAP TS-419P from the front" width="148" height="148" />

<%= render "adsense-wideskyscaper-right" %>
<% end %>

<h1>Troubleshooting</h1>

This page describes common problems that users of Debian on the QNAP
TS-410, TS-410U, TS-412, TS-419P, TS-419P+ and TS-419U have run into.  If
you have any problems with your QNAP TS-41x, either while trying to install
Debian or when running Debian, please look through this page carefully to
see whether you can find a solution.  If your problem is not covered here,
feel free to contact the <a href =
"http://lists.debian.org/debian-arm/">debian-arm list</a> for help.

<h2><a id = "installer">Debian installer</a></h2>

<h3><a id = "connect">Cannot connect to Debian installer</a></h3>

If you cannot connect to the Debian installer via SSH, make sure that you
connect the Ethernet cable to the correct port.  Ethernet port numeration
differs between the QNAP firmware and Debian.  Under Debian, `eth0` is the
port marked with "LAN2".  On the TS-419P, this is the lower (and not the
upper) connector!

<h3><a id = "partman-stuck">Formatting the disk is stuck at 33%</a></h3>

Formatting the disk may take a long time, especially if you have a large
disk.  Unfortunately, the progress bar is not updated while the disk is
being formatted so you may think that it is stuck (at 33%).  If this
happens, just be patient.  The installer is in fact formatting your disk.

<h2><a id = "debian">Debian</a></h2>

<h3><a id = "no-boot">My QNAP no longer boots</a></h3>

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
"../serial">a serial console</a> or use the <a href =
"../recovery">recovery mode</a> to flash the Debian installer and to
perform a new installation.

<%= render "paypal", :desc => "Debian/QNAP TS-41x donation" %>

<div class="bbf">
<%= render "adsense-banner-before-footer" %>
</div>

