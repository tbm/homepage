---
title: Specification of the QNAP TS-119 and TS-119
nav: Specs
description: Specs of the QNAP TS-110 and TS-119
keywords: [Debian, QNAP, TS-110, TS-112, TS-119, specs, specification]
---

<% content_for :right do %>
<img src = "../images/r_qnap_ts110.jpg" class="border" alt="QNAP TS-110 from the front" width="148" height="206" />

<%= render "adsense-wideskyscaper-right" %>
<% end %>

<h1>Specs of the QNAP TS-110 and TS-119</h1>

This page lists the internals of the QNAP TS-110, TS-119, TS-119P+.  There
is another page which shows the <a href = "../status">status of support in
Debian</a> for these components.

<table>

<tr>
<th>Component</th>
<th>Comment</th>
</tr>

<tr>
<td>CPU</td>
<td>Marvell Kirkwood 88F6281 800 MHz (TS-110), 88F6281 1.2 GHz (TS-119) or 88F6282 1.6 GHz (TS-119P+)
</td>
</tr>

<tr>
<td>RAM</td>
<td>256 MB (TS-110) or 512 MB (TS-119 and TS-119P+) DDR II</td>
</tr>

<tr>
<td>Flash ROM</td>
<td>16 MB STMicroelectronics 25P28V6P SPI</td>
</tr>

<tr>
<td>Internal hard drive</td>
<td>1x 3.5" SATA, integrated in SoC</td>
</tr>

<tr>
<td>External hard drive</td>
<td>1x eSATA</td>
</tr>

<tr>
<td>Ethernet</td>
<td>1x 10/100/1000 Mbit, integrated in SoC</td>
</tr>

<tr>
<td>USB</td>
<td>3x USB 2.0, GL850G and integrated in SoC</td>
</tr>

<tr>
<td>RTC</td>
<td>Seiko Instruments S-35390A</td>
</tr>

<tr>
<td>Fan</td>
<td>Yes (TS-110 and TS-119P+); No (TS-119)</td>
</tr>

<tr>
<td>Boot loader</td>
<td>U-Boot</td>
</tr>

</table>

<div class="bbf">
<%= render "adsense-banner-before-footer" %>
</div>

