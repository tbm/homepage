---
title: FAQ about Debian on the Kurobox Pro
nav: FAQ
description: FAQ about Debian on the Kurobox Pro
keywords: [Buffalo, Revogear, Kurobox Pro, FAQ, frequently asked questions, help, troubleshooting]
---

<div class="right">
<img src = "../images/r_kuroboxpro_front.jpg" class="border" alt="Kurobox Pro from the front" width="148" height="231" />
</div>

<h1>Frequently Asked Questions (FAQ)</h1>

<h3>Is Debian on the Kurobox Pro fully supported?</h3>

Most things are working already.  You can install and use Debian on your
device but some things are not supported as well as with the original
firmware.  In particular, the hard drive speed will be lower with Debian.
Please see the <a href = "../status/">status page</a> to see what is
supported.

<h3>Can you install Debian to MTD flash?</h3>

No, installations of Debian are currently only possible to a SATA disk.
The installation of Debian won't touch MTD flash at all, so the original
firmware from Buffalo can still be found in flash.

<h3>Is there a recovery mode?</h3>

Yes, the Kurobox Pro will request a kernel and ramdisk via TFTP when it has
been configured to boot from disk but there is no disk.  See the <a href =
"../recovery/">recovery page</a> for more information.

<h3>Will this installer also work on the Linkstation Pro/Live?</h3>

The Linkstation Pro/Live are supported by Debian.  The
Linkstation Pro/Live are not covered in this install guide but information
is available on the <a href =
"http://buffalo.nas-central.org/wiki/Install_Debian_on_the_Linkstation_Pro/Live">NAS-Central
Buffalo wiki</a>.

Go back to my <a href = "..">Debian on Kurobox Pro</a> page.

