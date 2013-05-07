---
title: Specification of the QNAP TS-209
nav: Specs
description: Specs of the QNAP TS-209
keywords: [Debian, QNAP, TS-209, specs, specification]
---

<% content_for :right do %>
<img src = "../images/r_ts209_front.jpg" class="border" alt="QNAP TS-209 from the front" width="148" height="97" />

<%= render "adsense-wideskyscaper-right" %>
<% end %>

<h1>Specs of the QNAP TS-209</h1>

This page lists the internals of the QNAP TS-209.  There is another page
which shows the <a href = "../status/">status of support in Debian</a> for
these components.

<table>

<tr>
<th>Component</th>
<th>Comment</th>
</tr>

<tr>
<td>CPU</td>
<td>Marvell Orion 88F5182 A2, 500 MHz</td>
</tr>

<tr>
<td>RAM</td>
<td>128 MB DDR II (or 256 MB on II models)</td>
</tr>

<tr>
<td>Flash ROM</td>
<td>8 MB NOR</td>
</tr>

<tr>
<td>Hard drive</td>
<td>2x 3.5" SATA, integrated in SoC</td>
</tr>

<tr>
<td>Ethernet</td>
<td>1x 10/100/1000 Mbit, integrated in SoC</td>
</tr>

<tr>
<td>USB</td>
<td>3x USB 2.0, integrated in SoC</td>
</tr>

<tr>
<td>RTC</td>
<td>Seiko Instruments S-35390A</td>
</tr>

<tr>
<td>Fan</td>
<td>Yes, one; Bi-Sonic SP702012L</td>
</tr>

<tr>
<td>Boot loader</td>
<td>U-Boot</td>
</tr>

</table>

<div class="bbf">
<%= render "adsense-banner-before-footer" %>
</div>

