---
title: Known issues of Debian on QNAP TS-209
nav: Known issues
keywords: [Debian, QNAP, TS-209, bugs, issues, defects]
---

<% content_for :right do %>
<img src = "../images/r_ts209_front.jpg" class="border" alt="QNAP TS-209 from the front" width="148" height="97" />
<% end %>

<h1>Known issues and bugs</h1>

Here is a list of known issues and bugs with Debian on the QNAP TS-209:

* The installer fails to make the system bootable, especially on
configurations with LVM and RAID.  You can [apply a
workaround](../troubleshooting/#bootable).
* qcontrol (the tool to control LEDs and beeper) doesn't work.

