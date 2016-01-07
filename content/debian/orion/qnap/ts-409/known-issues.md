---
title: Known issues of Debian on QNAP TS-409
nav: Known issues
keywords: [Debian, QNAP, TS-409, bugs, issues, defects]
---

<% content_for :right do %>
<img src = "../images/r_ts409_front.jpg" class="border" alt="QNAP TS-409 from the front" width="148" height="147" />
<% end %>

<h1>Known issues and bugs</h1>

Here is a list of known issues and bugs with Debian on the QNAP TS-409:

<ul>

<li>There's a timing issue that will result in <a
href="http://comments.gmane.org/gmane.linux.ide/47799">not all disks being
recognized</a> in time on boot.  If you're experience, you can <a
href="http://forum.qnap.com/viewtopic.php?p=284721#p284592">use a
workaround</a>.</li>

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

