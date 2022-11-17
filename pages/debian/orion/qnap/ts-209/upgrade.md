---
title: Debian on QNAP TS-209
nav: Upgrade
description: Debian on QNAP TS-209
keywords: [Debian, QNAP, support, status, buster, bullseye]
---

<div class="right">
<img src = "../images/r_ts209_front.jpg" class="border" alt="QNAP TS-209 from the front" width="148" height="97" />
</div>

Debian 10 (buster) was the last release to support QNAP TS-209 devices.
These devices are not supported in Debian 11 (bullseye).

The reason is that the Linux kernel no longer fits into flash memory.
These QNAP devices boot from a 8 MB flash chip.  During the installation
of Debian, we put the Linux kernel and a ramdisk (initramfs) into flash
which in turn loads Debian from disk.  Unfortunately, there's only
2 MB allocated for the kernel partition in flash, which is not enough
to store a modern version of the Linux kernel.

Support for QNAP TS-209 was dropped from Debian 11 (bullseye) because of
this limitation.

If you're running Debian on your QNAP TS-209 device, you have two
options:

1. Stay on Debian 10.  Please note that security support [stopped in September 2022](https://www.debian.org/News/2022/20220910).
2. Upgrade to Debian 11 while keeping the kernel from Debian 10.  Please
   see the [release notes](https://www.debian.org/releases/stable/armel/release-notes/ch-information.en.html#no-longer-supported-hardware)
   for instructions.

