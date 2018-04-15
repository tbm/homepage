---
title: FAQ about Debian on QNAP TS-209
nav: FAQ
description: FAQ about Debian on QNAP TS-209
keywords: [Debian, QNAP, TS-209, FAQ, frequently asked questions, help, troubleshooting]
---

<div class="right">
<img src = "../images/r_ts209_front.jpg" class="border" alt="QNAP TS-209 from the front" width="148" height="97" />
</div>

<h3>Is Debian on the QNAP TS-209 fully supported?</h3>

Debian 9 (stretch) includes support for the QNAP TS-209.  However, please
note that Debian 9 will be the last release to support this device.

<h3>Is Debian on the TS-209 suited for people new to Linux?</h3>

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

<h3>Will this installer work on the TS-209 and the TS-209 Pro?</h3>

Yes, the only difference between the TS-209 and the TS-209 Pro is the
software that is included in the QNAP firmware.  Since the installation of
Debian will replace the QNAP firmware, this difference in software won't
matter.

<h3>Will this installer work on the TS-209 II?</h3>

Yes, the TS-209 II is exactly the same as the TS-209 with the exception
that it has more RAM.  The same applies to TS-209 Pro and TS-209 Pro II.

<h3>Will this installer work on the QNAP TS-101 or TS-201?</h3>

No, the TS-101 and TS-201 are based on a PowerPC chip.  This installation
routine will only work on Orion based QNAP devices.  This include the <a
href = "../../ts-109/">TS-109</a>, <a href = "../../ts-209/">TS-209</a>, <a
href = "../../ts-409/">TS-409</a> and variants thereof.

<h3>Will this installer work on the QNAP TS-509?</h3>

No, the QNAP TS-509 is based on an Intel Celeron chip and therefore not
compatible with this installation routine which only supports QNAP devices
based on Marvell's Orion (ARM) chip.

<h3>Is there a recovery mode?</h3>

Yes, the TS-209 has a recovery mode with which a firmware image can be
written to flash.  This is useful in case there are problems during the
installation or an upgrade of Debian.  See the <a href =
"../recovery/">recovery mode</a> page for more information.

<h3>Is the serial header soldered onto the board already?</h3>

Yes, a serial header is on the main board.  You only need to prepare a
cable with a TTL level shifter for a <a href = "../serial/">serial
console</a>.

<h3>Will I need a serial console to use Debian?</h3>

No, the installation and operation of Debian on your QNAP doesn't require a
serial console.

Go back to my <a href = "..">Debian on QNAP TS-209</a> page.

