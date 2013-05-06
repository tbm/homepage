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
qcontrol --direct fanspeed # To see all valid speed settings
qcontrol --direct fanspeed medium
</pre>
</div>

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

