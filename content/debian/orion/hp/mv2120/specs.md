---
title: Specification of the HP mv2120
nav: Specs
description: Specs of the HP mv2120
keywords: [Debian, HP, mv2120, specs, specification]
---

<% content_for :right do %>
<img src = "../images/r_mv2120_front.jpg" class="border" alt="HP mv2120 from the front" width="148" height="212" />

<%= render "adsense-wideskyscaper-right" %>
<% end %>

<h1>Specs of the HP mv2120</h1>

This page lists the internals of the HP mv2120.  There is another page
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
<td>128 MB</td>
</tr>

<tr>
<td>Flash ROM</td>
<td>512 KB NOR</td>
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
<td>2x USB 2.0, integrated in SoC</td>
</tr>

<tr>
<td>RTC</td>
<td>PCF8563</td>
</tr>

<tr>
<td>Fan</td>
<td>Yes, one</td>
</tr>

<tr>
<td>Boot loader</td>
<td>U-Boot</td>
</tr>

</table>

Please note that the Media Vault Pro (mv5000 and mv5100) series is
identical to the hardware of the HP Media Vault mv2120.  They only differ
in their disk configuration.  The mv2120 (GX662AA) and mv5100 (GX666AA)
have a single 500 GB drive, the mv5140 (GX667AA) has two 500 GB drives and
the mv5150 (GX668AA) has a pair of 750 GB drives.

<div class="bbf">
<%= render "adsense-banner-before-footer" %>
</div>

