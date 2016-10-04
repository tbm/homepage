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

* The installer fails to make the system bootable, especially on
configurations with LVM and RAID.  You can [apply a
workaround](../troubleshooting/#bootable).
* There's a timing issue that will result in <a
href="http://comments.gmane.org/gmane.linux.ide/47799">not all disks being
recognized</a> in time on boot.  If you're experience, you can <a
href="http://forum.qnap.com/viewtopic.php?p=284721#p284592">use a
workaround</a>.
* qcontrol (the tool to control LEDs and beeper) doesn't work.

