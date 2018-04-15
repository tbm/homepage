---
title: Tips and tricks for Debian on QNAP TS-409
nav: Tips
description: Tips and tricks for Debian on QNAP TS-409
keywords: [Debian, QNAP, TS-409, tips, tricks]
---

<div class="right">
<img src = "../images/r_ts409_front.jpg" class="border" alt="QNAP TS-409 from the front" width="148" height="147" />
</div>

<h1>Tips and tricks for Debian on the QNAP TS-409</h1>

Here are some tips and tricks about running Debian on the QNAP TS-409.

<h2 id="qcontrol-upgrade">Automatic fan control</h2>

Debian ships a program called `qcontrol` which can be used to control the
fan, LEDs and buttons on QNAP devices.  You can edit the
`/etc/qcontrol.conf` configuration file to change the behaviour of
qcontrol, for example how the fans are regulated depending on the
temperature or which commands to run when a button is pressed.

<h2 id="autopower">Automatic power on</h2>

QNAP machines can turn on automatically when power is applied if the device
was not powered down correctly.  This is helpful when your power goes down.
In order to enable this feature, run the following command:

<div class="code">
<pre>
qcontrol --direct autopower on
</pre>
</div>

