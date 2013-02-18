---
title: Tips and tricks for Debian on QNAP TS-21x
nav: Tips
description: Tips and tricks for Debian on QNAP TS-21x
keywords: [Debian, QNAP, TS-210, TS-212, TS-219, TS-219P, tips, tricks]
---

<% content_for :right do %>
<img src = "../images/r_ts219p.jpg" class="border" alt="Open QNAP TS-219" width="148" height="188" />

<%= render "adsense-wideskyscaper-right" %>
<% end %>

<h1>Tips and tricks for Debian on QNAP TS-21x</h1>

Here are some tips and tricks about running Debian on the QNAP TS-21x.

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

<h2>Disk order on the QNAP TS-219P</h2>

One note for Debian users on the TS-219P (this note does not apply to
TS-210 and TS-219): when you use the QNAP firmware, the disk on the left is
HDD1 whereas the disk on the right is HDD2.  However, on Debian it is the
other way around (HDD1 is on the right, HDD2 is on the left).  This doesn't
really matter since Debian uses unique IDs (UUIDs) to refer to partitions,
but don't be surprised when the "HDD2" light goes on when you access the
first disk.

<div class="bbf">
<%= render "adsense-banner-before-footer" %>
</div>

