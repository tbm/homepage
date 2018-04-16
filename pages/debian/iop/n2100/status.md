---
title: Status of Thecus N2100 support
nav: Status
description: Status of Thecus N2100 support
keywords: [Debian, Thecus, N2100, support, status]
---

<div class="right">
<img src = "../images/r_n2100_debian.jpg" class="border" alt="Thecus N2100" width="133" height="148" />
</div>

The table below shows how well different components of the Thecus N2100 are
supported by Debian 7 (wheezy).

Note that this device is no longer supported by Debian 8 (jessie) or later
releases.

<table class="table table-hover">

<thead>
<tr>
<th>Component</th>
<th>Comment</th>
</tr>
</thead>

<tbody>
<tr class="table-success">
<th>Debian</th>
<td>Debian installer works well.</td>
</tr>

<tr class="table-success">
<th>CPU</th>
<td>Supported in mainline and Debian kernel.</td>
</tr>

<tr class="table-warning">
<th>SATA</th>
<td>Supported in the kernel by the `sata_sil` module.  However,
the hard drive speed is slow.</td>
</tr>

<tr class="table-success">
<th>Ethernet</th>
<td>Supported in the kernel by the `r8169` module.</td>
</tr>

<tr class="table-success">
<th>USB</th>
<td>Supported in the kernel.</td>
</tr>

<tr class="table-success">
<th>RTC</th>
<td>Supported in the kernel by the `rtc-rs5c372` module.</td>
</tr>

<tr class="table-success">
<th>LEDs</th>
<td>Supported in the kernel.</td>
</tr>

<tr class="table-warning">
<th>Fan</th>
<td>Supported in in the kernel, but there is no automatic regulation
of the fan based on the current temperature.</td>
</tr>

<tr class="table-success">
<th>Beeper</th>
<td>Supported in the kernel.</td>
</tr>
</tbody>

</table>

