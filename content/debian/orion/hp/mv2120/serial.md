---
title: Serial console for HP mv2120
nav: Serial Console
description: Connecting a serial console to the HP mv2120
keywords: [Debian, HP, mv2120, mv5100, serial, console, RS-232]
---

<h1>Connecting a serial console to the HP mv2120</h1>

The serial port is a 2x5 pin connector (labelled CN4) that is located
behind the front cover.  The pin layout is shown in the picture below.  In
order to connect to this serial port, you need a 3.3V TTL to RS-232 level
shifter.

<img src = "../images/img_0202s.jpg" class="border" alt = "HP mv2120 and serial console" width="640" height="480" />

Please note that you can easily access the serial header without voiding
your warranty by taking off the front plane.  Once you have connected your
serial console, you can use a terminal emulation program to connect to
U-Boot, the boot loader used by this device.  You have to connect with
115200 baud and set the parameters to 8N1 (8 data bits, no parity, 1 stop
bit).

