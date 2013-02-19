---
title: Serial console for QNAP TS-11x
nav: Serial Console
description: Connecting a serial console to the QNAP TS-11x
keywords: [Debian, QNAP, TS-110, TS-112, TS-119, serial, console, RS-232, hack]
---

<% content_for :right do %>
<%= render "adsense-wideskyscaper-right" %>
<% end %>

<h1>Connecting a serial console to QNAP TS-11x devices</h1>

If you want to connect a serial console to a QNAP TS-11x device, you'll
need a 3.3V TTL to RS-232 level shifter.  The serial connector is of type
JST PHR-4 and the wires need to be crimped into a JST SPH-002T-P0.5S
connector pin before it can be fitted inside the JST PHR-4 connector.  The
pin layout is as follows from left to right:

<ul>
<li>GND (white)</li>
<li>RX (black)</li>
<li>VCC (green)</li>
<li>TX (red)</li>
</ul>

<img src = "../images/img_0004s.jpg" class="border" alt = "TS-219 and serial console" width="640" height="480" />

Once you have connected your serial console, you can use a terminal
emulation program to connect to U-Boot, the boot loader used by this
device.  You have to connect with 115200 baud and set the parameters to 8N1
(8 data bits, no parity, 1 stop bit).  U-Boot on a <a href =
"../uboot">separate page about U-Boot</a>.

<div class="bbf">
<%= render "adsense-banner-before-footer" %>
</div>
