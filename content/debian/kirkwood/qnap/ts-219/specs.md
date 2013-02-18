---
title: Specification of the QNAP TS-219, TS-219 and TS-219P
nav: Specs
description: Specs of the QNAP TS-210, TS-212, TS-219 and TS-219P
keywords: [Debian, QNAP, TS-210, TS-219, TS-210P, specs, specification]
---

<% content_for :right do %>
<img src = "../images/r_ts219p.jpg" class="border" alt="Open QNAP TS-219" width="148" height="188" />

<%= render "adsense-wideskyscaper-right" %>
<% end %>

<h1>Specs of the QNAP TS-210, TS-219 and TS-219P</h1>

This page lists the internals of the QNAP TS-210, QNAP TS-219 and the QNAP
TS-219P.  There is another page which shows the <a href =
"../status">status of support in Debian</a> for these components.

<h2>QNAP TS-210 and TS-219</h2>

<p>

<table style="border-style: none" border="1" cellpadding="5">

<tr>
<th>Component</th>
<th>Comment</th>
</tr>

<tr>
<td>CPU</td>
<td>Marvell Kirkwood 88F6281 A0, 800 MHz (TS-210) or 1.2 GHz (TS-219)</td>
</tr>

<tr>
<td>RAM</td>
<td>256 MB (TS-210) or 512 MB (TS-219) DDR II</td>
</tr>

<tr>
<td>Flash ROM</td>
<td>16 MB STMicroelectronics 25P28V6P SPI</td>
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
<td>3x USB 2.0, GL850G and integrated in SoC</td>
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

<h2>QNAP TS-219P and TS-219P+</h2>

<p>

<table style="border-style: none" border="1" cellpadding="5">

<tr>
<th>Component</th>
<th>Comment</th>
</tr>

<tr>
<td>CPU</td>
<td>Marvell Kirkwood 88F6281 A0, 1.2 GHz (TS-219P) or 88F6282 1.6 GHz (TS-219P+)</td>
</tr>

<tr>
<td>RAM</td>
<td>512 MB DDR II</td>
</tr>

<tr>
<td>Flash ROM</td>
<td>16 MB STMicroelectronics 25P28V6P SPI</td>
</tr>

<tr>
<td>Internal hard drive</td>
<td>2x 3.5" SATA, integrated in SoC</td>
</tr>

<tr>
<td>External hard drive</td>
<td>2x eSATA, JMB362</td>
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
<td>Yes, one; Y.S. Tech FD127025LB</td>
</tr>

<tr>
<td>Boot loader</td>
<td>U-Boot</td>
</tr>

</table>

<div class="bbf">
<%= render "adsense-banner-before-footer" %>
</div>

