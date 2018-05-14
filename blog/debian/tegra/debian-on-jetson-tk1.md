---
title: "Debian on Jetson TK1"
date: 2016-07-24 18:31:28 -0700
---

<img src="/images/jetson-tk1-debian8.jpg"
 alt="Debian on Jetson TK1" class="right" width="504" height="378" />

I became interested in running Debian on NVIDIA's Tegra platform recently.
NVIDIA is doing a great job getting support for Tegra upstream (u-boot,
kernel, X.org and other projects).  As part of ensuring good Debian support
for Tegra, I wanted to install Debian on a Jetson TK1, a development board
from NVIDIA based on the Tegra K1 chip (Tegra 124), a 32-bit ARM chip.

Ian Campbell enabled u-boot and Linux kernel support and added support in
the installer for this device about a year ago.  I updated some kernel
options since there has been a lot of progress upstream in the meantime,
performed a lot of tests and documented the installation process on the
Debian wiki.  Wookey made substantial improvements to the wiki as well.

If you're interested in a good 32-bit ARM development platform, give
[Debian on the Jetson
TK1](https://wiki.debian.org/InstallingDebianOn/NVIDIA/Jetson-TK1) a try.

There's also a 64-bit board.  More on that later...

