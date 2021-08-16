---
title: Known issues of Debian on QNAP TS-409
nav: Known issues
keywords: [Debian, QNAP, TS-409, bugs, issues, defects]
---

<div class="right">
<img src = "../images/r_ts409_front.jpg" class="border" alt="QNAP TS-409 from the front" width="148" height="147" />
</div>

Here is a list of known issues and bugs with Debian on the QNAP TS-409:

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

* There's a timing issue that will result in <a
href="http://comments.gmane.org/gmane.linux.ide/47799">not all disks being
recognized</a> in time on boot.  If you're experienced, you can <a
href="http://forum.qnap.com/viewtopic.php?p=284721#p284592">use a
workaround</a>.
* qcontrol (the tool to control LEDs and beeper) [doesn't work](http://bugs.debian.org/933294).

## Support

* Debian 10 (buster) is the last release to <a href="../upgrade">support this device</a>.  There's no support in Debian 11 (bullseye).

