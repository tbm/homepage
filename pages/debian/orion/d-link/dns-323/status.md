---
title: Status of D-Link DNS-323 support
nav: Status
description: Status of D-Link DNS-323 support in Debian
keywords: [Debian, D-Link, DNS-323, Conceptronic, CH3SNAS, support, status]
---

<div class="right">
<img src = "../images/r_ch3snas_front.jpg" class="border" alt="Conceptronic CH3SNAS from the front" width="148" height="146" />
</div>

The D-Link DNS-323 is based on a Marvell Orion System on a Chip.  Marvell
has done a lot of work to get support for the Orion platform into the
mainline kernel.  However, some features of the Orion platform are not as
well supported as in the original Marvell LSP (Linux Support Package) used
by D-Link.  Please take this into account before deciding whether you want
to install Debian, especially if you have specific requirements (e.g.
related to performance).

The table below shows how well different components of the D-Link DNS-323
are supported by Debian 8 (jessie).  The device is no longer supported as
of Debian 9 (stretch).

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
<th>DNS-323 kernel</th>
<td>Supported in mainline and Debian kernel since 2.6.25 (revision A1).
The revision B2 is supported in the Debian kernel since 2.6.26 and in
the mainline kernel since 2.6.29</td>
</tr>

<tr class="table-success">
<th>SATA</th>
<td>Supported in the kernel by the `sata_mv` module.</td>
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
<td>Supported in the kernel by the `rtc-m41t80` module.</td>
</tr>

<tr class="table-success">
<th>LEDs</th>
<td>Supported in the kernel</td>
</tr>

<tr class="table-success">
<th>Fan</th>
<td>Supported.</td>
</tr>

<tr class="table-success">
<th>Temperature sensor</th>
<td>Supported.</td>
</tr>

<tr class="table-warning">
<th>Crypto engine</th>
<td>Basic support</td>
</tr>
</tbody>

</table>

