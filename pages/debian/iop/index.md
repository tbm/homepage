---
title: Debian on Intel IOP
nav: Intel IOP
description: Information about running Debian on devices based on Intel's IOP chip
keywords: [Debian, Intel, IOP, I/O processor, NAS, SAN, installation, guide]
---

<div class="right">
<img src = "images/r_intel.gif" class="border" alt="Intel logo" width="148" height="107" />
</div>

Intel's IOP (I/O processor) line is based on their XScale core, an
implementation of the ARM instruction set.  There are a number of NAS
devices based on IOP chips that can run Debian.  This page provides
instructions about running Debian on these devices.  Please note, however,
that the IOP series has reached its end of life.

Debian used to support the following devices:

<ul>

<li><a href = "n2100/">Thecus N2100</a>: this is a NAS device with a 600 MHz
IOP chip, 2 SATA slots, expandable DDR RAM, 3 USB ports, 2 GBit Ethernet
and mini-PCI.  This device is also sold by Allnet as the ALL6500 and by
Evesham as the SilverSTOR M-Box.</li>

<li><a href = "glantank/">IO-Data GLAN Tank</a>: this is a NAS device with a
400 MHz IOP chip, 2 IDE slots, 128 MB RAM, 4 USB ports and 1 GBit Ethernet.
Other devices from IO-Data, in particular the HDL-Gxxx, HDL-GWxxx, and
HDL-GZxxx series, are very similar and might work as well.</li>

<li>Intel SS4000-E: based on a 400 MHz IOP CPU, this device has 4 SATA
slots, 256 MB RAM (expandable), 2 USB ports and 1 GBit Ethernet.
Apparently this machine is also known as the Intel Baxter Creek SS4000-E.
This system appears to be based on a design by Lanner, a company that sells
the NAS appliances NS04-4100 and NS04-4110.  Wouter Verhelst
ported Debian to this device.</li>

</ul>

Support for IOP32x was dropped in Debian 8 (jessie).

<h2>Help</h2>

If you need any help getting Debian running on your IOP based machine after
reading this installation guide and using Google, you
can contact the <a href = "http://lists.debian.org/debian-arm/">Debian
ARM</a> mailing list.

