---
title: Status of Thecus N2100 support
nav: Status
description: Status of Thecus N2100 support
keywords: [Debian, Thecus, N2100, support, status]
---

<% content_for :right do %>
<img src = "../images/r_n2100_debian.jpg" class="border" alt="Thecus N2100" width="133" height="148" />

<%= render "adsense-wideskyscaper-right" %>
<% end %>

<h1>Status of Thecus N2100 support</h1>

The table below shows how well different components of the Thecus N2100 are
supported by Debian 6.0 (squeeze):

<table style="border-style: none" border="1" cellpadding="5">

<tr>
<th>Component</th>
<th>Comment</th>
</tr>

<tr>
<td style="color: white; background-color: #00AA00">Debian</td>
<td>Debian installer works well.</td>
</tr>

<tr>
<td style="color: white; background-color: #00AA00">CPU</td>
<td>Supported in mainline and Debian kernel.</td>
</tr>

<tr>
<td style="color: black; background-color: #FFFF00">SATA</td>
<td>Supported in the kernel by the `sata_sil` module.  However,
the hard drive speed is slow.</td>
</tr>

<tr>
<td style="color: white; background-color: #00AA00">Ethernet</td>
<td>Supported in the kernel by the `r8169` module.</td>
</tr>

<tr>
<td style="color: white; background-color: #00AA00">USB</td>
<td>Supported in the kernel.</td>
</tr>

<tr>
<td style="color: white; background-color: #00AA00">RTC</td>
<td>Supported in the kernel by the `rtc-rs5c372` module.</td>
</tr>

<tr>
<td style="color: white; background-color: #00AA00">LEDs</td>
<td>Supported in the kernel.</td>
</tr>

<tr>
<td style="color: black; background-color: #FFFF00">Fan</td>
<td>Supported in in the kernel, but there is no automatic regulation
of the fan based on the current temperature.</td>
</tr>

<tr>
<td style="color: white; background-color: #00AA00">Beeper</td>
<td>Supported in the kernel.</td>
</tr>

</table>

<div class="bbf">
<%= render "adsense-banner-before-footer" %>
</div>

