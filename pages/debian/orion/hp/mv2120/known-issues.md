---
title: Known issues of Debian on HP mv2120
nav: Known issues
keywords: [Debian, HP, mv2120, bugs, issues, defects]
---

<div class="right">
<img src = "../images/r_mv2120_front.jpg" class="border" alt="HP mv2120 from the front" width="148" height="212" />
</div>

Here is a list of known issues and bugs with Debian on the HP mv2120:

<ul>

<li>Although the kernel reports button presses, there's currently no
userland tool that will listen to the button events and actually do
something with them (i.e. reset or power down the machine).</li>

<li>Upgrades from Debian 8 (jessie) to Debian 9 (stretch) require a <a
href="../uboot-config">change in the u-boot configuration</a>.</li>

</ul>

