---
title: Specification of the Kurobox Pro
nav: Specs
description: Specs of the Kurobox Pro
keywords: [Buffalo, Revogear, Kurobox Pro, specs, specification]
---

<% content_for :right do %>
<img src = "../images/r_kuroboxpro_front.jpg" class="border" alt="Kurobox Pro from the front" width="148" height="231" />

<%= render "adsense-wideskyscaper-right" %>
<% end %>

<h1>Specs of the Kurobox Pro</h1>

This page lists the internals of the Kurobox Pro.

<table style="border-style: none" border="1" cellpadding="5">

<tr>
<th>Component</th>
<th>Comment</th>
</tr>

<tr>
<td>CPU</td>
<td>Marvell Orion 88F5182 A2, 400-500 MHz</td>
</tr>

<tr>
<td>RAM</td>
<td>128 MB</td>
</tr>

<tr>
<td>Flash ROM</td>
<td>256 KB NOR (boot loader), 256 MB NAND</td>
</tr>

<tr>
<td>Hard drive</td>
<td>1x 3.5" SATA, integrated in SoC</td>
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
<td>Ricoh RS5C372A/B</td>
</tr>

<tr>
<td>Fan</td>
<td>Yes, one</td>
</tr>

<tr>
<td>Boot loader</td>
<td>U-Boot</td>
</tr>

<tr>
<td>Other</td>
<td>1x PCI Express (PCIe) X1</td>
</tr>

<tr>
<td>Other</td>
<td>1x external SATA (but not eSATA)</td>
</tr>

<tr>
<td>Other</td>
<td>Expansion pin headers: UART, GPIO, I2C</td>
</tr>

</table>

Go back to my <a href = "..">Debian on Kurobox Pro</a> page.

<div class="bbf">
<%= render "adsense-banner-before-footer" %>
</div>

