---
title: Specification of the QNAP TS-409
nav: Specs
description: Specs of the QNAP TS-409
keywords: [Debian, QNAP, TS-409, specs, specification]
---

<% content_for :right do %>
<img src = "../images/r_ts409_front.jpg" class="border" alt="QNAP TS-409 from the front" width="148" height="147" />

<%= render "adsense-wideskyscaper-right" %>
<% end %>

<h1>Specs of the QNAP TS-409</h1>

This page lists the internals of the QNAP TS-409.  There is another page
which shows the <a href = "../status">status of support in Debian</a> for
these components.

<table style="border-style: none" border="1" cellpadding="5">

<tr style="background-color: #E0E0FF">
<td>Component</td>
<td>Comment</td>
</tr>

<tr>
<td>CPU</td>
<td>Marvell Orion 88F5281 D0, 500 MHz</td>
</tr>

<tr>
<td>RAM</td>
<td>256 MB DDR II (or 512 MB on TS-409 II and TS-409U)</td>
</tr>

<tr>
<td>Flash ROM</td>
<td>8 MB NOR</td>
</tr>

<tr>
<td>Hard drive</td>
<td>4x 3.5" SATA, Marvell 88SX7042</td>
</tr>

<tr>
<td>Ethernet</td>
<td>1x 10/100/1000 Mbit, integrated in SoC</td>
</tr>

<tr>
<td>USB</td>
<td>3x USB 2.0, GL852 and integrated in SoC</td>
</tr>

<tr>
<td>RTC</td>
<td>Seiko Instruments S-35390A</td>
</tr>

<tr>
<td>Fan</td>
<td>Yes</td>
</tr>

<tr>
<td>Boot loader</td>
<td>U-Boot</td>
</tr>

</table>

<div class="bbf">
<%= render "adsense-banner-before-footer" %>
</div>

