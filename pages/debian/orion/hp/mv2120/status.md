---
title: Status of HP mv2120 support
nav: Status
description: Status of HP mv2120 support in Debian
keywords: [Debian, HP, mv2120, support, status]
---

<div class="right">
<img src = "../images/r_mv2120_front.jpg" class="border" alt="HP mv2120 from the front" width="148" height="212" />
</div>

The HP mv2120 is based on a Marvell Orion System on a Chip.  Marvell has
done a lot of work to get support for the Orion platform into the mainline
kernel.  However, some features of the Orion platform are not as well
supported as in the original Marvell LSP (Linux Support Package) used by
HP.  Please take this into account before deciding whether you want to
install Debian, especially if you have specific requirements (e.g. related
to performance).

The table below shows how well different components of the HP mv2120 are
supported by Debian:

<table class="table table-hover">

<thead>
<tr>
<th>Component</th>
<th>Comment</th>
</tr>
</thead>

<tbody>
<tr class="table-success">
<th>Debian</th>
<td>Debian installer works well</td>
</tr>

<tr class="table-success">
<th>CPU</th>
<td>Supported in mainline and Debian kernel since 2.6.25</td>
</tr>

<tr class="table-success">
<th>mv2120 kernel</th>
<td>Supported in the Debian kernel since 2.6.25 and in the mainline
kernel since 2.6.27</td>
</tr>

<tr class="table-success">
<th>SATA</th>
<td>Supported in the kernel by the `sata_mv` module</td>
</tr>

<tr class="table-success">
<th>Ethernet</th>
<td>Supported in the kernel by the `mv643xx` module</td>
</tr>

<tr class="table-success">
<th>USB</th>
<td>Supported in the kernel since 2.6.25</td>
</tr>

<tr class="table-success">
<th>RTC</th>
<td>Supported in the kernel by the `rtc-pcf8563` module</td>
</tr>

<tr class="table-success">
<th>LEDs</th>
<td>Supported in the Debian kernel as of 2.6.26 and Debian will use the
LEDs to signal the status of the boot process.</td>
</tr>

<tr class="table-success">
<th>Fan</th>
<td>It seems the mv2120 has no temperature sensor or way to regulate
the fan.</td>
</tr>

<tr class="table-success">
<th>XOR engine</th>
<td>Supported in the Debian kernel since 2.6.26 and in the mainline
kernel since 2.6.27.  Support is mainly helpful for RAID5 at the
moment, so it's not quite useful on the mv2120</td>
</tr>

<tr class="table-warning">
<th>Crypto engine</th>
<td>Basic support</td>
</tr>
</tbody>

</table>

