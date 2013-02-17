---
title: Serial console for QNAP TS-41x
nav: Serial Console
description: Connecting a serial console to the QNAP TS-41x
keywords: [Debian, QNAP, TS-410, TS-410U, TS-412, TS-419P, TS-419U, serial, console, RS-232, hack]
---

<% content_for :right do %>
<img src = "../images/r_qnap_ts419p.jpg" class="border" alt="QNAP TS-419P from the front" width="148" height="148" />

<%= render 'adsense-wideskyscaper-right' %>
<% end %>

<h1>Connecting a serial console to the QNAP TS-410, TS-410U, TS-412, TS-419P, TS-419P+ and TS-419U</h1>

If you want to connect a serial console to the QNAP TS-41x, you'll need a
3.3V TTL to RS-232 level shifter.  The serial connector is marked as CN1
and is of type JST PHR-4.  The pin layout is as follows (from the top to
the bottom):

<ul>
<li>TX</li>
<li>VCC</li>
<li>RX</li>
<li>GND</li>
</ul>

Note that you have to add a jumper to JP1 for the serial to work.  On the
TS-419P and TS-419P+, the LCD cannot be used when the JP1 jumper is set
(i.e. the jumper selects between the serial console and the LCD).  You also
have to disconnect the LCD cable that goes to the connector right next to
the serial connector.

Once you have connected your serial console, you can use a terminal
emulation program to connect to U-Boot, the boot loader used by this
device.  You have to connect with 115200 baud and set the parameters to 8N1
(8 data bits, no parity, 1 stop bit).  U-Boot on a <a href =
"../uboot">separate page about U-Boot</a>.

<div class="bbf">
<%= render 'adsense-banner-before-footer' %>
</div>

