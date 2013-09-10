---
title: Tips and tricks about Debian on Linksys NSLU2
nav: Tips
description: Tips and tricks about Debian on Linksys NSLU2
keywords: [NSLU2, Linksys NSLU2, Debian, tips, tricks]
---

<% content_for :right do %>
<img src = "../images/r_nslu2_front.jpg" class="border" alt="A NSLU2 from the front" width="148" height="218" />

<%= render "adsense-wideskyscaper-right" %>
<% end %>

<h1>Tips and tricks for Debian on the Linksys NSLU2</h1>

<h3><a id = "led">Controlling the LEDs and beeper</a></h3>

You can use the tool `leds` to control the LEDs and beeper.  Typing `leds`
without any arguments will show a help screen.

To control the beeper, you can also install the `beep` package and then
run:

<div class="code">
<pre>
beep -e /dev/input/event0
</pre>
</div>

beep can do a lot of things.  For example, the following command will
result in three beeps:

<div class="code">
<pre>
beep -e /dev/input/event0 -f 220 -l 500 -d 500 -r 3
</pre>
</div>

<h3><a id = "halt">Use power button to shut down system</a></h3>

By default, Debian will reboot the NSLU2 when you press the power button.
If you want your NSLU2 to shut down when you press the button, you have to
edit `/etc/inittab`.  Look for a line like this:

<div class="code">
<pre>
ca:12345:ctrlaltdel:/sbin/shutdown -t1 -a -r now
</pre>
</div>

and replace `-r now` with `-h now`.  Make sure to run the following command
to reload the file:

<div class="code">
<pre>
telinit q
</pre>
</div>

<h3><a id = "upgrade">Upgrading from Debian 6.0 (squeeze) to 7 (wheezy)</a></h3>

Here are some notes regarding upgrades from Debian 6.0 to 7:

<ul>

<li>Make sure to read the release notes for Debian 7.  In particular,
follow the <a href =
"http://www.debian.org/releases/stable/armel/release-notes/ch-upgrading.en.html">chapter
on upgrades from Debian 6.0</a> which explains the upgrade process in great
detail.</li>

<li>Make sure to remove the package `apt-xapian-index` from your system
before the upgrade.  This package requires substantially more RAM than the
NSLU2 has and will cause your upgrade to take 24 hours or more!</li>

</ul>

<h3><a id = "uuid">Using UUIDs to reference disks</a></h3>

Debian 5.0 (lenny) uses names like `/dev/sda1` to refer to your disk but
there is no guarantee for device ordering with USB devices.  This means
that when you connect a second drive, your `sda` device might (or might
not) become `sdb`, causing Debian to fail to boot because it's trying to
access the wrong drive.

The solution for this problem is to disconnect the second drive, boot into
Debian and convert `/etc/fstab` to use UUID (a unique ID for each
partition) or LABEL (a name for each partition) instead of device names.
To use UUID, do the following to find out the UUID for each partition
(we'll use `sda1` in the example):

<div class="code">
<pre>
cd /dev/disk/by-uuid
ls -l | grep sda1
[...] 683dbecd-1669-4210-bf29-fde6187261ba -&gt; ../../sda1
</pre>
</div>

Now edit `/etc/fstab` and replace the entry for sda1 with the UUID:

<div class="code">
<pre>
UUID=683dbecd-1669-4210-bf29-fde6187261ba /boot ext2 defaults 0 2
</pre>
</div>

You have to do the same for all partitions listed in `/etc/fstab`.
Finally, make a backup of your flash and then generate the initramfs.  This
is necessary because the name of the root device is stored in the
initramfs.

<div class="code">
<pre>
cat /dev/mtdblock* &gt; nslu2-backup
update-initramfs -u
</pre>
</div>

Make sure you do this with only one disk connected.  When Debian boots
successfully with one disk using UUID, you can go ahead and add the second
drive.

By the way, when upgrading from Debian 5.0 to 6.0, the upgrade process will
automatically convert your `/etc/fstab` to UUIDs.  However, the tar ball of
Debian provided here still use `/dev/sda1`-style names.

<div class="bbf">
<%= render "adsense-banner-before-footer" %>
</div>

