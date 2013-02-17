---
title: Status of Kurobox Pro support
nav: Status
description: Status of Kurobox Pro support in Debian
keywords: [Buffalo, Revogear, Kurobox Pro, support, status]
---

<% content_for :right do %>
<img src = "../images/r_kuroboxpro_front.jpg" class="border" alt="Kurobox Pro from the front" width="148" height="231" />

<%= render 'adsense-wideskyscaper-right' %>
<% end %>

<h1>Status of Kurobox Pro support</h1>

The Kurobox Pro is based on a Marvell Orion System on a Chip.  Marvell has
done a lot of work in the last few months to get support for the Orion
platform into the mainline kernel and they continue to work on getting this
platform fully supported.  However, since this is an ongoing effort, some
features of the Orion platform are currently not as well supported as in
the original Marvell LSP (Linux Support Package) used by Buffalo.  Please
take this into account before deciding whether you want to install Debian,
especially if you have specific requirements (e.g. related to performance).

The table below shows how well different components of the Kurobox Pro are
supported by Debian:

<table style="border-style: none" border="1" cellpadding="5">

<tr style="background-color: #E0E0FF">
<td>Component</td>
<td>Comment</td>
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
<td style="color: white; background-color: #00AA00">Kurobox Pro kernel</td>
<td>Supported in mainline and Debian kernel since 2.6.25</td>
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
<td>Supported in the kernel by the `rtc-rs5c372` module</td>
</tr>

<tr>
<td style="color: white; background-color: #00AA00">LEDs</td>
<td>Supported by micro-evtd</td>
</tr>

<tr>
<td style="color: white; background-color: #00AA00">Fan</td>
<td>Supported by micro-evtd.</td>
</tr>

<tr>
<td style="color: white; background-color: #00AA00">Beeper</td>
<td>Supported by micro-evtd.</td>
</tr>

<tr>
<td style="color: white; background-color: #00AA00">XOR engine</td>
<td>Supported in the Debian kernel since 2.6.26 and in the mainline
kernel since 2.6.27.  Support is mainly helpful for RAID5 at the
moment, so it's not quite useful on the Kurobox Pro.</td>
</tr>

<tr>
<td style="color: black; background-color: #FFFF00">Crypto engine</td>
<td>Initial support in 2.6.32</td>
</tr>

</table>

Go back to my <a href = "..">Debian on Kurobox Pro</a> page.

<div class="bbf">
<%= render 'adsense-banner-before-footer' %>
</div>

