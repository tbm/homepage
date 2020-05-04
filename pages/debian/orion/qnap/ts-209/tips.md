---
title: Tips and tricks for Debian on QNAP TS-209
nav: Tips
description: Tips and tricks for Debian on QNAP TS-209
keywords: [Debian, QNAP, TS-209, tips, tricks]
---

<div class="right">
<img src = "../images/r_ts209_front.jpg" class="border" alt="QNAP TS-209 from the front" width="148" height="97" />
</div>

Here are some tips and tricks about running Debian on the QNAP TS-209.

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
sudo qcontrol --direct autopower on
</pre>
</div>

<h2 id="battery">Battery for clock</h2>

There's a CR-2032 battery hidden on the bottom of the main board (similar
to the CMOS battery on most PCs).  It's likely that the battery is dead
after all these years and has to be replaced.

