---
title: Status of QNAP TS-41x support
nav: Status
description: Status of QNAP QNAP TS-41x support in Debian
keywords: [Debian, QNAP, TS-410, TS-410U, TS-412, TS-419P, TS-419U, support, status]
---

<% content_for :right do %>
<img src = "../images/r_qnap_ts419p.jpg" class="border" alt="QNAP TS-419P from the front" width="148" height="148" />

<%= render "adsense-wideskyscaper-right" %>
<% end %>

<h1>Status of QNAP TS-410, TS-410U, TS-412, TS-419P, TS-419P+, TS-419U and TS-410U+</h1>

The QNAP TS-41x is based on a Marvell Kirkwood System on a Chip.  Marvell
has done a lot of work in the last few months to get support for the
Kirkwood platform into the mainline kernel and they continue to work on
getting this platform fully supported.  However, since this is an ongoing
effort, some features of the Kirkwood platform are currently not as well
supported as in the original Marvell LSP (Linux Support Package) used by
QNAP.  Please take this into account before deciding whether you want to
install Debian, especially if you have specific requirements (e.g. related
to performance).

The table below shows how well different components of the QNAP TS-41x are
supported by Debian:

<table>

<tr>
<th>Component</th>
<th>Comment</th>
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
<td style="color: white; background-color: #AA0000">LCD (TS-419P/TS-419P+)</td>
<td>Supported in upstream qcontrol but not yet in Debian</td>
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
<td>Supported</td>
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

