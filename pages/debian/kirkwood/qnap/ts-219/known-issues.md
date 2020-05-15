---
title: Known issues of Debian on QNAP TS-21x/TS-22x
nav: Known issues
keywords: [Debian, QNAP, HS-210, TS-210, TS-212, TS-212-E, TS-212P, TS-219, TS-219P, TS-219P+, TS-220, TS-221, Fujitsu, Q703, bugs, issues, defects]
---

<div class="right">
<img src = "../images/r_ts219p.jpg" class="border" alt="Open QNAP TS-219" width="148" height="188" />
</div>

Here is a list of known issues and bugs with Debian on QNAP TS-21x/TS-22x:

* On devices with 1 GB of RAM (i.e. QNAP TS-221 and Fujitsu Q703), the installer fails
because of a kernel issue.  Messages in `dmesg` include `BUG: Bad
rss-counter state` and `Unhandled fault: external abort on linefetch`.
You can [set the RAM size to 768 MB](../mem-768m/) as a workaround.

* The initramfs might not fit in flash.  You can try to [use XZ
compression to make it fit](../troubleshooting/#ramdisk-space).

* There are some reports that LED lights don't work correctly on some
QNAP models (they always show red).

* There are some reports that Wake-on-LAN (WOL) no longer works.

* There are [problems setting the clock (RTC)](https://lists.debian.org/debian-arm/2019/09/msg00023.html).

