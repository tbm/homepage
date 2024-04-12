---
title: Hardware compatible with the BCM91250A
nav: Hardware List
description: List of hardware compatible with Broadcom's SWARM
keywords: [hardware list, compatibility, SWARM, PCI]
---

The BCM91250A has standard PCI slots (two 32 and two 64 bit slots, 3.3v
only) but not all PCI cards (especially graphics cards) are supported.
I had a particularly hard time finding a graphics card which would work.
With a supported graphics card, the BCM91250A can be used as a desktop like
system with USB keyboard.  In the following, I've listed hardware which has
been tested on an BCM91250A board and which either worked or didn't work.

<h2>Graphics cards</h2>

<ul>

<li>S3 ViRGE/DX: does <i>not</i> work (with CFE VGA emulation).</li>

<li>Nvidia Riva 128: does <i>not</i> work (with CFE VGA emulation).</li>

<li>3Dfx Voodoo3: does <i>not</i> work (neither with CFE VGA emulation nor
Linux framebuffer).</li>

<li>nVidia NV5M64 (RIVA TNT2): works (with CFE VGA emulation) but only in
text mode (no framebuffer or X11).  Linux framebuffer does not work.</li>

<li>Matrox G450: some G450 based cards work with the Linux framebuffer
driver.  The version with 16 MB (revision 82) does <i>not</i> work while
the 32 MB variant (revision 85) is reported to work!</li>

</ul>

<h2>Ethernet cards</h2>

<ul>

<li>D-Link Systems product 0x1300: works with the <code>8139too</code> module.</li>

<li>3Com 3c905C-TX 10/100: works with the <code>3c59x</code> module.</li>

</ul>

<h2>IDE controllers</h2>

<ul>

<li>Silicon Image PCI0680 Ultra ATA-133 Host Controller: works.</li>

</ul>

<h2>SCSI controllers</h2>

<ul>

<li>Adaptec AIC-7892A U160: works (in the 64 bit slot).</li>

</ul>

