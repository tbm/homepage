---
title: Known issues of Debian on QNAP TS-41x/TS-42x
nav: Known issues
keywords: [Debian, QNAP, TS-410, TS-410U, TS-412, TS-419P, TS-419U, TS-420, TS-421, bugs, issues, defects]
---

<div class="right">
<img src = "../images/r_qnap_ts419p.jpg" class="border" alt="QNAP TS-419P from the front" width="148" height="148" />
</div>

Here is a list of known issues and bugs with Debian on QNAP TS-41x/TS-42x:

* On some QNAP devices with a Kirkwood 6282 chip, the installer fails
because of a kernel issue.  Messages in `dmesg` include `BUG: Bad
rss-counter state` and `Unhandled fault: external abort on linefetch`.
Unfortunately, the Linux kernel developers [haven't been able to reproduce
this issue](https://lists.debian.org/debian-arm/2017/07/msg00051.html).

