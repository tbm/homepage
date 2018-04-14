---
title: Specification of the HP mv2120
nav: Specs
description: Specs of the HP mv2120
keywords: [Debian, HP, mv2120, specs, specification]
---

<div class="right">
<img src = "../images/r_mv2120_front.jpg" class="border" alt="HP mv2120 from the front" width="148" height="212" />
</div>

<h1>Specs of the HP mv2120</h1>

This page lists the internals of the HP mv2120.  There is another page
which shows the <a href = "../status/">status of support in Debian</a> for
these components.

<table class="table table-hover">

<thead>
<tr>
<th>Component</th>
<th>Comment</th>
</tr>
<thead>

<tbody>
<tr>
<th>CPU</th>
<td>Marvell Orion 88F5182 A2, 500 MHz</td>
</tr>

<tr>
<th>RAM</th>
<td>128 MB</td>
</tr>

<tr>
<th>Flash ROM</th>
<td>512 KB NOR</td>
</tr>

<tr>
<th>Hard drive</th>
<td>2x 3.5" SATA, integrated in SoC</td>
</tr>

<tr>
<th>Ethernet</th>
<td>1x 10/100/1000 Mbit, integrated in SoC</td>
</tr>

<tr>
<th>USB</th>
<td>2x USB 2.0, integrated in SoC</td>
</tr>

<tr>
<th>RTC</th>
<td>PCF8563</td>
</tr>

<tr>
<th>Fan</th>
<td>Yes, one</td>
</tr>

<tr>
<th>Boot loader</th>
<td>U-Boot</td>
</tr>
</tbody>

</table>

Please note that the Media Vault Pro (mv5000 and mv5100) series is
identical to the hardware of the HP Media Vault mv2120.  They only differ
in their disk configuration.  The mv2120 (GX662AA) and mv5100 (GX666AA)
have a single 500 GB drive, the mv5140 (GX667AA) has two 500 GB drives and
the mv5150 (GX668AA) has a pair of 750 GB drives.

