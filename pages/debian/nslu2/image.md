---
title: Linksys NSLU2 installer images for Debian
nav: Installer Images
description: debian-installer images for Linksys NSLU2
keywords: [Debian, NSLU2, Linksys NSLU2, DebianSlug, Ethernet, IXP4xx, SlugDebian]
---

<div class="right">
<img src = "../images/r_nslu2_front.jpg" class="border" alt="A NSLU2 from the front" width="148" height="218" />
</div>

The Intel IXP4xx chip used in the Linksys NSLU2 needs some proprietary
microcode for the Ethernet driver.  As such, it cannot be distributed by
the Debian project since we believe in free software and the advantages it
offers to our users.  While you can download an NSLU2 image <a href =
"http://ftp.nl.debian.org/debian/dists/lenny/main/installer-armel/current/images/ixp4xx/netboot/">directly
from Debian</a> this is probably <em>not</em> what you are looking for.  It
will only work if you use a USB Ethernet adapter.  If you wish to use the
Ethernet port of your NSLU2, you have to use the <a href =
"http://www.slug-firmware.net/">unofficial images</a> which are a copy of
the Debian images plus the proprietary Ethernet microcode.

Once you have obtained the installer image, please follow the <a href =
"../install/">installation guide</a>.

