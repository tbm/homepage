---
title: Known issues of Debian on QNAP TS-109
nav: Known issues
keywords: [Debian, QNAP, TS-109, bugs, issues, defects]
---

<% content_for :right do %>
<img src = "../images/r_ts109_front.jpg" class="border" alt="QNAP TS-109 from the front" width="148" height="217" />

<%= render 'adsense-wideskyscaper-right' %>
<% end %>

<h1>Known issues and bugs</h1>

Here is a list of known issues and bugs with Debian on the QNAP TS-109:

<ul>

<li>Power and USB buttons not supported: there's currently no way to
associate the power and USB buttons with specific actions, such as shutting
down the system or copying a file.  Note: if you press the power button for
a few seconds, the system will shut down.  However, this is not software
but hardware controlled.  This means that Linux is currently not properly
shut down when you press the power button and your system may have to check
the disks for a long them on the next reboot.  Please do not use the power
button!</li>

</ul>

<div class="bbf">
<%= render 'adsense-banner-before-footer' %>
</div>

