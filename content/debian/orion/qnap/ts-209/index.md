---
title: Debian on QNAP TS-209
nav: TS-209
description: Instructions for running Debian on the QNAP TS-209
keywords: [Debian, NAS, QNAP, QNAP Turbo Station, Orion, TS-209, TS-209 II, TS-209 Pro, TS-209 Pro II]
---

<% content_for :right do %>
<img src = "images/r_ts209_front.jpg" class="border" alt="QNAP TS-209 from the front" width="148" height="97" />

<%= render "adsense-wideskyscaper-right" %>
<% end %>

<h1>Debian on QNAP TS-209</h1>

The QNAP TS-209 is a NAS device that can be used for a variety of tasks.
In the following, I will describe what is needed needed to get Debian
running on your TS-209, TS-209 II, TS-209 Pro or TS-209 Pro II.

<h2>News</h2>

<ul>

<li>[2011-02-06] Debian 6.0 (squeeze) <a href =
"http://www.debian.org/News/2011/20110205a">is out</a>.  Grab it and follow
my <a href = "install">installation guide</a>.</li>

<li>[2008-12-09] QNAP has released a <a href =
"http://www.cyrius.com/journal/debian/orion/qnap/recovery-mode-available">recovery
mode</a>: this is useful in case there are problems with the installation
or an upgrade of Debian.</li>

</ul>

<h2>Information</h2>

<ul>

<li>An <a href = "install">installation guide</a> for Debian on the QNAP
TS-209.</li>

<li>A set of <a href = "faq">Frequently Asked Questions (FAQ)</a>.</li>

<li><a href = "troubleshooting">Troubleshooting information</a> with common
problems and their solutions.</li>

<li>Some <a href = "tips">tips and tricks</a> about running Debian on the
QNAP TS-209.</li>

<li>A list of <a href = "known-issues">known issues and bugs</a> with
Debian on the QNAP TS-209.</li>

<li>A <a href = "status">status page</a> showing which components of the
TS-209 are currently supported.</li>

<li>An <a href = "specs">internals page</a> listing the specs of the
TS-209.</li>

<li>An <a href = "gallery">image gallery</a> with various pictures showing
the internals of the TS-209.</li>

<li>Information about the <a href = "recovery">recovery mode</a>.</li>

<li>Instructions for <a href = "deinstall">restoring the original QNAP
firmware</a>.</li>

<li>Connecting a <a href = "serial">serial console</a>.</li>

<li>Instructions for <a href = "uboot">using U-Boot</a> (if you have a
serial console).  U-Boot is the boot loader used by QNAP.</li>

</ul>

<h2>External Resources</h2>

<ul>

<li>Information about <a href = "http://qnap.nas-central.org/">QNAP devices
at NAS-Central</a>.</li>

</ul>

<h2>Help</h2>

If you have problems with Debian on QNAP TS-209 and cannot solve them
with Google, there are the following resources you can consult:

<ul>

<li>The <a href = "http://lists.debian.org/debian-arm/">debian-arm list</a>
for questions specifically related to the ARM port of Debian or about
running Debian on the QNAP TS-209.</li>

<li>If you don't want to post to a mailing list, please post to the
<a href = "http://forum.qnap.com/viewforum.php?f=147">Debian area
on the QNAP forum</a>.</li>

<li>For questions about the QNAP TS-209 that are not related to Debian,
please use the <a href = "http://forum.qnap.com/">QNAP forum</a>.</li>

</ul>

<h2>Acknowledgements</h2>

A lot of people helped to make Debian on QNAP Turbo Station possible.  The
folks at QNAP have been very supportive of this effort and have supplied
some hardware and technical expertise.  Marvell has done a fabulous job
integrating Orion support into the mainline kernel.  Byron Bradley added
kernel support for the TS-209 and wrote qcontrol to control the LEDs, fan
and buzzer.  Frans Pop packaged qcontrol for Debian and helped with the
development and testing of the Debian installer.

<div class="bbf">
<%= render "adsense-banner-before-footer" %>
</div>

