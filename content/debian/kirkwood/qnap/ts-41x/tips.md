---
title: Tips and tricks for Debian on QNAP TS-41x
nav: Tips
description: Tips and tricks for Debian on the QNAP TS-41x
keywords: [Debian, QNAP, TS-410, TS-410U, TS-412, TS-419P, TS-419U, tips, tricks]
---

<% content_for :right do %>
<img src = "../images/r_qnap_ts419p.jpg" class="border" alt="QNAP TS-419P from the front" width="148" height="148" />

<%= render "adsense-wideskyscaper-right" %>
<% end %>

<h1>Tips and tricks for Debian on the QNAP TS-410, TS-410U, TS-412, TS-419P, TS-419P+ and TS-419U</h1>

Here are some tips and tricks about running Debian on the QNAP TS-41x.

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

