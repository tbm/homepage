---
title: Known issues of Debian on QNAP TS-21x/TS-22x
nav: Known issues
keywords: [Debian, QNAP, HS-210, TS-210, TS-212, TS-212-E, TS-212P, TS-219, TS-219P, TS-219P+, TS-220, TS-221, bugs, issues, defects]
---

<div class="right">
<img src = "../images/r_ts219p.jpg" class="border" alt="Open QNAP TS-219" width="148" height="188" />
</div>

Here is a list of known issues and bugs with Debian on QNAP TS-21x/TS-22x:

* On QNAP devices with 1 GB of RAM (i.e. TS-221), the installer fails
because of a kernel issue.  Messages in `dmesg` include `BUG: Bad
rss-counter state` and `Unhandled fault: external abort on linefetch`.
You have two options: 1) stay with Debian jessie, or 2) [set the RAM
size to 768 MB](https://blog.spblinux.de/2018/09/debian-with-btrfs-on-qnap-11x-21x-kirkwood/).

