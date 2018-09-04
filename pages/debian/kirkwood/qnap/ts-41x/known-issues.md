---
title: Known issues of Debian on QNAP TS-41x/TS-42x
nav: Known issues
keywords: [Debian, QNAP, TS-410, TS-410U, TS-412, TS-419P, TS-419U, TS-420, TS-421, bugs, issues, defects]
---

<div class="right">
<img src = "../images/r_qnap_ts419p.jpg" class="border" alt="QNAP TS-419P from the front" width="148" height="148" />
</div>

Here is a list of known issues and bugs with Debian on QNAP TS-41x/TS-42x:

* On QNAP devices with 1 GB of RAM (i.e. TS-420U, TS-421 and TS-421U), the
installer fails because of a kernel issue.  Messages in `dmesg` include
`BUG: Bad rss-counter state` and `Unhandled fault: external abort on
linefetch`.  You have two options: 1) stay with Debian jessie, or 2) [set
the RAM size to 768 MB](https://blog.spblinux.de/2018/09/debian-with-btrfs-on-qnap-11x-21x-kirkwood/).

