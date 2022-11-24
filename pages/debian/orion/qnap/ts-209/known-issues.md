---
title: Known issues of Debian on QNAP TS-209
nav: Known issues
keywords: [Debian, QNAP, TS-209, bugs, issues, defects]
---

<div class="right">
<img src = "../images/r_ts209_front.jpg" class="border" alt="QNAP TS-209 from the front" width="148" height="97" />
</div>

Here is a list of known issues and bugs with Debian on the QNAP TS-209:

## Installation

* The installer fails to make the system bootable, especially on
configurations with LVM or RAID.  If you don't use LVM or RAID, you can
[apply a workaround](../troubleshooting/#bootable).  Do not use LVM or
RAID!

## Upgrades

* Upgrades may fail because the initramfs doesn't fit in flash.  If you
use LVM or RAID, it's best to stay on Debian 9 (stretch) as there's no
solution or workaround.  If you don't use LVM or RAID, you can [apply a
workaround](../troubleshooting/#ramdisk).

## General operations

* qcontrol (the tool to control LEDs and beeper) [doesn't work](http://bugs.debian.org/933294).

## Support

* Debian 10 (buster) is the last release to <a href="../upgrade">support this device</a>.  There's no support in Debian 11 (bullseye).

