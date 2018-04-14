---
title: Status of QNAP TS-21x/TS-22x support
nav: Status
description: Status of QNAP TS-21x/TS-22x support in Debian
keywords: [Debian, QNAP, TS-210, TS-212, TS-219, TS-219P, TS-220, TS-221, support, status]
---

<div class="right">
<img src = "../images/r_ts219p.jpg" class="border" alt="Open QNAP TS-219" width="148" height="188" />
</div>

<h1>Status of QNAP TS-21x/TS-22x support</h1>

QNAP TS-21x/TS-22x devices are based on a Marvell Kirkwood System on a Chip.
Marvell has done a lot of work to get support for the Kirkwood platform
into the mainline kernel.  However, some features of the Kirkwood platform
are not as well supported in the mainline kernel (which we use in Debian)
as in the original Marvell LSP (Linux Support Package) used by QNAP.
Please take this into account before deciding whether you want to install
Debian, especially if you have specific requirements (e.g. related to
performance).

The table below shows how well different components of the QNAP
TS-21x/TS-22x are supported by Debian:

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
<td>Debian and the Debian installer work well</td>
</tr>

<tr class="table-success">
<th>CPU</th>
<td>Supported in the kernel by the `kirkwood` platform</td>
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
<td>Supported</td>
</tr>

<tr class="table-success">
<th>RTC</th>
<td>Supported in the kernel by the `rtc-s35390a` module</td>
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
<td>Supported. Support is mainly helpful for RAID5 at the
moment, so it's not quite useful on the TS-21x</td>
</tr>

<tr class="table-warning">
<th>Crypto engine</th>
<td>Basic support</td>
</tr>

<tr class="table-success">
<th>Wake-on-LAN (WOL)</th>
<td>Supported in qcontrol.</td>
</tr>

<tr class="table-success">
<th>Scheduled power</th>
<td>Supported; see <a href = "../tips/#wakealarm">instructions</a></td>
</tr>
</tbody>

</table>

