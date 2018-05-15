---
title: Known issues of Debian on QNAP TS-11x/TS-12x
nav: Known issues
keywords: [Debian, QNAP, TS-110, TS-112, TS-112P, TS-119, TS-119P+, TS-120, TS-121, bugs, issues, defects]
---

<div class="right">
<img src = "../images/r_qnap_ts110.jpg" class="border" alt="QNAP TS-110 from the front" width="148" height="206" />
</div>

Here is a list of known issues and bugs with Debian on QNAP TS-11x/TS-12x:

* On some QNAP devices with a Kirkwood 6282 chip, the installer fails
because of a kernel issue.  Messages in `dmesg` include `BUG: Bad
rss-counter state` and `Unhandled fault: external abort on linefetch`.
Unfortunately, the Linux kernel developers [haven't been able to reproduce
this issue](https://lists.debian.org/debian-arm/2017/07/msg00051.html).
* On fanless QNAP systems (TS-119), [fan errors are
reported](http://bugs.debian.org/712841).  There is a [patch for this
issue](http://bugs.debian.org/712841#169).

