---
title: Debian on the GLAN Tank
nav: GLAN Tank
description: Instructions for running Debian on the GLAN Tank
keywords: [Debian, GLAN Tank, installation, guide, IOP, NAS, server]
---

<div class="alert alert-danger">

Intel's IOP platform is no longer supported in Debian.

</div>

<div class="right">
<img src = "images/r_glantank.jpg" class="border" alt="Thecus N2100" width="148" height="100" />
</div>

The GLAN Tank is a Network Attached Storage (NAS) device based on Intel's
IOP 80219 CPU.  Other devices from IO-Data, in particular the HDL-Gxxx,
HDL-GWxxx, and HDL-GZxxx series, are very similar.  The GLAN Tank
(SOTO-HDLGW) has the following features:

<ul>

<li>Intel IOP 80219 CPU running at 400 MHz</li>

<li>2 IDE slots</li>

<li>128 MB RAM</li>

<li>4 USB 2.0 ports</li>

<li>1 GBit Ethernet</li>

</ul>

<h2>Support status</h2>

While the GLAN Tank was supported up to Debian 7 (wheezy), it is no longer
supported in Debian 8 (jessie) or later releases.

<h2>Information</h2>

<ul>

<li>An <a href = "install/">installation guide</a> for Debian on the GLAN
Tank.  A <a href =
"http://iohack.sourceforge.jp/tanks/index.php?DEBIANonGLANTANK">Japanese
translation</a> of these instructions are available.</li>

<li>An <a href = "gallery/">image gallery</a> with various pictures showing
the internals of the GLAN Tank.</li>

</ul>

<h2>Acknowledgements</h2>

Kinneko-san of IO-Data for providing a GLAN Tank to Lennert Buytenhek and
me each.  Hiroyuki Araki for maintaining a series of kernel patches for the
GLAN Tank.  Gordon Farquharson for doing lots of testing.

