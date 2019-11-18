---
title: Tips and tricks for Debian on QNAP TS-41x/TS-42x
nav: Tips
description: Tips and tricks for Debian on the QNAP TS-41x/TS-42x
keywords: [Debian, QNAP, TS-410, TS-410U, TS-412, TS-419P, TS-419U, TS-420, TS-421, tips, tricks]
---

<div class="right">
<img src = "../images/r_qnap_ts419p.jpg" class="border" alt="QNAP TS-419P from the front" width="148" height="148" />
</div>

Here are some tips and tricks about running Debian on the QNAP
TS-41x/TS-42x.

<h2 id="qcontrol-upgrade">Automatic fan control</h2>

Debian ships a program called `qcontrol` which can be used to control the
fan, LEDs and buttons on QNAP devices.  You can edit the
`/etc/qcontrol.conf` configuration file to change the behaviour of
qcontrol, for example how the fans are regulated depending on the
temperature or which commands to run when a button is pressed.

<h2 id="wakealarm">Scheduled power</h2>

You can tell your QNAP device to power on at a specific time using the
`wakealarm` system.  For example, if you want your QNAP to power on in 5
minutes, issue the following commands and turn off your device:

<div class="code">
<pre>
echo 0 | sudo tee /sys/class/rtc/rtc0/wakealarm
echo `date '+%s' -d '+ 5 minutes'` | sudo tee /sys/class/rtc/rtc0/wakealarm
</pre>
</div>

You can check check whether a wakealarm has been configured with:

<div class="code">
<pre>
cat /proc/driver/rtc
</pre>
</div>

Look for `alrm_time` and `and alrm_date`.

<h2 id="autopower">Automatic power on</h2>

QNAP machines can turn on automatically when power is applied if the device
was not powered down correctly.  This is helpful when your power goes down.
In order to enable this feature, run the following command:

<div class="code">
<pre>
sudo qcontrol --direct autopower on
</pre>
</div>

