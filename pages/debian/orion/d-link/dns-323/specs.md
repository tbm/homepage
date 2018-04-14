---
title: Specification of the D-Link DNS-323
nav: Specs
description: Specs of the D-Link DNS-323
keywords: [Debian, D-Link, DNS-323, Conceptronic, CH3SNAS, specs, specification]
---

<div class="right">
<img src = "../images/r_ch3snas_front.jpg" class="border" alt="Conceptronic CH3SNAS from the front" width="148" height="146" />
</div>

<h1>Specs of the D-Link DNS-323</h1>

This page lists the internals of the D-Link DNS-323.  There is another page
which shows the <a href = "../status/">status of support in Debian</a> for
these components.

There are currently two revisions of the D-Link DNS-323, revision A1 and
B1.  Revision A1 uses a Marvell 88F5181 CPU along with a separate SATA
chip.  Revision B1, on the other hand, uses a Marvell 88F5182 CPU which
integrates SATA into the SoC itself.  The DNS-323 revision B1 is also sold
by Conceptronic as the CH3SNAS.

<table class="table table-hover">

<thead>
<tr>
<th>Component</th>
<th>Comment</th>
</tr>
</thead>

<tbody>
<tr>
<th>CPU</th>
<td>Marvell Orion 88F5181 (revision A1) or 88F5182 (revision B1), 500 MHz</td>
</tr>

<tr>
<th>RAM</th>
<td>64 MB</td>
</tr>

<tr>
<th>Flash ROM</th>
<td>8 MB NOR</td>
</tr>

<tr>
<th>Hard drive</th>
<td>2x 3.5" SATA, Marvell 88X7042 (revision A1) or integrated in SoC
(revision B1)</td>
</tr>

<tr>
<th>Ethernet</th>
<td>1x 10/100/1000 Mbit, integrated in SoC</td>
</tr>

<tr>
<th>USB</th>
<td>1x USB 2.0, integrated in SoC</td>
</tr>

<tr>
<th>RTC</th>
<td>ST M41T80</td>
</tr>

<tr>
<th>Fan</th>
<td>One, controlled by GMT G760Af</td>
</tr>

<tr>
<th>Temperature sensor</th>
<td>GMT G751-2f</td>
</tr>

<tr>
<th>Boot loader</th>
<td>U-Boot</td>
</tr>
</tbody>

</table>

