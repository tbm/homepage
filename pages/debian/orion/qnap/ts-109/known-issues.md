---
title: Known issues of Debian on QNAP TS-109
nav: Known issues
keywords: [Debian, QNAP, TS-109, bugs, issues, defects]
---

<div class="right">
<img src = "../images/r_ts109_front.jpg" class="border" alt="QNAP TS-109 from the front" width="148" height="217" />
</div>

Here is a list of known issues and bugs with Debian on the QNAP TS-109:

## Installation

* The installer fails to make the system bootable, especially on
configurations with LVM and RAID.  You can [apply a
workaround](../troubleshooting/#bootable) for RAID, but installation
with LVM are not possible.

## Upgrades

* Upgrades may fail because the initramfs doesn't fit in flash.  If you
use LVM, it's best to stay on Debian 9 (stretch) as there's no solution
or workaround.  If you don't use LVM, you can [apply a workaround](../troubleshooting/#ramdisk).

## General operations

* qcontrol (the tool to control LEDs and beeper) [doesn't work](http://bugs.debian.org/933294).

## Support

* Debian 10 (buster) is the last release to <a href="../upgrade">support this device</a>.  There's no support in Debian 11 (bullseye).

