---
title: Tips and tricks for Debian on QNAP TS-409
nav: Tips
description: Tips and tricks for Debian on QNAP TS-409
keywords: [Debian, QNAP, TS-409, tips, tricks]
---

<% content_for :right do %>
<img src = "../images/r_ts409_front.jpg" class="border" alt="QNAP TS-409 from the front" width="148" height="147" />

<%= render "adsense-wideskyscaper-right" %>
<% end %>

<h1>Tips and tricks for Debian on the QNAP TS-409</h1>

Here are some tips and tricks about running Debian on the QNAP TS-409.

<h2>Controlling the fan</h2>

Debian currently doesn't have automatic support for the fan.  While there
is a tool that can control the fan, it won't automatically set its speeds
according to the temperature.  If you want to manually control the fan, do
this:

<div class="code">
<pre>
qcontrol -d &amp;
qcontrol fanspeed # To see all valid speed settings
qcontrol fanspeed medium
kill %1
rm /var/run/qcontrol.sock
</pre>
</div>

<div class="bbf">
<%= render "adsense-banner-before-footer" %>
</div>

