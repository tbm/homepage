---
title: De-installing Debian on the Thecus N2100
nav: De-installing Debian
description: Restoring the original Thecus firmware on the Thecus N2100
keywords: [Debian, Thecus, N2100, original firmware, guide]
---

<% content_for :right do %>
<img src = "../images/r_n2100.jpg" class="border" alt="Thecus N2100" width="141" height="148" />

<%= render "adsense-wideskyscaper-right" %>
<% end %>

<h1>De-installing Debian</h1>

If you need to restore the original Thecus firmware for some reason, you
can follow the instructions below.  Please note that this will only work if
your Debian system is still working.  If Debian is broken but the machine
itself works, it is possible to restore the original firmware from within
RedBoot, either by using <a href = "../telnet/">telnet to RedBoot</a> or a
serial console.

First of all, you need to get a copy of the N2100 firmware.  If you don't
have your copy anymore, you can download it from <a href =
"http://www.thecus.com/dl.php">Thecus firmware site</a>.  Once you have the
`.bin` file, you need to decrypt and unpack it.  For this, you need to have
the `openssl` package installed.

<div class="code">
<pre>
openssl enc -d -des -in N2100_FW_2.01.10.bin -out upgrade.tar.gz \
 -K 7A9816A4C275D557 -iv 0 -nosalt -nopad
tar -xzpf upgrade.tar.gz
</pre>
</div>

You can ignore the warning from gzip and error from tar that the last
command will show.  You will now have several files in the `upgrade`
directory.  For us, only the files `ramdisk.arm` and `zImage` are of
interest.  You need to write these files to MTD flash, which is quite
simple.  First, check the file `/proc/mtd` and look which MTD partition is
associated with the ramdisk and the kernel.  This should be mtd1 and mtd2
respectively but please check `/proc/mtd` to ensure that this is the same
on your machine.  Then write the files to these partitions.

<div class="code">
<pre>
cat ramdisk.arm &gt; /dev/mtdblock1
cat zImage &gt; /dev/mtdblock2
</pre>
</div>

When you reboot your machine, the original Thecus firmware will start.  Now
you should check if there's a new Thecus firmware available and if so
upgrade to the latest firmware using the Thecus upgrade procedure.

