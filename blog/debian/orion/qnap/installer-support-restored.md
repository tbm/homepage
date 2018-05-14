---
title: "QNAP TS-x09 installer available again"
date: 2016-01-23 18:30:27 -0800
---

Debian 8.3 [came out today](https://www.debian.org/News/2016/20160123).
As part of this update, Debian installer images for QNAP TS-109, TS-209
and TS-409 are available again.  These devices are pretty old but there
are still some users.  We dropped installer support several years ago
because the installer ramdisk was too large to fit in flash.  Since then,
users had to install Debian 6.0 (squeeze) and upgrade from there.  When
squeeze was removed from the Debian mirrors recently, I received mail from
a number of users.

I investigated a bit and found out that we can bring back the installer
thanks to XZ compression and some other changes.  The installer is
available for jessie and stretch.

