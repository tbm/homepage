---
title: Obtaining original QNAP firmware
nav: Obtaining original QNAP firmware
description: Obtaining the original QNAP firmware from Live CD
keywords: [Debian, QNAP, TS-110, TS-112, TS-112P, TS-119, TS-120, TS-121, original firmware]
---

If you lost your backup of the QNAP firmware and want to restore the QNAP
OS, you can extract the files from the Live CD that QNAP provides.

First, download the <a href =
"http://wiki.qnap.com/wiki/Firmware_Recovery">Live CD provided by QNAP</a>.
You should have a file called `live-cd-20130730.iso` or
`live-cd-20140212.iso` (depending on your QNAP model).

You have to mount this ISO image.  Within the ISO image, there is a Squash
image located at `casper/filesystem.squashfs`.  Loop mount that image and
you'll find images of the QNAP firmware under `tftpboot`.  Take the image
for your QNAP device.

<div class="code">
<pre>
sudo mkdir /media/qnap-cd /media/qnap-live
sudo mount -o loop,ro ~/Downloads/live-cd-20130730.iso /media/qnap-cd
sudo mount -o loop,ro /media/qnap-cd/casper/filesystem.squashfs /media/qnap-live
ls -1 /media/qnap-live/tftpboot | head -n 3
cp /media/qnap-live/F_TS-<span class="input">YOURMODEL</span>_20130611-1.1.10.img ~
sudo umount /media/qnap-live
sudo umount /media/qnap-cd
</pre>
</div>

Now you can extract the Linux kernel (`mtd1`) and ramdisk (`mtd2`) from the
QNAP image.  You can do this with these commands:

<div class="code">
<pre>
dd if=F_TS-*_20130613-1.1.10.img of=mtd1 bs=1M skip=2 count=2
dd if=F_TS-*_20130613-1.1.10.img of=mtd2 bs=1M skip=4 count=9
</pre>
</div>

Now you have `mtd1` and `mtd2` and can continue with the <a href =
"../deinstall">installation of QNAP OS</a>.

<h2>Limitations</h2>

Historically, Debian only modified `mtd1` and `mtd2`.  We never touched any
of the other MTD partitions.

However, some people use modified MTD partition layouts in order to run
newer versions of Debian.  If you use that, you may need to extract other
files from the QNAP image and restore them. (Probably `mtd3`.)

This is how the QNAP image is arranged:

<table class="table table-hover">

<thead>
<tr>
<th>Partition</th>
<th>Function</th>
<th>Size</th>
<th>Size (bytes)</th>
</tr>
</thead>

<tbody>
<tr>
<th>mtd0</th>
<td>U-Boot</td>
<td>512 KB</td>
<td>524288</td>
</tr>

<tr>
<th>mtd4</th>
<td>U-Boot Config</td>
<td>256 KB</td>
<td>262144</td>
</tr>

<tr>
<th>mtd5</th>
<td>QNAP Config (ext2)</td>
<td>1 MB + 256 KB</td>
<td>1310720</td>
</tr>

<tr>
<th>mtd1</th>
<td>Linux kernel</td>
<td>2.0 MB</td>
<td>2097152</td>
</tr>

<tr>
<th>mtd2</th>
<td>ramdisk</td>
<td>9.0 MB</td>
<td>9437184</td>
</tr>

<tr>
<th>mtd3</th>
<td>ramdisk 2</td>
<td>3.0 MB</td>
<td>3145728</td>
</tr>

</table>

