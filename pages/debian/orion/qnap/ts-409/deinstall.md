---
title: Restoring the original QNAP firmware
nav: De-installing Debian
description: Restoring the original QNAP Firmware on the QNAP TS-409
keywords: [Debian, QNAP, TS-409, original firmware]
---

If you want to restore the original QNAP firmware for some reason, you can
follow the instructions below.  Please note that this will only work if
your Debian system is still working.  If your Debian system is broken but
the machine itself works, you can use the <a href = "../recovery/">recovery
mode</a> to restore the QNAP firmware.

First of all, you need a copy of the QNAP firmware.  If you made a copy
of the flash partitions from your QNAP device, copy the backup files `mtd1`
and `mtd2` to your QNAP device.  If you did not keep a copy, you can
[obtain an image of the firmware from QNAP](https://wiki.qnap.com/wiki/System_Recovery_Mode#Operating_Guideline_of_System_Recovery_Mode)
and extract the files manually (make sure you obtain the correct file
for your model):

<div class="code">
<pre>
wget http://download.qnap.com/Storage/tsd/<span class="input">flashimage/F_TS-409_20081024-2.1.2.zip</span>
sudo apt install unzip
unzip <span class="input">F_TS-409_20081024-2.1.2.zip</span>
dd if=<span class="input">F_TS-409_20081024-2.1.2.img</span> of=mtd1 bs=1M count=2
dd if=<span class="input">F_TS-409_20081024-2.1.2.img</span> of=mtd2 bs=1M skip=2 count=4
</pre>
</div>

There are two steps to restore the original QNAP firmware.  First, write
the QNAP firmware to flash:

<div class="code">
<pre>
sudo modprobe mtdblock
sudo dd if=mtd1 of=/dev/mtdblock1
sudo dd if=mtd2 of=/dev/mtdblock2
</pre>
</div>

Second, you have to restart your QNAP, and then run QNAP Finder to install
the QNAP software again.  The second step is needed because the QNAP
software is stored both in flash and on the hard drive and Debian removed
the QNAP software when it formatted the disk.

After you put the QNAP firmware back in flash and installed the complete
the QNAP software with QNAP Finder, your device will run the original
software from QNAP again.

