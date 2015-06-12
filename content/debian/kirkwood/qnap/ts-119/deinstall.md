---
title: De-installing Debian on QNAP TS-11x/TS-12x
nav: De-installing Debian
description: Restoring the original QNAP firmware or re-installing Debian on QNAP TS-11x/TS-12x
keywords: [Debian, QNAP, TS-110, TS-112, TS-112P, TS-119, TS-120, TS-121, original firmware]
---

<% content_for :right do %>
<%= render "adsense-wideskyscaper-right" %>
<% end %>

<h1>Restoring the original QNAP firmware or re-installing Debian</h1>

If you want to restore the original QNAP firmware or re-install Debian on your TS-11x/TS-12x device for
some reason, you can follow the instructions below.  Please note that this
will only work if your Debian system is still working.  If your Debian
system is broken but the machine itself works, you can use the <a href =
"../recovery/">recovery mode</a> to restore the QNAP firmware or
re-install Debian.

<h2>Restoring the original QNAP firmware</h2>

There are two steps to restore the original QNAP firmware.  First, you have
to put the backup of the flash partitions from the QNAP firmware you made
<a href = "../install/">before the installation of Debian</a> into flash.

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

<h2><a id="reinstall">Re-installing Debian</a></h2>

If you want to re-install Debian using Debian installer, you have to obtain
the <a
href="http://ftp.debian.org/debian/dists/stable/main/installer-armel/current/images/kirkwood/network-console/qnap/ts-119/kernel">kernel</a>
and <a
href="http://ftp.debian.org/debian/dists/stable/main/installer-armel/current/images/kirkwood/network-console/qnap/ts-119/initrd.gz">initrd.gz</a>
files of the installer (make sure the initrd.gz does not get uncompressed
when you download it).

You can then write the installer files to flash:

<div class="code">
<pre>
cat kernel &gt; /dev/mtdblock1
cat initrd.gz &gt; /dev/mtdblock2
</pre>
</div>

Reboot your QNAP device and Debian installer will start and you can connect
via SSH, as <a href="../install/#install">documented on the install
page</a>.  Please be aware that the SSH key of the machine will have
changed.

<div class="bbf">
<%= render "adsense-banner-before-footer" %>
</div>

