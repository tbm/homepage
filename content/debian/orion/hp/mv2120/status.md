---
title: Status of HP mv2120 support
nav: Status
description: Status of HP mv2120 support in Debian
keywords: [Debian, HP, mv2120, support, status]
---

<% content_for :right do %>
<img src = "../images/r_mv2120_front.jpg" class="border" alt="HP mv2120 from the front" width="148" height="212" />

<%= render "adsense-wideskyscaper-right" %>
<% end %>

<h1>Status of HP mv2120 support</h1>

The HP mv2120 is based on a Marvell Orion System on a Chip.  Marvell has
done a lot of work in the last few months to get support for the Orion
platform into the mainline kernel and they continue to work on getting this
platform fully supported.  However, since this is an ongoing effort, some
features of the Orion platform are currently not as well supported as in
the original Marvell LSP (Linux Support Package) used by HP.  Please take
this into account before deciding whether you want to install Debian,
especially if you have specific requirements (e.g. related to performance).

The table below shows how well different components of the HP mv2120 are
supported by Debian:

<table>

<tr>
<th>Component</th>
<th>Comment</th>
</tr>

<tr>
<td style="color: white; background-color: #00AA00">Debian</td>
<td>Debian installer works well</td>
</tr>

<tr>
<td style="color: white; background-color: #00AA00">CPU</td>
<td>Supported in mainline and Debian kernel since 2.6.25</td>
</tr>

<tr>
<td style="color: white; background-color: #00AA00">mv2120 kernel</td>
<td>Supported in the Debian kernel since 2.6.25 and in the mainline
kernel since 2.6.27</td>
</tr>

<tr>
<td style="color: white; background-color: #00AA00">SATA</td>
<td>Supported in the kernel by the `sata_mv` module</td>
</tr>

<tr>
<td style="color: white; background-color: #00AA00">Ethernet</td>
<td>Supported in the kernel by the `mv643xx` module</td>
</tr>

<tr>
<td style="color: white; background-color: #00AA00">USB</td>
<td>Supported in the kernel since 2.6.25</td>
</tr>

<tr>
<td style="color: white; background-color: #00AA00">RTC</td>
<td>Supported in the kernel by the `rtc-pcf8563` module</td>
</tr>

<tr>
<td style="color: white; background-color: #00AA00">LEDs</td>
<td>Supported in the Debian kernel as of 2.6.26 and Debian will use the
LEDs to signal the status of the boot process.</td>
</tr>

<tr>
<td style="color: white; background-color: #00AA00">Fan</td>
<td>It seems the mv2120 has no temperature sensor or way to regulate
the fan.</td>
</tr>

<tr>
<td style="color: white; background-color: #00AA00">XOR engine</td>
<td>Supported in the Debian kernel since 2.6.26 and in the mainline
kernel since 2.6.27.  Support is mainly helpful for RAID5 at the
moment, so it's not quite useful on the mv2120</td>
</tr>

<tr>
<td style="color: black; background-color: #FFFF00">Crypto engine</td>
<td>Initial support in 2.6.32</td>
</tr>

</table>

<div class="bbf">
<%= render "adsense-banner-before-footer" %>
</div>

