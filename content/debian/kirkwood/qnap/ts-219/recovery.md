---
title: Recovery mode of QNAP TS-21x/TS-22x
nav: Recovery mode
description: System Recovery Mode of QNAP TS-21x/TS-22x
keywords: [Debian, QNAP, HS-210, TS-210, TS-212, TS-219, TS-219P, TS-219P+, TS-220, TS-221, recovery, emergency, rescue]
---

<% content_for :right do %>
<img src = "../images/r_ts219p.jpg" class="border" alt="Open QNAP TS-219" width="148" height="188" />
<% end %>

<h1>Recovery mode of QNAP HS-210, TS-21x and TS-22x devices</h1>

QNAP HS-210, TS-21x and TS-22x devices have a recovery mode that can be used when there is a
problem with your installation of Debian that renders your device
unbootable.  The system recovery mode allows you write a recovery image to
flash via the network using the TFTP protocol.  This pages describes how
how to create recovery images and how to use the recovery mode.  As an
alternative to the instructions on this page, you can use a <a href =
"http://wiki.qnap.com/wiki/Firmware_Recovery">Live CD provided by QNAP</a>.

<h2><a id = "create">Creating recovery images</a></h2>

In order to create a recovery image for your QNAP TS-21x/TS-22x, you have to take
an exact copy of your flash memory.  That is, the recovery image consists
of the following parts of your flash in this order: `mtd0`, `mtd4`, `mtd5`,
`mtd1`, `mtd2`, `mtd3`.  You may wonder about this strange order but this
is the way in which the data is physically stored in the flash memory.
During recovery mode, `mtd0` (the boot loader), `mtd4` (the boot loader
configuration) and on some devices `mtd5` (device configuration) are
ignored and the other parts of flash are overwritten with the data from
your recovery image.  In order to make a valid QNAP recovery image, you
therefore have to put all `mtd` partitions into one file in the order
described above.

<h3><a id = "image-qnap">Making a recovery image of the QNAP backup</a></h3>

Before installing Debian, you should have made a backup of the QNAP
firmware and have several `mtdX` files.  You can now make a recovery image
out of the backup with this command:

<div class="code">
<pre>
cat mtd0 mtd4 mtd5 mtd1 mtd2 mtd3 &gt; F_TS-219_qnap
</pre>
</div>

<h3><a id = "image-system">Making a recovery image from a running system</a></h3>

You can easily make a valid recovery image with the following command:

<div class="code">
<pre>
cat /dev/mtdblock0 /dev/mtdblock4 /dev/mtdblock5 /dev/mtdblock1 /dev/mtdblock2 /dev/mtdblock3 &gt; F_TS-219_debian
</pre>
</div>

It is recommended to create periodic recovery images of your flash, so you
have a recovery image in case something goes wrong.

<h3><a id = "image-di">Making a recovery image containing the Debian installer</a></h3>

If you want to make a QNAP recovery image containing the Debian installer,
you can follow these steps.  First of all, download the <a href =
"http://ftp.uk.debian.org/debian/dists/stable/main/installer-armel/current/images/kirkwood/network-console/qnap/ts-219/initrd.gz">initrd</a>
and <a href =
"http://ftp.uk.debian.org/debian/dists/stable/main/installer-armel/current/images/kirkwood/network-console/qnap/ts-219/kernel">kernel</a>
for the installer.  You now have to pad the kernel so it is the right size:

<div class="code">
<pre>
dd if=kernel of=kernel.pad ibs=2097152 conv=sync
</pre>
</div>

Finally, you can create a recovery image:

<div class="code">
<pre>
cat mtd0 mtd4 mtd5 kernel.pad initrd.gz mtd3 &gt; F_TS-219_di
</pre>
</div>

Note that the `mtdX` files in this command refer to the backup you created
earlier (before the installation).

<h2><a id = "use">Using the recovery mode</a></h2>

In case your Debian system no longer boots after a system upgrade, you can
use the QNAP system recovery mode to restore a previous image, an image of
the Debian installer, or the QNAP firmware.

The recovery mode will first request an IP address via DHCP and then
request a recovery image by TFTP from a server on your network.  You have
to configure your DHCP server so it will request the right file from the
right machine.  In particular, you have to create an entry for your QNAP
that specifies `filename` and `next-server`.  The latter refers to the IP
address of your TFTP server (likely the same as your DHCP server).  The
`filename` of the recovery image has to start with a specific string
depending on your machine (otherwise the machine won't load the image!).
You also have to install a TFTP server (such as `tftpd-hpa`) to serve
the file.

You can check the following table to find out which string to use:

<table>

<tr>
<th>Device</th>
<th>String</th>
</tr>

<tr>
<td>HS-210</td>
<td>`F_HS-210`</td>
</tr>

<tr>
<td>TS-210</td>
<td>`F_TS-210`</td>
</tr>

<tr>
<td>TS-212</td>
<td>`F_TS-212`</td>
</tr>

<tr>
<td>TS-219</td>
<td>`F_TS-219`</td>
</tr>

<tr>
<td>TS-219P</td>
<td>`F_TS-219` or (for older revisions) `F_TS-219PE`</td>
</tr>

<tr>
<td>TS-219P+</td>
<td>`F_TS-219P+`</td>
</tr>

<tr>
<td>TS-219P II</td>
<td>`F_TS-219P2+`</td>
</tr>

<tr>
<td>TS-220</td>
<td>`F_TS-220`</td>
</tr>

<tr>
<td>TS-221</td>
<td>`F_TS-221`</td>
</tr>

</table>

One some devices (but not on the TS-219P+), you can check the backup you
made of the flash to find out what the right string is for your machine:

<div class="code">
<pre>
strings mtd4 | grep bootp_vendor_class
</pre>
</div>

Please note that by default the MAC address used by your QNAP device in the
recovery mode is different to the one used while running the QNAP firmware.
When you install Debian, a script is run to ensure that the same MAC
address is used everywhere.  Therefore, depending on whether you ran that
script, the MAC address will either be that from the QNAP firmware (the one
printed on your device; it probably starts with `00:08:9B`) or an address
starting with `00:50:43`.  You can run the recovery mode and then look for
`DHCPDISCOVER` messages in `/var/log/syslog` to find out the correct MAC
address.

Once you have the right MAC address, you can configure your DHCP server.  I
used the following entry in `/etc/dhcp/dhcpd.conf`:

<div class="code">
<pre>
host ts219 {
    hardware ethernet 00:50:43:3c:3b:5d;
    filename "F_TS-219_debian";
    fixed-address 192.168.1.71;
    next-server 192.168.1.2;
}
</pre>
</div>

Reload your DHCP server so the configuration change will take effect.

You can activate the recovery mode by pressing the reset button on the back
of your QNAP for about 10 seconds.  I suggest you press the reset button
and keep it pressed, and then turn on your QNAP device.  After about 10
seconds, you will hear two short beeps.  Your QNAP will now request a
recovery image via TFTP.  When it has obtained the recovery image and
written it to flash (which takes about 3.5 minutes), your QNAP will make
two short beeps again and restart.

<%= render "paypal", :desc => "Debian/QNAP TS-21x/TS-22x donation" %>

