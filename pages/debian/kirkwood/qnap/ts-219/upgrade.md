---
title: Debian on QNAP TS-21x/TS-22x
nav: Upgrade
description: Debian on TS-21x/TS-22x
keywords: [Debian, QNAP, TS-210, TS-212, TS-219, TS-220, TS-221, support, status, buster, bullseye]
---

<div class="right">
<img src = "../images/r_ts219p.jpg" class="border" alt="Open QNAP TS-219" width="148" height="188" />
</div>

Debian 10 (buster) is the last release to support QNAP TS-21x/TS-22x
devices.  These devices are not supported in Debian 11 (bullseye).

The reason is that the Linux kernel no longer fits into flash memory.
These QNAP devices boot from a 16 MB flash chip.  During the installation
of Debian, we put the Linux kernel and a ramdisk (initramfs) into flash
which in turn loads Debian from disk.  Unfortunately, there's only
2 MB allocated for the kernel partition in flash, which is not enough
to store a modern version of the Linux kernel.

Support for QNAP TS-21x/TS-22x was dropped from Debian 11 (bullseye)
because of this limitation.

If you're running Debian on your QNAP TS-21x/TS-22x device, you have
several options:

1. Stay on Debian 10.  This release will be supported until [around August 2022](https://wiki.debian.org/DebianReleases).
2. Upgrade to Debian 11 while keeping the kernel from Debian 10.  Please
   see the [release notes](https://www.debian.org/releases/stable/armel/release-notes/ch-information.en.html#no-longer-supported-hardware)
   for instructions.
3. Change the flash partition layout.  Arnaud Mouiche has [created a script](https://github.com/amouiche/qnap_mtd_resize_for_bullseye) that re-configures the partition layout.

