---
title: Troubleshooting Debian on Linksys NSLU2
nav: Troubleshooting
description: Troubleshooting Debian on Linksys NSLU2
keywords: [NSLU2, Linksys NSLU2, Debian, troubleshooting, problems]
---

<% content_for :right do %>
<img src = "../images/r_nslu2_front.jpg" class="border" alt="A NSLU2 from the front" width="148" height="218" />
<% end %>

<h1>Troubleshooting</h1>

This page describes common problems that users of Debian on the Linksys
NSLU2 have run into.  If you have any problems with your NSLU2, either
while trying to install Debian or when running Debian, please look through
this page carefully to see whether you can find a solution.  If your
problem is not covered here, feel free to contact the <a href =
"http://lists.debian.org/debian-arm/">debian-arm list</a> for help.

<h2><a id = "debian">Debian</a></h2>

<h3><a id = "unpack">Debian doesn't boot after manually unpacking the tar ball</a></h3>

There can be a lot of reasons for that.  The manual installation method
involves a lot of different steps, so there's a lot of potential to get
something wrong that will cause your NSLU2 not to boot.  Please take a
close look at the <a href = "../unpack/">installation steps</a> again and
make sure you followed everything correctly.  For example, if you used a
non-standard disk layout, did you update `/etc/fstab` accordingly?

<h3><a id = "two-disks">Debian no longer boots after connecting a second disk</a></h3>

Some users connect a second disk or USB stick to their NSLU2 and find that
the machine no longer boots.  The reason for this is that Debian lenny uses
names like `/dev/sda1` to refer to your disk but there is no guarantee for
device ordering with USB devices.  This means that when you connect a
second drive, your `sda` device might (or might not) become `sdb`, causing
Debian to fail to boot because it's trying to access the wrong drive.

The solution for this problem is to disconnect the second drive, boot into
Debian and convert `/etc/fstab` to use UUID (a unique ID for each
partition), as explained on the <a href = "../tips/#uuid">tips and
tricks</a> page.

<h3><a id = "disk-power">I get strange errors from my USB disk</a></h3>

Some users have reported strange errors with their USB disk, such as data
corruption and disk errors displayed in `dmesg`.  In some cases, the disks
were simply broken or dying.  However, in some cases the problem was
related to lack of power.  There's only so much power on the USB port, so
you might have to use a separate power supply for your disk.

<h3><a id = "no-boot">My NSLU2 no longer boots</a></h3>

There can be many reasons why a NSLU2 no longer boots, ranging from a
broken disk, to a bad upgrade or configuration.  Unfortunately, it's often
impossible to say what the problem is without the use of a serial console.
The best solution is to connect a serial console to see what the problem is
but not everyone can do that.

Something you should try is to connect your USB drive to another PC and to
check the log files:

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

Connect the drive to your NSLU2, boot it, wait a few minutes, then turn it
off and connect the drive to your PC again and mount it.  Now look at the
file `/mnt/var/log/boot` which might tell you more.

One common cause for boot problems is related to filesystem checks and
running `fsck` over all partitions may help.  There are several reasons why
this might help:

<ul>

<li>The Linux ext3 filesystem has to be checked periodically.  Even though
Debian has been configured not to prompt the user during the filesystem
check, it might still do so in case of serious errors.  Without a serial
console, this prompt means that your NSLU2 will hang waiting for user
input.</li>

<li>Some users have reported that the NSLU2 doesn't have enough RAM to
perform a filesystem check on large disks (i.e. 200 GB or more).</li>

</ul>

Turn your NSLU2 off, connect the disk to another machine running Linux and
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

If this doesn't help, there's one more thing you can try: remove the RTC
battery and boot again.  There have been various reports that the clock on
the NSLU2 can get "stuck" and removing the battery helps.

If none of this helps, I'm afraid you probably have to connect a serial
console or perform a new installation.

<%= render "paypal", :desc => "Debian/NSLU2 donation" %>

