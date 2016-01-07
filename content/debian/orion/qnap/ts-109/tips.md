---
title: Tips and tricks for Debian on QNAP TS-109
nav: Tips
description: Tips and tricks for Debian on QNAP TS-109
keywords: [Debian, QNAP, TS-109, tips, tricks]
---

<% content_for :right do %>
<img src = "../images/r_ts109_front.jpg" class="border" alt="QNAP TS-109 from the front" width="148" height="217" />
<% end %>

<h1>Tips and tricks for Debian on the QNAP TS-109</h1>

<h2><a id="autopower">Automatic power on</a></h2>

QNAP machines can turn on automatically when power is applied if the device
was not powered down correctly.  This is helpful when your power goes down.
In order to enable this feature, run the following command:

<div class="code">
<pre>
qcontrol --direct autopower on
</pre>
</div>

