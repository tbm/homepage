---
title: FAQ about Debian on QNAP TS-41x/TS-42x
nav: FAQ
description: FAQ about Debian on QNAP TS-41x/TS-42x
keywords: [Debian, QNAP, TS-410, TS-410U, TS-412, TS-419P, TS-419P II, TS-419U, TS-420, TS-421, FAQ, frequently asked questions, help, troubleshooting]
---

<% content_for :right do %>
<img src = "../images/r_qnap_ts419p.jpg" class="border" alt="QNAP TS-419P from the front" width="148" height="148" />

<%= render "adsense-wideskyscaper-right" %>
<% end %>

<h1>Frequently Asked Questions (FAQ)</h1>

<h3>Is Debian on the QNAP TS-410, TS-410U, TS-412, TS-419P, TS-419P+, TS-419P II, TS-419U, TS-419U+, TS-420 and TS-421 fully supported?</h3>

Debian includes support for the QNAP TS-410, TS-410U, TS-412, TS-419P,
TS-419P+, TS-419P II, TS-419U, TS-419U+, TS-420 and TS-421.  However, some
functionality from the original firmware may not be available.  For
example, Wake-on-LAN (WOL) is not supported.  Please see the <a href =
"../status/">status page</a> to see what is supported.

<h3>Which QNAP devices are supported?</h3>

All QNAP devices based on the Marvell Kirkwood platform are supported.
This includes the <a href = "../../ts-119/">QNAP TS-110, TS-112, TS-119,
TS-119P+, TS-119P II, TS-120 and TS-121</a>, <a href = "../../ts-219/">QNAP TS-210, TS-219,
TS-219P, TS-219P+, TS-219P II, TS-220 and TS-221</a> as well as the QNAP TS-410, TS-410U,
TS-412, TS-419P, TS-419P+, TS-419P II, TS-419U, TS-419U+, TS-420 and TS-421.  Older QNAP devices based
on the Marvell Orion platform are <a href = "/debian/orion/qnap/">also
supported</a>.  I don't support any other QNAP devices, but you may find
information and help <a href =
"http://forum.qnap.com/viewforum.php?f=147">on the QNAP forum</a>.

<h3>Is Debian on QNAP suited for people new to Linux?</h3>

No, I would not recommend you install Debian on your QNAP if you don't have
any experience with Linux and Debian.  Debian will not install a web
interface through which you can control your QNAP, so I recommend you stay
with the QNAP firmware.

<h3>Can I have both the QNAP firmware and Debian?</h3>

No, Debian will completely replace the QNAP firmware on disk and in flash.
You have to choose between the QNAP firmware and the Debian installation
described on my pages.  However, it would be possible to make a small
Debian system on your disk with the QNAP firmware by using `debootstrap`
and `chroot`.

<h3>Can I go back to the QNAP firmware if I don't like Debian?</h3>

Yes, you can <a href = "../deinstall/">restore the original QNAP
software</a> without any problems.

<h3>Is there a recovery mode?</h3>

Yes, the TS-41x/TS-42x devices all have a recovery mode with which a firmware
image can be written to flash.  This is useful in case there are problems
during the installation or an upgrade of Debian.  See the <a href =
"../recovery/">recovery mode</a> page for more information.

<h3>Is the serial header soldered onto the board already?</h3>

Yes, a serial header is on the main board.  You only need to prepare a
cable with a TTL level shifter for a <a href = "../serial/">serial
console</a>.

<h3>Will I need a serial console to use Debian?</h3>

No, the installation and operation of Debian on your QNAP doesn't require a
serial console.

Go back to my <a href = "..">Debian on QNAP TS-41x/TS-42x</a> page.

<div class="bbf">
<%= render "adsense-banner-before-footer" %>
</div>

