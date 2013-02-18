---
title: Debian on QNAP Turbo NAS
nav: QNAP
description: Useful page for running Debian on the QNAP Turbo NAS
keywords: [Debian, QNAP, QNAP Turbo NAS, Kirkwood, TS-110, TS-119, TS-119P+, TS-210, TS-219, TS-219P, TS-219P+]
---

<% content_for :right do %>
<img src = "ts-219/images/r_ts219_open.jpg" class="border" alt="Open QNAP TS-219" width="148" height="119" />

<%= render "adsense-wideskyscaper-right" %>
<% end %>

<h1>Debian on QNAP Turbo NAS</h1>

Debian supports QNAP's Turbo NAS devices.  This includes the following
devices:

<ul>
<li><a href = "ts-119">QNAP TS-110, TS-112, TS-119, TS-119P+ and TS-119P II</a></li>
<li><a href = "ts-219">QNAP TS-210, TS-212, TS-219, TS-219P, TS-219P+ and TS-219P II</a></li>
<li><a href = "ts-41x">QNAP TS-410, TS-410U, TS-419P, TS-419P+, TS-419P II, TS-419U and TS-419U+</a></li>
</ul>

Here is a table showing the differences between these devices:

<table style="border-style: none" border="1" cellpadding="5">

<tr>
<th style="background-color: white"></th>
<th>TS-110</th>
<th>TS-112</th>
<th>TS-119</th>
<th>TS-119P+</th>
<th>TS-119P II</th>
</tr>

<tr>
<td style="background-color: #E0E0FF">CPU</td>
<td>800 MHz</td>
<td>1.2 GHz</td>
<td>1.2 GHz</td>
<td>1.6 GHz</td>
<td>2.0 GHz</td>
</tr>

<tr>
<td style="background-color: #E0E0FF">RAM</td>
<td>256 MB</td>
<td>256 MB</td>
<td>512 MB</td>
<td>512 MB</td>
<td>512 MB</td>
</tr>

<tr>
<td style="background-color: #E0E0FF">Flash</td>
<td>16 MB</td>
<td>16 MB</td>
<td>16 MB</td>
<td>16 MB</td>
<td>16 MB</td>
</tr>

<tr>
<td style="background-color: #E0E0FF">HDD</td>
<td>1</td>
<td>1</td>
<td>1</td>
<td>1</td>
<td>1</td>
</tr>

<tr>
<td style="background-color: #E0E0FF">eSATA</td>
<td>1</td>
<td>1</td>
<td>1</td>
<td>1</td>
<td>1</td>
</tr>

<tr>
<td style="background-color: #E0E0FF">USB front</td>
<td>1</td>
<td>1</td>
<td>1</td>
<td>1</td>
<td>1</td>
</tr>

<tr>
<td style="background-color: #E0E0FF">USB back</td>
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
</tr>

<tr>
<td style="background-color: #E0E0FF">Fan</td>
<td>1</td>
<td>1</td>
<td>no</td>
<td>1</td>
<td>1</td>
</tr>

</table>

<table style="border-style: none" border="1" cellpadding="5">

<tr>
<th style="background-color: white"></th>
<th>TS-210</th>
<th>TS-212</th>
<th>TS-219</th>
<th>TS-219P</th>
<th>TS-219P+</th>
<th>TS-219P II</th>
</tr>

<tr>
<td style="background-color: #E0E0FF">CPU</td>
<td>800 MHz</td>
<td>1.2 GHz</td>
<td>1.2 GHz</td>
<td>1.2 GHz</td>
<td>1.6 GHz</td>
<td>2.0 GHz</td>
</tr>

<tr>
<td style="background-color: #E0E0FF">RAM</td>
<td>256 MB</td>
<td>256 MB</td>
<td>512 MB</td>
<td>512 MB</td>
<td>512 MB</td>
<td>512 MB</td>
</tr>

<tr>
<td style="background-color: #E0E0FF">Flash</td>
<td>16 MB</td>
<td>16 MB</td>
<td>16 MB</td>
<td>16 MB</td>
<td>16 MB</td>
<td>16 MB</td>
</tr>

<tr>
<td style="background-color: #E0E0FF">HDD</td>
<td>2</td>
<td>2</td>
<td>2</td>
<td>2</td>
<td>2</td>
<td>2</td>
</tr>

<tr>
<td style="background-color: #E0E0FF">eSATA</td>
<td>no</td>
<td>no</td>
<td>no</td>
<td>2</td>
<td>2</td>
<td>2</td>
</tr>

<tr>
<td style="background-color: #E0E0FF">USB front</td>
<td>1</td>
<td>1</td>
<td>1</td>
<td>1</td>
<td>1</td>
<td>1</td>
</tr>

<tr>
<td style="background-color: #E0E0FF">USB back</td>
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
<td>1</td>
<td>1</td>
<td>1</td>
<td>1</td>
<td>1</td>
<td>1</td>
</tr>

</table>

<table style="border-style: none" border="1" cellpadding="5">

<tr>
<th style="background-color: white"></th>
<th>TS-410</th>
<th>TS-410U</th>
<th>TS-412</th>
<th>TS-419P</th>
<th>TS-419P+</th>
<th>TS-419P II</th>
<th>TS-419U</th>
<th>TS-419U+</th>
</tr>

<tr>
<td style="background-color: #E0E0FF">CPU</td>
<td>800 MHz</td>
<td>800 MHz</td>
<td>1.2 GHz</td>
<td>1.2 GHz</td>
<td>1.6 GHz</td>
<td>2.0 GHz</td>
<td>1.2 GHz</td>
<td>1.6 GHz</td>
</tr>

<tr>
<td style="background-color: #E0E0FF">RAM</td>
<td>256 MB</td>
<td>512 MB</td>
<td>256 MB</td>
<td>512 MB</td>
<td>512 MB</td>
<td>512 MB</td>
<td>512 MB</td>
<td>512 MB</td>
</tr>

<tr>
<td style="background-color: #E0E0FF">Flash</td>
<td>16 MB</td>
<td>16 MB</td>
<td>16 MB</td>
<td>16 MB</td>
<td>16 MB</td>
<td>16 MB</td>
<td>16 MB</td>
<td>16 MB</td>
</tr>

<tr>
<td style="background-color: #E0E0FF">HDD</td>
<td>4</td>
<td>4</td>
<td>4</td>
<td>4</td>
<td>4</td>
<td>4</td>
<td>4</td>
<td>4</td>
</tr>

<tr>
<td style="background-color: #E0E0FF">eSATA</td>
<td>2</td>
<td>2</td>
<td>2</td>
<td>2</td>
<td>2</td>
<td>2</td>
<td>2</td>
<td>2</td>
</tr>

<tr>
<td style="background-color: #E0E0FF">USB front</td>
<td>1</td>
<td>1</td>
<td>1</td>
<td>1</td>
<td>1</td>
<td>1</td>
<td>1</td>
<td>1</td>
</tr>

<tr>
<td style="background-color: #E0E0FF">USB back</td>
<td>3</td>
<td>3</td>
<td>3</td>
<td>3</td>
<td>3</td>
<td>3</td>
<td>3</td>
<td>3</td>
</tr>

<tr>
<td style="background-color: #E0E0FF">Ethernet</td>
<td>2</td>
<td>2</td>
<td>2</td>
<td>2</td>
<td>2</td>
<td>2</td>
<td>2</td>
<td>2</td>
</tr>

<tr>
<td style="background-color: #E0E0FF">Fan</td>
<td>1</td>
<td>3</td>
<td>1</td>
<td>1</td>
<td>1</td>
<td>1</td>
<td>3</td>
<td>2</td>
</tr>

</table>

<div class="bbf">
<%= render "adsense-banner-before-footer" %>
</div>

