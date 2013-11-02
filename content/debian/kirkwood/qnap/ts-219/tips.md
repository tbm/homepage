---
title: Tips and tricks for Debian on QNAP TS-21x/TS-22x
nav: Tips
description: Tips and tricks for Debian on QNAP TS-21x/TS-22x
keywords: [Debian, QNAP, TS-210, TS-212, TS-219, TS-219P, TS-220, TS-221, tips, tricks]
---

<% content_for :right do %>
<img src = "../images/r_ts219p.jpg" class="border" alt="Open QNAP TS-219" width="148" height="188" />

<%= render "adsense-wideskyscaper-right" %>
<% end %>

<h1>Tips and tricks for Debian on QNAP TS-21x/TS-22x</h1>

Here are some tips and tricks about running Debian on the QNAP
TS-21x/TS-22x.

<h2><a id="qcontrol-upgrade">Upgrading qcontrol for automatic fan control</a></h2>

Debian ships a program called `qcontrol` which can be used to control the
fan, LEDs and buttons on QNAP devices.  The version of qcontrol included in
Debian 7 (wheezy) is missing a number of important features, such as
automatic temperature control.  Fortunately, Ian Campell, the maintainer of
qcontrol, has provided a backport of qcontrol to Debian 7 which includes
many new features.

In order to install this updated version of qcontrol, you have to configure
the `wheezy-backports` repository by editing the file
`/etc/apt/sources.list` and adding the following line:

<div class="code">
<pre>
deb http://ftp.debian.org/debian/ wheezy-backports main
</pre>
</div>

Afterwards, run the following commands to active the new repository and
install the updated qcontrol package:

<div class="code">
<pre>
apt-get update
apt-get install -t wheezy-backports qcontrol
</pre>
</div>

qcontrol will now run in daemon mode and control the fan and listen for
button presses.  You can edit the `/etc/qcontrol.conf` configuration file
to change the behaviour of qcontrol, for example how the fans are regulated
depending on the temperature or which commands to run when a button is
pressed.

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

