---
title: Upgrade CFE on the BCM91250A
nav: CFE Upgrade
description: Upgrade guide of the CFE firmware
keywords: [upgrade, CFE, SWARM, firmware, MIPS]
---

<div class="alert alert-danger">

Support for the BCM91250A board was dropped from Debian.  This page is
only provided for historical purposes.

</div>

In order to install Debian, you might have to upgrade the firmware (CFE) on
your BCM91250A.  Older versions used `ide0` to refer to the first IDE
device while newer versions use `ide0.0`.  I've obtained an <a href =
"../cfe-ws-ex.flash">image of CFE 1.0.40</a> from Broadcom which has
supports for VGA init, USB, IDE, and everything else.  It's also the
"bi-endian" version, meaning it should boot either big or little endian by
changing jumper J1 on your SWARM.

To update your flash, put the `cfe-ws-ex.flash` image to your TFTP server.
Check that the md5sum matches `4102210a104b1e30ecb0ebcf7980976b`.  Then,
do:

<div class="code">
<pre>
CFE&gt; ifconfig eth0 -auto
CFE&gt; flash <span class="input">hostname</span>:<span class="input">path/to/</span>cfe-ws-ex.flash flash0
</pre>
</div>

Since it's a bi-endian image, it's pretty big and may take 30-40 seconds to
write to flash.  If you press the reset button after it's done, you should
be up and running with the new version.  Please note that once you've
started to flash this new version, you may not interrupt the process!  If
you interrupt you, you may end with a board which no longer boots.  Also
note that this flash image is provided under no warranty.  It worked for me
and some others, but it may not work for you.

Thanks to Mitch Lichtenberg of Broadcom who provided most of the
information for this CFE page.

