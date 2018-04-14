---
title: De-installing Debian on the QNAP TS-209
nav: De-installing Debian
description: Restoring the original QNAP Firmware on the QNAP TS-209
keywords: [Debian, QNAP, TS-209, original firmware]
---

<h1>Restoring the original QNAP firmware</h1>

If you want to restore the original QNAP firmware for some reason, you can
follow the instructions below.  Please note that this will only work if
your Debian system is still working.  If your Debian system is broken but
the machine itself works, you can use the <a href = "../recovery/">recovery
mode</a> to restore the QNAP firmware.

There are two steps to restore the original QNAP firmware.  First, you have
to put the backup of the flash partitions from the QNAP firmware you made
<a href = "../install/">before the installation of Debian</a> into flash.

<div class="code">
<pre>
cat mtd1 &gt; /dev/mtdblock1
cat mtd2 &gt; /dev/mtdblock2
</pre>
</div>

Second, you have to restart your QNAP, and then run QNAP Finder to install
the QNAP software again.  The second step is needed because the QNAP
software is stored both in flash and on the hard drive and Debian removed
the QNAP software when it formatted the disk.

After you put the QNAP firmware back in flash and installed the complete
the QNAP software with QNAP Finder, your device will run the original
software from QNAP again.

