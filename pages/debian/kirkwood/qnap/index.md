---
title: Debian on QNAP Turbo NAS
nav: QNAP
description: Useful page for running Debian on the QNAP Turbo NAS
keywords: [Debian, QNAP, QNAP Turbo NAS, Kirkwood, TS-110, TS-119, TS-119P+, TS-210, TS-219, TS-219P, TS-219P+]
---

<div class="right">
<img src = "ts-219/images/r_ts219_open.jpg" class="border" alt="Open QNAP TS-219" width="148" height="119" />
</div>

<h1>Debian on QNAP Turbo NAS</h1>

Debian supports devices from QNAP's Turbo NAS devices that are based on the
Marvell Kirkwood platform.   This includes the following devices:

<ul>
<li><a href = "ts-119/">QNAP TS-110, TS-112, TS-112P, TS-119, TS-119P+, TS-119P II, TS-120 and TS-121</a></li>
<li><a href = "ts-219/">QNAP HS-210, TS-210, TS-212, TS-212-E, TS-212P, TS-219, TS-219P, TS-219P+, TS-219P II, TS-220 and TS-221</a></li>
<li><a href = "ts-41x/">QNAP TS-410, TS-410U, TS-412, TS-419P, TS-419P+, TS-419P II, TS-419U, TS-419U+, TS-420, TS-420U, TS-421 and TS-421U</a></li>
</ul>

Please note that the TS-x31 series is not supported since these devices
don't use Marvell Kirkwood chips.

Here is a table showing the differences between the supported devices:

<table class="table table-hover">

<thead>
<tr>
<th></th>
<th>TS-110</th>
<th>TS-112</th>
<th>TS-112P</th>
<th>TS-119</th>
<th>TS-119P+</th>
<th>TS-119P II</th>
<th>TS-120</th>
<th>TS-121</th>
</tr>
</thead>

<tbody>
<tr>
<th>CPU</th>
<td>800 MHz</td>
<td>1.2 GHz</td>
<td>1.6 GHz</td>
<td>1.2 GHz</td>
<td>1.6 GHz</td>
<td>2.0 GHz</td>
<td>1.6 GHz</td>
<td>2.0 GHz</td>
</tr>

<tr>
<th>RAM</th>
<td>256 MB</td>
<td>256 MB</td>
<td>512 MB</td>
<td>512 MB</td>
<td>512 MB</td>
<td>512 MB</td>
<td>512 MB</td>
<td>1 GB</td>
</tr>

<tr>
<th>Flash</th>
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
<th>HDD</th>
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
<th>eSATA</th>
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
<th>USB front</th>
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
<th>USB back</th>
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
<th>USB 3.0</th>
<td>none</td>
<td>none</td>
<td>2</td>
<td>none</td>
<td>none</td>
<td>none</td>
<td>2</td>
<td>2</td>
</tr>

<tr>
<th>Ethernet</th>
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
<th>Fan</th>
<td>1</td>
<td>1</td>
<td>1</td>
<td>no</td>
<td>1</td>
<td>1</td>
<td>1</td>
<td>1</td>
</tr>
</tbody>

</table>

<table class="table table-hover">

<thead>
<tr>
<th></th>
<th>HS-210</th>
<th>TS-210</th>
<th>TS-212</th>
<th>TS-212-E</th>
<th>TS-212P</th>
<th>TS-219</th>
<th>TS-219P</th>
<th>TS-219P+</th>
<th>TS-219P II</th>
<th>TS-220</th>
<th>TS-221</th>
</tr>
</thead>

<tbody>
<tr>
<th scope="row">CPU</th>
<td>1.6 GHz</td>
<td>800 MHz</td>
<td>1.2 GHz</td>
<td>1.6 GHz</td>
<td>1.6 GHz</td>
<td>1.2 GHz</td>
<td>1.2 GHz</td>
<td>1.6 GHz</td>
<td>2.0 GHz</td>
<td>1.6 GHz</td>
<td>2.0 GHz</td>
</tr>

<tr>
<th>RAM</th>
<td>512 MB</td>
<td>256 MB</td>
<td>256 MB</td>
<td>256 MB</td>
<td>512 MB</td>
<td>512 MB</td>
<td>512 MB</td>
<td>512 MB</td>
<td>512 MB</td>
<td>512 MB</td>
<td>1 GB</td>
</tr>

<tr>
<th>Flash</th>
<td>16 MB</td>
<td>16 MB</td>
<td>16 MB</td>
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
<th>HDD</th>
<td>2</td>
<td>2</td>
<td>2</td>
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
<th>eSATA</th>
<td>no</td>
<td>no</td>
<td>no</td>
<td>no</td>
<td>no</td>
<td>no</td>
<td>2</td>
<td>2</td>
<td>2</td>
<td>2</td>
<td>2</td>
</tr>

<tr>
<th>USB front</th>
<td>0</td>
<td>1</td>
<td>1</td>
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
<th>USB back</th>
<td>4</td>
<td>2</td>
<td>2</td>
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
<th>USB 3.0</th>
<td>2</td>
<td>none</td>
<td>none</td>
<td>2</td>
<td>2</td>
<td>none</td>
<td>none</td>
<td>none</td>
<td>none</td>
<td>2</td>
<td>2</td>
</tr>

<tr>
<th>Ethernet</th>
<td>1</td>
<td>1</td>
<td>1</td>
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
<th>Fan</th>
<td>none</td>
<td>1</td>
<td>1</td>
<td>1</td>
<td>1</td>
<td>1</td>
<td>1</td>
<td>1</td>
<td>1</td>
<td>1</td>
<td>1</td>
</tr>
</tbody>

</table>

<table class="table table-hover">

<thead>
<tr>
<th></th>
<th>TS-410</th>
<th>TS-410U</th>
<th>TS-412</th>
<th>TS-419P</th>
<th>TS-419P+</th>
<th>TS-419P II</th>
</tr>
</thead>

<tbody>
<tr>
<th>CPU</th>
<td>800 MHz</td>
<td>800 MHz</td>
<td>1.2 GHz</td>
<td>1.2 GHz</td>
<td>1.6 GHz</td>
<td>2.0 GHz</td>
</tr>

<tr>
<th>RAM</th>
<td>256 MB</td>
<td>512 MB</td>
<td>256 MB</td>
<td>512 MB</td>
<td>512 MB</td>
<td>512 MB</td>
</tr>

<tr>
<th>Flash</th>
<td>16 MB</td>
<td>16 MB</td>
<td>16 MB</td>
<td>16 MB</td>
<td>16 MB</td>
<td>16 MB</td>
</tr>

<tr>
<th>HDD</th>
<td>4</td>
<td>4</td>
<td>4</td>
<td>4</td>
<td>4</td>
<td>4</td>
</tr>

<tr>
<th>eSATA</th>
<td>2</td>
<td>2</td>
<td>2</td>
<td>2</td>
<td>2</td>
<td>2</td>
</tr>

<tr>
<th>USB front</th>
<td>1</td>
<td>1</td>
<td>1</td>
<td>1</td>
<td>1</td>
<td>1</td>
</tr>

<tr>
<th>USB back</th>
<td>3</td>
<td>3</td>
<td>3</td>
<td>3</td>
<td>3</td>
<td>3</td>
</tr>

<tr>
<th>USB 3.0</th>
<td>none</td>
<td>none</td>
<td>none</td>
<td>none</td>
<td>none</td>
<td>depends</td>
</tr>

<tr>
<th>Ethernet</th>
<td>2</td>
<td>2</td>
<td>2</td>
<td>2</td>
<td>2</td>
<td>2</td>
</tr>

<tr>
<th>Fan</th>
<td>1</td>
<td>3</td>
<td>1</td>
<td>1</td>
<td>1</td>
<td>1</td>
</tr>

<tr>
<th>LCD panel</th>
<td>no</td>
<td>no</td>
<td>no</td>
<td>yes</td>
<td>yes</td>
<td>yes</td>
</tr>
</tbody>

</table>

<table class="table table-hover">

<thead>
<tr>
<th></th>
<th>TS-419U</th>
<th>TS-419U+</th>
<th>TS-420</th>
<th>TS-420U</th>
<th>TS-421</th>
<th>TS-421U</th>
</tr>
<thead>

<tbody>
<tr>
<th>CPU</th>
<td>1.2 GHz</td>
<td>1.6 GHz</td>
<td>1.6 GHz</td>
<td>1.6 GHz</td>
<td>2.0 GHz</td>
<td>2.0 GHz</td>
</tr>

<tr>
<th>RAM</th>
<td>512 MB</td>
<td>512 MB</td>
<td>512 MB</td>
<td>1 GB</td>
<td>1 GB</td>
<td>1 GB</td>
</tr>

<tr>
<th>Flash</th>
<td>16 MB</td>
<td>16 MB</td>
<td>16 MB</td>
<td>16 MB</td>
<td>16 MB</td>
<td>16 MB</td>
</tr>

<tr>
<th>HDD</th>
<td>4</td>
<td>4</td>
<td>4</td>
<td>4</td>
<td>4</td>
<td>4</td>
</tr>

<tr>
<th>eSATA</th>
<td>2</td>
<td>2</td>
<td>2</td>
<td>2</td>
<td>2</td>
<td>2</td>
</tr>

<tr>
<th>USB front</th>
<td>1</td>
<td>1</td>
<td>1</td>
<td>1</td>
<td>1</td>
<td>1</td>
</tr>

<tr>
<th>USB back</th>
<td>3</td>
<td>3</td>
<td>3</td>
<td>3</td>
<td>3</td>
<td>3</td>
</tr>

<tr>
<th>USB 3.0</th>
<td>none</td>
<td>none</td>
<td>2</td>
<td>2</td>
<td>2</td>
<td>2</td>
</tr>

<tr>
<th>Ethernet</th>
<td>2</td>
<td>2</td>
<td>2</td>
<td>2</td>
<td>2</td>
<td>2</td>
</tr>

<tr>
<th>Fan</th>
<td>3</td>
<td>2</td>
<td>1</td>
<td>2</td>
<td>1</td>
<td>2</td>
</tr>

<tr>
<th>LCD panel</th>
<td>no</td>
<td>no</td>
<td>no</td>
<td>no</td>
<td>yes</td>
<td>no</td>
</tr>
</tbody>

</table>

