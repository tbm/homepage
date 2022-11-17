---
title: Debian on QNAP TS-41x/TS-42x
nav: Upgrade
description: Debian on QNAP TS-41x/TS-42x
keywords: [Debian, QNAP, support, status, buster, bullseye]
---

<div class="right">
<img src = "../images/r_qnap_ts419p.jpg" class="border" alt="QNAP TS-419P from the front" width="148" height="148" />
</div>

Debian 10 (buster) was the last release to support QNAP TS-41x/TS-42x
devices.  These devices are not supported in Debian 11 (bullseye).

The reason is that the Linux kernel no longer fits into flash memory.
These QNAP devices boot from a 16 MB flash chip.  During the installation
of Debian, we put the Linux kernel and a ramdisk (initramfs) into flash
which in turn loads Debian from disk.  Unfortunately, there's only
2 MB allocated for the kernel partition in flash, which is not enough
to store a modern version of the Linux kernel.

Support for QNAP TS-41x/TS-42x was dropped from Debian 11 (bullseye)
because of this limitation.

If you're running Debian on your QNAP TS-41x/TS-42x device, you have
several options:

1. Stay on Debian 10.  Please note that security support [stopped in September 2022](https://www.debian.org/News/2022/20220910).
2. Upgrade to Debian 11 while keeping the kernel from Debian 10.  Please
   see the [release notes](https://www.debian.org/releases/stable/armel/release-notes/ch-information.en.html#no-longer-supported-hardware)
   for instructions.
3. Change the flash partition layout.  Arnaud Mouiche has [created a script](https://github.com/amouiche/qnap_mtd_resize_for_bullseye) that re-configures the partition layout.

My recommendation is for the third option: Arnaud Mouiche's method has been used by many users with success.

