---
title: De-installing Debian on the QNAP TS-41x
nav: De-installing Debian
description: Restoring the original QNAP Firmware on the QNAP TS-41x
keywords: [Debian, QNAP, TS-410, TS-410U, TS-412, TS-419P, TS-419U, original firmware]
---

<% content_for :right do %>
<img src = "../images/r_qnap_ts419p.jpg" class="border" alt="QNAP TS-419P from the front" width="148" height="148" />

<%= render "adsense-wideskyscaper-right" %>
<% end %>

<h1>Restoring the original QNAP firmware</h1>

If you want to restore the original QNAP firmware on your TS-410, TS-410U,
TS-412, TS-419P, TS-419P+ or TS-419U for some reason, you can follow the
instructions below.  Please note that this will only work if your Debian
system is still working.  If your Debian system is broken but the machine
itself works, you can use the <a href = "../recovery/">recovery mode</a> to
restore the QNAP firmware.

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

<div class="bbf">
<%= render "adsense-banner-before-footer" %>
</div>

