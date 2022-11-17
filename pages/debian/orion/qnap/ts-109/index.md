---
title: Debian on QNAP TS-109
nav: TS-109
description: Instructions for running Debian on the QNAP TS-109
keywords: [Debian, NAS, QNAP, QNAP Turbo Station, Orion, TS-109, TS-109 II, TS-109 Pro, TS-109 Pro II]
---

<div class="right">
<img src = "images/r_ts109_front.jpg" class="border" alt="QNAP TS-109 from the front" width="148" height="217" />
</div>

The QNAP TS-109 is a NAS device that can be used for a variety of tasks.
In the following, I will describe what is needed to get Debian running on
your TS-109, TS-109 II, TS-109 Pro or TS-109 Pro II.

Please note that <a href="upgrade">Debian 10 was the last release</a> to
support these devices.  Debian 11 (bullseye) is not supported.

<h2>Information</h2>

<ul>

<li>An <a href = "install/">installation guide</a> for Debian on the QNAP
TS-109.</li>

<li>A set of <a href = "faq/">Frequently Asked Questions (FAQ)</a>.</li>

<li>A list of <a href = "known-issues/">known issues and bugs</a> with
Debian on the QNAP TS-109.</li>

<li><a href = "troubleshooting/">Troubleshooting information</a> with common
problems and their solutions.</li>

<li>Some <a href = "tips/">tips and tricks</a> about running Debian on the
QNAP TS-109.</li>

<li>A <a href = "status/">status page</a> showing which components of the
TS-109 are currently supported.</li>

<li>An <a href = "specs/">internals page</a> listing the specs of the
TS-109.</li>

<li>An <a href = "gallery/">image gallery</a> with various pictures showing
the internals of the TS-109.</li>

<li>Information about the <a href = "recovery/">recovery mode</a>.</li>

<li>Instructions for <a href = "deinstall/">restoring the original QNAP
firmware</a>.</li>

<li>Connecting a <a href = "serial/">serial console</a>.</li>

<li>Instructions for <a href = "uboot/">using U-Boot</a> (if you have a
serial console).  U-Boot is the boot loader used by QNAP.</li>

</ul>

<h2>External Resources</h2>

<ul>

<li>Information about <a href = "http://qnap.nas-central.org/">QNAP devices
at NAS-Central</a>.</li>

</ul>

<h2>Help</h2>

If you have problems with Debian on QNAP TS-109 and cannot solve them
with Google, there are the following resources you can consult:

<ul>

<li>The <a href = "http://lists.debian.org/debian-arm/">debian-arm list</a>
for questions specifically related to the ARM port of Debian or about
running Debian on the QNAP TS-109.</li>

<li>If you don't want to post to a mailing list, please post to the
<a href = "http://forum.qnap.com/viewforum.php?f=147">Debian area
on the QNAP forum</a>.</li>

<li>For questions about the QNAP TS-109 that are not related to Debian,
please use the <a href = "http://forum.qnap.com/">QNAP forum</a>.</li>

</ul>

<h2>Acknowledgements</h2>

A lot of people helped to make Debian on QNAP Turbo Station possible.  The
folks at QNAP have been very supportive of this effort and have supplied
some hardware and technical expertise.  Marvell has done a fabulous job
integrating Orion support into the mainline kernel.  Byron Bradley added
kernel support for the TS-109 and wrote qcontrol to control the LEDs
and buzzer.  Frans Pop packaged qcontrol for Debian and helped with the
development and testing of the Debian installer.

