---
title: Serial console for Kurobox Pro
nav: Serial Console
description: Connecting a serial console to the Kurobox Pro
keywords: [Debian, Buffalo, Kurobox Pro, serial, console, RS-232]
---

<% content_for :right do %>
<img src = "../images/r_kuroboxpro_front.jpg" class="border" alt="Kurobox Pro from the front" width="148" height="231" />

<%= render "adsense-wideskyscaper-right" %>
<% end %>

<h1>Connecting a serial console to the Kurobox Pro</h1>

You have to solder a 4 pin connector to the daughter board of the Kurobox
Pro labelled as UART0.  The pin layout is described on the board.  In order
to connect to this serial port, you need a 3.3V TTL to RS-232 level shifter.

<img src = "../images/img_0037s.jpg" class="border" alt = "Kurobox Pro and serial console" width="547" height="402" />

<div class="bbf">
<%= render "adsense-banner-before-footer" %>
</div>

