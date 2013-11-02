---
title: Status of QNAP TS-409 support
nav: Status
description: Status of QNAP TS-409 support in Debian
keywords: [Debian, QNAP, TS-409, support, status]
---

<% content_for :right do %>
<img src = "../images/r_ts409_front.jpg" class="border" alt="QNAP TS-409 from the front" width="148" height="147" />

<%= render "adsense-wideskyscaper-right" %>
<% end %>

<h1>Status of QNAP TS-409 support</h1>

The QNAP TS-409 is based on a Marvell Orion System on a Chip.  Marvell has
done a lot of work to get support for the Orion platform into the mainline
kernel.  However, some features of the Orion platform are not as well
supported as in the original Marvell LSP (Linux Support Package) used by
QNAP.  Please take this into account before deciding whether you want to
install Debian, especially if you have specific requirements (e.g. related
to performance).

The table below shows how well different components of the QNAP TS-409 are
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
<td>Supported in mainline and Debian kernel since 2.6.25 but there is <a
href = "../5281-d0-bug/">one bug</a> you may want to know about</td>
</tr>

<tr>
<td style="color: white; background-color: #00AA00">TS-409 kernel</td>
<td>Supported in the Debian kernel since 2.6.25 and since 2.6.27 in
the mainline kernel.</td>
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
<td>Supported in the kernel by the `rtc-s35390a` module since 2.6.25</td>
</tr>

<tr>
<td style="color: white; background-color: #00AA00">LEDs</td>
<td>Supported in qcontrol</td>
</tr>

<tr>
<td style="color: white; background-color: #00AA00">Fan</td>
<td>Supported in qcontrol; you can <a href="../tips/#qcontrol-upgrade">upgrade
qcontrol</a> to get automatic temperature regulation.</td>
</tr>

<tr>
<td style="color: white; background-color: #00AA00">Beeper</td>
<td>Supported in qcontrol</td>
</tr>

</table>

<div class="bbf">
<%= render "adsense-banner-before-footer" %>
</div>

