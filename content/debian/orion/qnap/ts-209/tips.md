---
title: Tips and tricks for Debian on QNAP TS-209
nav: Tips
description: Tips and tricks for Debian on QNAP TS-209
keywords: [Debian, QNAP, TS-209, tips, tricks]
---

<% content_for :right do %>
<img src = "../images/r_ts209_front.jpg" class="border" alt="QNAP TS-209 from the front" width="148" height="97" />

<%= render "adsense-wideskyscaper-right" %>
<% end %>

<h1>Tips and tricks for Debian on the QNAP TS-209</h1>

Here are some tips and tricks about running Debian on the QNAP TS-209.

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

