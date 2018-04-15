---
title: Restoring the original QNAP firmware or re-installing Debian
nav: De-installing Debian
description: Restoring the original QNAP firmware or re-installing Debian on the QNAP TS-41x/TS-42x
keywords: [Debian, QNAP, TS-410, TS-410U, TS-412, TS-419P, TS-419U, TS-420, TS-421, original firmware]
---

<div class="right">
<img src = "../images/r_qnap_ts419p.jpg" class="border" alt="QNAP TS-419P from the front" width="148" height="148" />
</div>

If you want to restore the original QNAP firmware or re-install Debian on your TS-41x or TS-42x
device for some reason, you can follow the
instructions below.  Please note that this will only work if your Debian
system is still working.  If your Debian system is broken but the machine
itself works, you can use the <a href = "../recovery/">recovery mode</a> to
restore the QNAP firmware or re-install Debian.

<h2>Restoring the original QNAP firmware</h2>

There are two steps to restore the original QNAP firmware.  First, you have
to put the backup of the flash partitions from the QNAP firmware you made
<a href = "../unpack/">before the installation of Debian</a> into flash.

<div class="code">
<pre>
cat mtd1 &gt; /dev/mtdblock1
cat mtd2 &gt; /dev/mtdblock2
</pre>
</div>

Second, you have to restart your QNAP, and then go to the web interface to
format your disk and install the full QNAP firmware.

After you put the QNAP firmware back in flash and installed the complete
the QNAP software, your device will run the original software from QNAP
again.

<h2 id="reinstall">Re-installing Debian</h2>

If you want to re-install Debian using Debian installer, you can put the
installer in flash and restart your device.

Since there are two different kernel variants for QNAP devices, you first
have to determine which variant you need.  You can do this by calling this
script:

<div class="code">
<pre>
/usr/share/flash-kernel/dtb-probe/kirkwood-qnap
</pre>
</div>

If the output is `kirkwood-ts419-6281.dtb`, you need the <a
href="http://ftp.debian.org/debian/dists/stretch/main/installer-armel/current/images/kirkwood/network-console/qnap/ts-41x/kernel-6281">kernel-6281</a>
file.  If the output is `kirkwood-ts419-6282.dtb`, you need the <a
href="http://ftp.debian.org/debian/dists/stretch/main/installer-armel/current/images/kirkwood/network-console/qnap/ts-41x/kernel-6282">kernel-6282</a>
file.

You also have to download the <a
href="http://ftp.debian.org/debian/dists/stretch/main/installer-armel/current/images/kirkwood/network-console/qnap/ts-41x/initrd">initrd</a>
files of the installer (make sure the initrd does not get uncompressed when
you download it).

You can now write the installer files to flash:

<div class="code">
<pre>
cat kernel-628<span class="input">x</span> &gt; /dev/mtdblock1
cat initrd &gt; /dev/mtdblock2
</pre>
</div>

Reboot your QNAP device and Debian installer will start and you can connect
via SSH, as <a href="../install/#install">documented on the install
page</a>.  Please be aware that the SSH key of the machine will have
changed.

