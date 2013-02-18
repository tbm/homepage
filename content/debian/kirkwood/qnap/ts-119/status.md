---
title: Status of QNAP TS-11x support
nav: Status
description: Status of QNAP TS-11x support in Debian
keywords: [Debian, QNAP, TS-110, TS-112, TS-119, support, status]
---

<% content_for :right do %>
<img src = "../images/r_qnap_ts110.jpg" class="border" alt="QNAP TS-110 from the front" width="148" height="206" />

<%= render "adsense-wideskyscaper-right" %>
<% end %>

<h1>Status of QNAP TS-11x support</h1>

QNAP TS-11x devices are based on a Marvell Kirkwood System on a Chip.
Marvell has done a lot of work to get support for the Kirkwood platform
into the mainline kernel.  However, some features of the Kirkwood platform
are not as well supported in the mainline kernel (which we use in Debian)
as in the original Marvell LSP (Linux Support Package) used by QNAP.
Please take this into account before deciding whether you want to install
Debian, especially if you have specific requirements (e.g. related to
performance).

The table below shows how well different components of the QNAP TS-11x are
supported by Debian:

<table style="border-style: none" border="1" cellpadding="5">

<tr style="background-color: #E0E0FF">
<td>Component</td>
<td>Comment</td>
</tr>

<tr>
<td style="color: white; background-color: #00AA00">Debian</td>
<td>Debian and the Debian installer work well</td>
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
<td style="color: white; background-color: #00AA00">RTC</td>
<td>Supported in the kernel by the `rtc-s35390a` module</td>
</tr>

<tr>
<td style="color: white; background-color: #00AA00">LEDs</td>
<td>Supported in qcontrol</td>
</tr>

<tr>
<td style="color: black; background-color: #FFFF00">Fan</td>
<td>Supported in qcontrol, but there is no automatic regulation of
the fan based on the current temperature.</td>
</tr>

<tr>
<td style="color: white; background-color: #00AA00">Beeper</td>
<td>Supported in qcontrol</td>
</tr>

<tr>
<td style="color: white; background-color: #00AA00">XOR engine</td>
<td>Supported. Support is mainly helpful for RAID5 at the
moment, so it's not quite useful on the TS-11x</td>
</tr>

<tr>
<td style="color: black; background-color: #FFFF00">Crypto engine</td>
<td>Initial support in 2.6.32</td>
</tr>

<tr>
<td style="color: white; background-color: #AA0000">Wake-on-LAN (WOL)</td>
<td>Not supported.  Looking for a <a href =
"http://lists.debian.org/debian-arm/2011/05/msg00030.html">volunteer who
can adapt the Linux kernel</a></td>
</tr>

<tr>
<td style="color: white; background-color: #AA0000">Scheduled power</td>
<td>Not supported in Debian 6.0 but this will be supported in the next
release (Debian wheezy, version 7.0).</td>
</tr>

</table>

<div class="bbf">
<%= render "adsense-banner-before-footer" %>
</div>

