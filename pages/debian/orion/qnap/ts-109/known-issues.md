---
title: Known issues of Debian on QNAP TS-109
nav: Known issues
keywords: [Debian, QNAP, TS-109, bugs, issues, defects]
---

<div class="right">
<img src = "../images/r_ts109_front.jpg" class="border" alt="QNAP TS-109 from the front" width="148" height="217" />
</div>

Here is a list of known issues and bugs with Debian on the QNAP TS-109:

* The installer fails to make the system bootable, especially on
configurations with LVM and RAID.  You can [apply a
workaround](../troubleshooting/#bootable).
* qcontrol (the tool to control LEDs and beeper) doesn't work.
* On fanless QNAP systems (TS-109 and TS-109 II), [fan errors are
reported](http://bugs.debian.org/712841).  There is a [patch for this
issue](http://bugs.debian.org/712841#169).

