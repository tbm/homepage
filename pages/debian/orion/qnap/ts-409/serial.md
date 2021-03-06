---
title: Serial console for QNAP TS-409
nav: Serial Console
description: Connecting a serial console to the QNAP TS-409
keywords: [Debian, QNAP, TS-409, serial, console, RS-232, hack]
---

If you want to connect a serial console to the QNAP TS-409, you'll need a
3.3V TTL to RS-232 level shifter.  The serial connector is marked as CN9 on
the board and is a connector of type JST PHR-4.  The pin layout is as
follows from left to right:

<ul>
<li>GND (white)</li>
<li>RX (black)</li>
<li>VCC (green)</li>
<li>TX (red)</li>
</ul>

<img src = "../images/img_0108s.jpg" class="border" alt = "TS-409 and serial console" width="640" height="480" />

Note that you have to void your warranty in order to access the serial
console on the TS-409U.

Once you have connected your serial console, you can use a terminal
emulation program to connect to U-Boot, the boot loader used by this
device.  You have to connect with 115200 baud and set the parameters to 8N1
(8 data bits, no parity, 1 stop bit).  U-Boot on a <a href =
"../uboot/">separate page about U-Boot</a>.

If your serial console doesn't work or you can see text but your typing is
ignored, it might be because you have to connect RX from your connector
cable to TX on the QNAP and TX with RX.

