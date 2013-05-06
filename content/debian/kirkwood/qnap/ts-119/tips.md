---
title: Tips and tricks for Debian on QNAP TS-11x
nav: Tips
description: Tips and tricks for Debian on QNAP TS-11x
keywords: [Debian, QNAP, TS-110, TS-112, TS-119, tips, tricks]
---

<% content_for :right do %>
<img src = "../images/r_qnap_ts110.jpg" class="border" alt="QNAP TS-110 from the front" width="148" height="206" />

<%= render "adsense-wideskyscaper-right" %>
<% end %>

<h1>Tips and tricks for Debian on QNAP TS-11x</h1>

Here are some tips and tricks about running Debian on the QNAP TS-11x.

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

<h2><a id="autopower">Automatic power on</a></h2>

QNAP machines can turn on automatically when power is applied if the device
was not powered down correctly.  This is helpful when your power goes down.
In order to enable this feature, run the following command:

<div class="code">
<pre>
qcontrol --direct autopower on
</pre>
</div>

<div class="bbf">
<%= render "adsense-banner-before-footer" %>
</div>

