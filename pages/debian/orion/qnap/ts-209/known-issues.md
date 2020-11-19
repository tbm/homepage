---
title: Known issues of Debian on QNAP TS-209
nav: Known issues
keywords: [Debian, QNAP, TS-209, bugs, issues, defects]
---

<div class="right">
<img src = "../images/r_ts209_front.jpg" class="border" alt="QNAP TS-209 from the front" width="148" height="97" />
</div>

Here is a list of known issues and bugs with Debian on the QNAP TS-209:

* The installer fails to make the system bootable, especially on
configurations with LVM and RAID.  You can [apply a
workaround](../troubleshooting/#bootable).
* qcontrol (the tool to control LEDs and beeper) [doesn't work](http://bugs.debian.org/933294).
* The Linux kernel in Debian 10 [fails to boot](https://bugs.debian.org/908712).  **Do not upgrade to Debian 10 (buster) until this issue is resolved!**  The issue will be resolved in Debian 10.7 on 2020-12-05.
* Debian 10 (buster) is the last release to support this device.  There's no support in Debian 11 (bullseye).

