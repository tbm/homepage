---
title: Known issues of Debian on QNAP TS-21x/TS-22x
nav: Known issues
keywords: [Debian, QNAP, HS-210, TS-210, TS-212, TS-212-E, TS-212P, TS-219, TS-219P, TS-219P+, TS-220, TS-221, bugs, issues, defects]
---

<div class="right">
<img src = "../images/r_ts219p.jpg" class="border" alt="Open QNAP TS-219" width="148" height="188" />
</div>

Here is a list of known issues and bugs with Debian on QNAP TS-21x/TS-22x:

* On some QNAP devices with a Kirkwood 6282 chip, the installer fails
because of a kernel issue.  Messages in `dmesg` include `BUG: Bad
rss-counter state` and `Unhandled fault: external abort on linefetch`.
Unfortunately, the Linux kernel developers [haven't been able to reproduce
this issue](https://lists.debian.org/debian-arm/2017/07/msg00051.html).
* On fanless QNAP systems (HS-210), [fan errors are
reported](http://bugs.debian.org/712841).  There is a [patch for this
issue](http://bugs.debian.org/712841#169).

