---
title: Status of QNAP TS-209 support
nav: Status
description: Status of QNAP TS-209 support in Debian
keywords: [Debian, QNAP, TS-209, support, status]
---

<div class="right">
<img src = "../images/r_ts209_front.jpg" class="border" alt="QNAP TS-209 from the front" width="148" height="97" />
</div>

<h1>Status of QNAP TS-209 support</h1>

The QNAP TS-209 is based on a Marvell Orion System on a Chip.  Marvell has
done a lot of work to get support for the Orion platform into the mainline
kernel.  However, some features of the Orion platform are not as well
supported as in the original Marvell LSP (Linux Support Package) used by
QNAP.  Please take this into account before deciding whether you want to
install Debian, especially if you have specific requirements (e.g. related
to performance).

The table below shows how well different components of the QNAP TS-209 are
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
<th>TS-209 kernel</th>
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
<td>Supported in the kernel by the `rtc-s35390a` module since 2.6.25</td>
</tr>

<tr class="table-success">
<th>LEDs</th>
<td>Supported in qcontrol</td>
</tr>

<tr class="table-success">
<th>Fan</th>
<td>Supported in qcontrol; you can <a href="../tips/#qcontrol-upgrade">upgrade
qcontrol</a> to get automatic temperature regulation.</td>
</tr>

<tr class="table-success">
<th>Beeper</th>
<td>Supported in qcontrol</td>
</tr>

<tr class="table-success">
<th>XOR engine</th>
<td>Supported in the Debian kernel since 2.6.26 and in the mainline
kernel since 2.6.27.  Support is mainly helpful for RAID5 at the
moment, so it's not quite useful on the TS-209</td>
</tr>

<tr class="table-warning">
<th>Crypto engine</th>
<td>Basic support</td>
</tr>
</tbody>

</table>

