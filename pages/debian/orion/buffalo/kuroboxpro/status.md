---
title: Status of Kurobox Pro support
nav: Status
description: Status of Kurobox Pro support in Debian
keywords: [Buffalo, Revogear, Kurobox Pro, support, status]
---

<div class="right">
<img src = "../images/r_kuroboxpro_front.jpg" class="border" alt="Kurobox Pro from the front" width="148" height="231" />
</div>

The Kurobox Pro is based on a Marvell Orion System on a Chip.  Marvell has
done a lot of work to get support for the Orion platform into the mainline
kernel.  However, some features of the Orion platform are not as well
supported as in the original Marvell LSP (Linux Support Package) used by
Buffalo.  Please take this into account before deciding whether you want to
install Debian, especially if you have specific requirements (e.g. related
to performance).

The table below shows how well different components of the Kurobox Pro are
supported by Debian:

<table class="table table-hover">

<thead>
<tr>
<th>Component</th>
<th>Comment</th>
</tr>
<thead>

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
<th>Kurobox Pro kernel</th>
<td>Supported in mainline and Debian kernel since 2.6.25</td>
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
<td>Supported in the kernel by the `rtc-rs5c372` module</td>
</tr>

<tr class="table-success">
<th>LEDs</th>
<td>Supported by micro-evtd</td>
</tr>

<tr class="table-success">
<th>Fan</th>
<td>Supported by micro-evtd.</td>
</tr>

<tr class="table-success">
<th>Beeper</th>
<td>Supported by micro-evtd.</td>
</tr>

<tr class="table-success">
<th>XOR engine</th>
<td>Supported in the Debian kernel since 2.6.26 and in the mainline
kernel since 2.6.27.  Support is mainly helpful for RAID5 at the
moment, so it's not quite useful on the Kurobox Pro.</td>
</tr>

<tr class="table-warning">
<th>Crypto engine</th>
<td>Basic support</td>
</tr>
</tbody>

</table>

