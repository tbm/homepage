---
title: Debian on HP mv2120 and mv5020
nav: mv2120
description: Useful page for running Debian on the HP mv2120
keywords: [Debian, HP, Media Vault, mv2120, mv5020, mv5100]
---

<% content_for :right do %>
<img src = "images/r_mv2120_front.jpg" class="border" alt="HP mv2120 from the front" width="148" height="212" />

<%= render "adsense-wideskyscaper-right" %>
<% end %>

<h1>Debian on HP mv2120, mv5020 and the mv5100 series</h1>

The HP Media Vault mv2120 and the HP Media Vault Pro mv5020 are NAS devices
that can be used for a variety of tasks.  In the following, I will describe
what is needed to get Debian running on your HP mv2120.

<h2>Information</h2>

<ul>

<li>An <a href = "install/">installation guide</a> for Debian on the HP
mv2120.</li>

<li>A set of <a href = "faq/">Frequently Asked Questions (FAQ)</a>.</li>

<li>A list of <a href = "known-issues/">known issues and bugs</a> with
Debian on the HP mv2120.</li>

<li>A <a href = "status/">status page</a> showing which components of the HP
mv2120 are currently supported.</li>

<li>An <a href = "specs/">internals page</a> listing the specs of the HP
mv2120.</li>

<li>An <a href = "gallery/">image gallery</a> with various pictures of the
HP mv2120.</li>

<li>Connecting a <a href = "serial/">serial console</a>.</li>

</ul>

<h2>External Resources</h2>

<ul>

<li><a href = "http://k0lee.com/hpmediavault/index.php">HP Media Vault
FAQ and Knowledge base</a>, maintained by Lee Devlin.</li>

<li>Information about <a href = "http://hp.nas-central.org/">HP devices at
NAS-Central</a>.</li>

<li><a href = "http://tech.groups.yahoo.com/group/hackingthemediavault/">A
group at Yahoo</a> for people hacking the HP Media Vault.</li>

</ul>

<h2>Help</h2>

If you have problems with Debian on HP mv2120 and cannot solve them with
Google, there are the following resources you can consult:

<ul>

<li>The <a href = "http://lists.debian.org/debian-arm/">debian-arm list</a>
for questions specifically related to the ARM port of Debian or about
running Debian on the HP mv2120.</li>

</ul>

<h2>Acknowledgements</h2>

A lot of people helped to make Debian on HP mv2120 possible.  The folks at
HP have been very supportive of this effort and have supplied some
hardware.  Marvell has done a fabulous job integrating Orion support into
the mainline kernel.  Eugene San has figured out a lot of details about the
boot process of the HP mv2120.  Marc Singer has also done a lot of
investigation and has written uphpmvault.

<h2>Disclaimer</h2>

Even though I currently work for HP, all of this work was done in my spare
time.  Debian on the HP mv2120 is not supported by HP in any way.

<div class="bbf">
<%= render "adsense-banner-before-footer" %>
</div>

