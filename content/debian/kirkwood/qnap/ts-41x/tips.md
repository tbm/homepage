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

Debian 7.0 doesn't have automatic support for the fan.  While there
is a tool that can control the fan, it won't automatically set its speeds
according to the temperature.  If you want to manually control the fan, do
this:

<div class="code">
<pre>
qcontrol --direct fanspeed # To see all valid speed settings
qcontrol --direct fanspeed medium
</pre>
</div>

<h2><a id="wakealarm">Scheduled power</a></h2>

You can tell your QNAP device to power on at a specific time using the
`wakealarm` system.  For example, if you want your QNAP to power on in 5
minutes, issue the following commands and turn off your device:

<div class="code">
<pre>
echo 0 > /sys/class/rtc/rtc0/wakealarm
echo `date '+%s' -d '+ 5 minutes'` > /sys/class/rtc/rtc0/wakealarm
</pre>
</div>

You can check check whether a wakealarm has been configured with:

<div class="code">
<pre>
cat /proc/driver/rtc
</pre>
</div>

Look for `alrm_time` and `and alrm_date`.

<div class="bbf">
<%= render "adsense-banner-before-footer" %>
</div>

