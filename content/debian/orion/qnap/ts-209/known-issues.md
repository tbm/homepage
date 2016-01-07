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

<ul>

<li>No automatic temperature regulation: there is currently no regulation
of the fan speed depending on the system temperature.</li>

<li>Power and USB buttons not supported: there's currently no way to
associate the power and USB buttons with specific actions, such as shutting
down the system or copying a file.  Note: if you press the power button for
a few seconds, the system will shut down.  However, this is not software
but hardware controlled.  This means that Linux is currently not properly
shut down when you press the power button and your system may have to check
the disks for a long them on the next reboot.  Please do not use the power
button!</li>

</ul>

