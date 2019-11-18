---
title: Tips and tricks for Debian on QNAP TS-109
nav: Tips
description: Tips and tricks for Debian on QNAP TS-109
keywords: [Debian, QNAP, TS-109, tips, tricks]
---

<div class="right">
<img src = "../images/r_ts109_front.jpg" class="border" alt="QNAP TS-109 from the front" width="148" height="217" />
</div>

<h2 id="autopower">Automatic power on</h2>

QNAP machines can turn on automatically when power is applied if the device
was not powered down correctly.  This is helpful when your power goes down.
In order to enable this feature, run the following command:

<div class="code">
<pre>
sudo qcontrol --direct autopower on
</pre>
</div>

<h2 id="Fanless">qcontrol on fanless QNAP systems</h2>

On QNAP systems without fan (TS-109 and TS-109 II), fan errors will be
reported by qcontrol because it tries to regulate the fan and fails.

To avoid these errors, edit the qcontrol config file `/etc/qcontrol.conf`
and change:

<div class="code">
<pre>
has_fan = true
</pre>
</div>

to:

<div class="code">
<pre>
has_fan = false
</pre>
</div>

Restart qcontrol:

<div class="code">
<pre>
sudo systemctl restart qcontrol.service qcontrold.service
</pre>
</div>

