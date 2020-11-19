---
title: Known issues of Debian on QNAP TS-41x/TS-42x
nav: Known issues
keywords: [Debian, QNAP, TS-410, TS-410U, TS-412, TS-412U, TS-419P, TS-419U, TS-420, TS-421, bugs, issues, defects]
---

<div class="right">
<img src = "../images/r_qnap_ts419p.jpg" class="border" alt="QNAP TS-419P from the front" width="148" height="148" />
</div>

Here is a list of known issues and bugs with Debian on QNAP TS-41x/TS-42x:

* On QNAP devices with 1 GB of RAM (i.e. TS-420U, TS-421 and TS-421U), the
installer fails because of a kernel issue.  Messages in `dmesg` include
`BUG: Bad rss-counter state` and `Unhandled fault: external abort on
linefetch`.  You can [set the RAM size to 768 MB](../mem-768m/) as a
workaround.

* The initramfs might not fit in flash.  You can try to [use XZ
compression to make it fit](../troubleshooting/#ramdisk-space).

* There are some reports that LED lights don't work correctly on some
QNAP models (they always show red).

* There are some reports that Wake-on-LAN (WOL) no longer works.

* There are [problems setting the clock (RTC)](https://lists.debian.org/debian-arm/2019/09/msg00023.html).

* Debian 10 (buster) is the last release to support this device.  There's no support in Debian 11 (bullseye).

