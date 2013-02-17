---
title: Status of OpenRD support
nav: Status
description: Status of OpenRD support in Debian
keywords: [Debian, OpenRD, support, status]
---

<% content_for :right do %>
<%= render 'adsense-wideskyscaper-right' %>
<% end %>

<h1>Status of OpenRD support</h1>

The table below shows how well different components of the OpenRD are
supported by Debian:

<table style="border-style: none" border="1" cellpadding="5">

<tr style="background-color: #E0E0FF">
<td>Component</td>
<td>Comment</td>
</tr>

<tr>
<td style="color: white; background-color: #00AA00">Debian</td>
<td>Debian and Debian installer work well</td>
</tr>

<tr>
<td style="color: white; background-color: #00AA00">CPU</td>
<td>Supported in the kernel by the `kirkwood` platform</td>
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
<td>Supported</td>
</tr>

<tr>
<td style="color: white; background-color: #00AA00">VGA</td>
<td>Supported in the official kernel since 2.6.35 and included in
Debian's 2.6.32 kernel in Debian squeeze.</td>
</tr>

<tr>
<td style="color: black; background-color: #FFFF00">Audio</td>
<td>Audio is supported in 2.6.36 kernels but is not included in Debian's
squeeze kernel which is based on 2.6.32.</td>
</tr>

</table>

<div class="bbf">
<%= render 'adsense-banner-before-footer' %>
</div>

