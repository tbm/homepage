---
title: Recovery mode of the QNAP TS-409
nav: Recovery mode
description: System Recovery Mode of the QNAP TS-409
keywords: [Debian, QNAP, TS-409, recovery, emergency, rescue]
---

<% content_for :right do %>
<img src = "../images/r_ts409_front.jpg" class="border" alt="QNAP TS-409 from the front" width="148" height="147" />

<%= render "adsense-wideskyscaper-right" %>
<% end %>

<h1>Recovery mode of the QNAP TS-409</h1>

QNAP added a recovery mode to their devices that can be used when there is
a problem with your installation of Debian that renders your device
unbootable.  The system recovery mode allows you write a recovery image to
flash via the network using the TFTP protocol.  This pages describes how
you can verify whether your device includes the recovery mode, how to
upgrade your firmware to a version that includes the recovery mode, how to
create recovery images and finally how to use the recovery mode.

<h2><a id = "verify">Verifying whether your system has the recovery mode</a></h2>

The QNAP recovery mode is relatively new and is not included in QNAP
devices that were manufactured prior to 2009.  Even if you have a new QNAP
device, you should verify whether your firmware includes the recovery mode.
You can do this with the following command:

<div class="code">
<pre>
cksum /dev/mtdblock0
</pre>
</div>

Please compare the first value that is printed with those from the
following table to see whether your device has the recovery mode already:

<table style="border-style: none" border="1" cellpadding="5">

<tr>
<td>Checksum</td>
<td>Recovery mode</td>
<td>Build date</td>
</tr>

<tr>
<td>1009915998</td>
<td>no</td>
<td>Jul 26 2007 - 11:26:33</td>
</tr>

<tr>
<td>2829080541</td>
<td>no</td>
<td>Feb 19 2008 - 11:13:40</td>
</tr>

<tr>
<td>45443607</td>
<td>yes</td>
<td>Oct 24 2008 - 17:47:36</td>
</tr>

<tr>
<td>1135766646</td>
<td>yes</td>
<td>Nov 14 2008 - 17:06:53</td>
</tr>

</table>

If your device does not have the recovery mode, please read on to see how
you can upgrade your firmware.  If the value printed by `cksum` is not
listed in this table, please <a href = "/contact/">contact me</a>.

<h2><a id = "install">Installing the recovery mode</a></h2>

You can install the recovery mode according to two ways, depending on
whether you are <a href = "#install-initialized">running the full QNAP
firmware</a> or <a href = "#install-uninitialized">have an uninitialized
QNAP system</a>.

<h3><a id = "install-initialized">Fully Initialized QNAP System</a></h3>

QNAP provides a <a href =
"http://wiki.qnap.com/wiki/Emergency_Recovery_Mode">page about the recovery
mode</a> which tells you exactly how to install the recovery mode.  In
short, you have to install a QPKG provided by QNAP that will automatically
install the recovery mode.

<h3><a id = "install-uninitialized">Uninitialized QNAP System</a></h3>

You need a USB stick on which you can store some files.  Please put the USB
stick in your PC, download the zip file for your QNAP device from QNAP's <a
href = "http://wiki.qnap.com/wiki/Emergency_Recovery_Mode">recovery mode
page</a> (but ignore the installation instructions from that page).  Unzip
the file and copy the `.qpkg` file to the USB stick.  Now start your QNAP
device and connect the USB stick to it.  Login to your QNAP via telnet as
the `admin` user as described in the <a href = "../install">installation
guide</a> and go into the directory where the USB stick is mounted.

First of all, you should make a backup of your flash partitions using the
following commands:

<div class="code">
<pre>
cat /dev/mtdblock1 &gt; mtd1
cat /dev/mtdblock2 &gt; mtd2
cat /dev/mtdblock3 &gt; mtd3
</pre>
</div>

Now you can unpack the QPKG file provided by QNAP:

<div class="code">
<pre>
dd if=QNAP_SystemRecovery_1.0_TS-409.qpkg bs=526 skip=1 | tar xzv
</pre>
</div>

This will create two files: `qinstall.sh` and `QNAP_SystemRecovery.tgz`.
We are only interested in the latter, which you have to unpack with:

<div class="code">
<pre>
tar xzvf QNAP_SystemRecovery.tgz
</pre>
</div>

Now you can start the actual upgrade process.  There are two steps you have
to follow.  First of all, you have to update the Linux kernel.  Normally,
the Linux kernel is configured so it won't allow you to change `mtd0`, the
flash partition where the u-boot boot loader is stored.  The first step is
therefore to write a Linux kernel to flash that doesn't protect `mtd0`,
otherwise you couldn't upgrade u-boot to the new version that includes the
recovery mode.

Make sure the checksum of the kernel image matches that listed in the
`cksum` file:

<div class="code">
<pre>
cksum uImage
3523682680 2000808 uImage
cat uImage.cksum
3523682680 2000808 .../uImage
</pre>
</div>

If they match, go ahead and write the kernel to flash:

<div class="code">
<pre>
dd if=uImage of=/dev/mtdblock1
</pre>
</div>

You have to restart your machine now so the new kernel is loaded:

<div class="code">
<pre>
cd
umount /share/external/sdi
reboot
</pre>
</div>

Once your system has restarted, login as `admin` again and go to the
directory where your USB stick is mounted.  Then verify the checksum of the
u-boot binary:

<div class="code">
<pre>
cksum u-boot.bin
2049233834 469608 u-boot.bin
cat u-boot.bin.cksum
2049233834 469608 u-boot.bin
</pre>
</div>

If they match, write the new u-boot to flash using the following command.
Make sure that you don't interrupt this process and that your QNAP has a
good power source.  If the process of writing u-boot to flash is
interrupted, your QNAP device might no longer boot!

<div class="code">
<pre>
dd if=u-boot.bin of=/dev/mtdblock0
</pre>
</div>

You have successfully upgraded your firmware to a version that includes the
recovery mode.  You can now go ahead with the <a href =
"../install">installation of Debian</a>.

<h2><a id = "create">Creating recovery images</a></h2>

The QNAP recovery image contains a copy of `mtd1`, `mtd2` and `mtd3`, i.e.
the kernel partition, ramdisk partition and second ramdisk partition.

<h3><a id = "image-qnap">Making a recovery image of the QNAP backup</a></h3>

Before installing Debian, you should have made a backup of the QNAP
firmware and have several `mtdX` files.  You can now make a recovery image
out of the backup with this command:

<div class="code">
<pre>
cat mtd1 mtd2 mtd3 &gt; qnapimg.bin
</pre>
</div>

<h3><a id = "image-system">Making a recovery image from a running system</a></h3>

You can easily make a valid recovery image with the following command:

<div class="code">
<pre>
cat /dev/mtdblock1 /dev/mtdblock2 /dev/mtdblock3 &gt; qnapimg.bin
</pre>
</div>

It is recommended to create periodic recovery images of your flash,
so you have a recovery image in case something goes wrong.

<h3><a id = "image-di">Making a recovery image containing the Debian installer</a></h3>

If you want to make a QNAP recovery image containing the Debian installer,
you can follow these steps.  First of all, download the <a href =
"http://ftp.nl.debian.org/debian/dists/stable/main/installer-armel/current/images/orion5x/network-console/qnap/ts-409/initrd.gz">initrd</a>
and <a href =
"http://ftp.nl.debian.org/debian/dists/stable/main/installer-armel/current/images/orion5x/network-console/qnap/ts-409/kernel">kernel</a>
for the installer.  You now have to pad the kernel so it is the right size:

<div class="code">
<pre>
dd if=kernel of=kernel.pad ibs=2097152 conv=sync
</pre>
</div>

Finally, you can create a recovery image:

<div class="code">
<pre>
cat kernel.pad initrd.gz mtd3 &gt; qnapimg.bin
</pre>
</div>

Note that the `mtd3` file in this command refers to the backup you created
earlier (before the installation).

<h2><a id = "use">Using the recovery mode</a></h2>

In case your Debian system no longer boots after a system upgrade, you can
use the QNAP system recovery mode to restore a previous image, an image of
the Debian installer, or the QNAP firmware.

The recovery mode will request a recovery image by TFTP from a server on
your network.  The QNAP will use the IP address `192.168.0.10` and will
request a file called `qnapimg.bin` from the server with the address
`192.168.0.11`.  These addresses cannot be configured.

You can activate the recovery mode by pressing the reset button on the back
of your QNAP for about 10 seconds.  I suggest you press the reset button
and keep it pressed, and then turn on your QNAP device.  After about 10
seconds, you will hear two short beeps.  Your QNAP will now request a
recovery image via TFTP.  When it has obtained the recovery image and
written it to flash, your QNAP will make one long beep and restart.

More information about the recovery mode can be found on <a href =
"http://wiki.qnap.com/wiki/Emergency_Recovery_Mode">QNAP's System Recovery
Mode</a> page.

<%= render "paypal", :desc => "Debian/QNAP TS-409 donation" %>

<div class="bbf">
<%= render "adsense-banner-before-footer" %>
</div>

