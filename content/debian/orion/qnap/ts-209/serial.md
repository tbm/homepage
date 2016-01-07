---
title: Serial console for QNAP TS-209
nav: Serial Console
description: Connecting a serial console to the QNAP TS-209
keywords: [Debian, QNAP, TS-209, serial, console, RS-232, hack]
---

<h1>Connecting a serial console to the QNAP TS-209</h1>

The serial port is a 2x3 pin connector (labelled JP1) that is located close
to the button on the left side on the front of the mainboard.  The pin
layout of the row closer to the edge of the mainboard is 3.3V, N/C, N/C
whereas that of the second row is GND, TX, RX.  In the picture below, the
red cable is 3.3V.  In order to connect to this serial port, you need a
3.3V TTL to RS-232 level shifter.  The serial connector on the TS-209 is
the same as that of the TS-101 which has a <a href =
"http://scratchpad.wikia.com/wiki/Open_Turbostation:SerialPort">page with
more information about the serial port</a> (please note though that the
connector has a different location on the TS-101).

<img src = "../images/img_0008s.jpg" class="border" alt = "TS-209 and serial console" width="640" height="480" />

Please note that you can access the serial header without voiding your
warranty:

<img src = "../images/img_0006s.jpg" class="border" alt = "Access to the serial header" width="640" height="480" />

Once you have connected your serial console, you can use a terminal
emulation program to connect to U-Boot, the boot loader used by this
device.  You have to connect with 115200 baud and set the parameters to 8N1
(8 data bits, no parity, 1 stop bit).  U-Boot on a <a href =
"../uboot/">separate page about U-Boot</a>.

If your serial console doesn't work or you can see text but your typing is
ignored, it might be because you have to connect RX from your connector
cable to TX on the QNAP and TX with RX.

