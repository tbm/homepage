---
title: Serial console for QNAP TS-109
nav: Serial Console
description: Connecting a serial console to the QNAP TS-109
keywords: [Debian, QNAP, TS-109, serial, console, RS-232, hack]
---

<% content_for :right do %>
<%= render "adsense-wideskyscaper-right" %>
<% end %>

<h1>Connecting a serial console to the QNAP TS-109</h1>

The serial port is a 2x3 pin connector (labelled JP1) that is located close
to the button on the left side on the front of the mainboard.  If you look
at the picture below, you'll see that the layout of the row closer to the
edge of the mainboard is N/C, N/C and 3.3V whereas that of the other row is
RX, TX and GND.  In the picture below, the red cable is 3.3V.

In order to connect to this serial port, you need a 3.3V TTL to RS-232
level shifter.  The serial connector on the TS-109 is the same as that of
the TS-101 which has a <a href =
"http://scratchpad.wikia.com/wiki/Open_Turbostation%3ASerialPort">page with
more information about the serial port</a> (please note though that the
connector has a different location on the TS-101).

<img src = "../images/img_0012s.jpg" class="border" alt = "TS-109 and serial console" width="640" height="480" />

Once you have connected your serial console, you can use a terminal
emulation program to connect to U-Boot, the boot loader used by this
device.  You have to connect with 115200 baud and set the parameters to 8N1
(8 data bits, no parity, 1 stop bit).  U-Boot on a <a href =
"../uboot/">separate page about U-Boot</a>.

<div class="bbf">
<%= render "adsense-banner-before-footer" %>
</div>

