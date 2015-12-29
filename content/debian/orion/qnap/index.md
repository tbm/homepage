---
title: Debian on QNAP Turbo Station
nav: QNAP
description: Useful page for running Debian on the QNAP Turbo Station
keywords: [Debian, QNAP, QNAP Turbo Station, Orion, TS-109, TS-209, TS-409]
---

<% content_for :right do %>
<img src = "images/r_ts109_ts209_front.jpg" class="border" alt="QNAP TS-109 and TS-209 from the front" width="148" height="120" />

<%= render "adsense-wideskyscaper-right" %>
<% end %>

<h1>Debian on QNAP Turbo Station</h1>

Debian supports all Orion based QNAP Turbo Stations.  This includes the
TS-109, TS-209, TS-409 and TS-409U.

There are additional pages with instructions and information about all
supported models:

<ul>
<li><a href = "ts-109/">QNAP TS-109</a></li>
<li><a href = "ts-209/">QNAP TS-209</a></li>
<li><a href = "ts-409/">QNAP TS-409 and TS-409U</a></li>
</ul>

Here is a table showing the differences between the supported devices:

<table>

<tr>
<th style="background-color: white"></th>
<th>TS-109</th>
<th>TS-109 II</th>
<th>TS-209</th>
<th>TS-209 II</th>
<th>TS-409</th>
<th>TS-409U</th>
</tr>

<tr>
<td style="background-color: #E0E0FF">CPU</td>
<td>88F5182 500MHz</td>
<td>88F5182 500MHz</td>
<td>88F5182 500MHz</td>
<td>88F5182 500MHz</td>
<td>88F5281 500MHz</td>
<td>88F5281 500MHz</td>
</tr>

<tr>
<td style="background-color: #E0E0FF">RAM</td>
<td>128 MB</td>
<td>256 MB</td>
<td>128 MB</td>
<td>256 MB</td>
<td>256 MB</td>
<td>512 MB</td>
</tr>

<tr>
<td style="background-color: #E0E0FF">Flash</td>
<td>8 MB</td>
<td>8 MB</td>
<td>8 MB</td>
<td>8 MB</td>
<td>8 MB</td>
<td>8 MB</td>
</tr>

<tr>
<td style="background-color: #E0E0FF">HDD</td>
<td>1</td>
<td>1</td>
<td>2</td>
<td>2</td>
<td>4</td>
<td>4</td>
</tr>

<tr>
<td style="background-color: #E0E0FF">eSATA</td>
<td>1</td>
<td>1</td>
<td>no</td>
<td>no</td>
<td>no</td>
<td>no</td>
</tr>

<tr>
<td style="background-color: #E0E0FF">USB 2.0 front</td>
<td>1</td>
<td>1</td>
<td>1</td>
<td>1</td>
<td>1</td>
<td>1</td>
</tr>

<tr>
<td style="background-color: #E0E0FF">USB 2.0 back</td>
<td>2</td>
<td>2</td>
<td>2</td>
<td>2</td>
<td>2</td>
<td>2</td>
</tr>

<tr>
<td style="background-color: #E0E0FF">Ethernet</td>
<td>1</td>
<td>1</td>
<td>1</td>
<td>1</td>
<td>1</td>
<td>1</td>
</tr>

<tr>
<td style="background-color: #E0E0FF">Fan</td>
<td>no</td>
<td>no</td>
<td>1</td>
<td>1</td>
<td>1</td>
<td>3</td>
</tr>

</table>

The Pro variants are the same hardware as the regular variants.  They only
differ in the software included in the original QNAP firmware.

Debian also supports QNAP's <a href = "../../kirkwood/qnap/">Turbo NAS</a>
devices, which are based on Marvell's Kirkwood chip.

<div class="bbf">
<%= render "adsense-banner-before-footer" %>
</div>

