---
title: Known issues of Debian on QNAP TS-11x/TS-12x
nav: Known issues
keywords: [Debian, QNAP, TS-110, TS-112, TS-112P, TS-119, TS-119P+, TS-120, TS-121, bugs, issues, defects]
---

<div class="right">
<img src = "../images/r_qnap_ts110.jpg" class="border" alt="QNAP TS-110 from the front" width="148" height="206" />
</div>

Here is a list of known issues and bugs with Debian on QNAP TS-11x/TS-12x:

* On QNAP devices with 1 GB of RAM (i.e. TS-121), the installer fails
because of a kernel issue.  Messages in `dmesg` include `BUG: Bad
rss-counter state` and `Unhandled fault: external abort on linefetch`.
You can [set the RAM size to 768 MB](../mem-768m/) as a workaround.

* The initramfs might not fit in flash.  You can try to [use XZ
compression to make it fit](../troubleshooting/#ramdisk-space).

* There are some reports that LED lights don't work correctly on some
QNAP models (they always show red).

* There are some reports that Wake-on-LAN (WOL) no longer works.

* There are [problems setting the clock (RTC)](https://lists.debian.org/debian-arm/2019/09/msg00023.html).

* Debian 10 (buster) is the last release to support this device.  There's no support in Debian 11 (bullseye).

