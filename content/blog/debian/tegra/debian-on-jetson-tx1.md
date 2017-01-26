---
title: "Debian on Jetson TX1"
created_at: 2017-01-26 13:51:25 -0800
kind: article
---

Debian is now working on the NVIDIA Jetson TX1 developer kit, a
development board based on the Tegra X1 chip (Tegra 210), a 64-bit ARM
chip.

We have a pre-built u-boot image in Debian as well as kernel and
installer support.  There are some minor kernel glitches but NVIDIA
is very active upstream and I hope they'll get resolved soon.

The Jetson TX1 developer kit makes a pretty good 64-bit ARM development
platform.  The board is supported in mainline u-boot and the mainline
kernel and NVIDIA are pretty responsive to bug reports.  Unfortunately,
a proprietary blob is required for USB (and Ethernet is connected via
USB).

If you're interested in a good 64-bit ARM development platform, give
[Debian on the Jetson
TX1 development kit](https://wiki.debian.org/InstallingDebianOn/NVIDIA/Jetson-TX1)
a try.

