---
title: FAQ about Debian on Linksys NSLU2
nav: FAQ
description: FAQ about Debian on Linksys NSLU2
keywords: [NSLU2, Linksys NSLU2, Debian, FAQ, questions]
---

<div class="alert alert-danger">

The Linksys NSLU2 is no longer supported by Debian.

</div>

<div class="right">
<img src = "../images/r_nslu2_front.jpg" class="border" alt="A NSLU2 from the front" width="148" height="218" />
</div>

<h3>Is Debian on the NSLU2 fully supported?</h3>

Debian 8 (jessie) was the last release to include some support for the Linksys NSLU2.  There
is no installer but you can install a <a href = "../unpack/">tar ball
of Debian 7</a> and then upgrade to Debian 8.

Please note that Debian 8 was the last release to support the NSLU2.  There
is no support in Debian 9 (stretch) or Debian 10 (buster).

<h3>The NSLU2 is slow... what alternatives are there to the NSLU2?</h3>

While the NSLU2 is a nice device, it only offers a 133 or 266 MHz CPU and
32 MB of RAM.  You therefore cannot expect particularly good performance.
A modern alternative to the NSLU2 is the <a href =
"/debian/kirkwood/sheevaplug/">Marvell SheevaPlug</a> which is also
supported by Debian.

<h3>Why does my NSLU2 no longer boot?</h3>

There can me many different reasons for this.  Please see the <a href =
"../troubleshooting/#debian">troubleshooting page</a> for some things you
can try.

<h3>How do upgrades work?</h3>

Upgrades with Debian on the NSLU2 work like on any other Debian system.
You can simply use `apt-get` or `aptitude` for upgrades:

<div class="code">
<pre>
apt-get update
apt-get dist-upgrade
</pre>
</div>

<h3>How can I upgrade the kernel?  Is it written to flash automatically?</h3>

Debian will take of everything automatically.  When you install a Debian
kernel package, a tool called `flash-kernel` will automatically write the
new kernel and ramdisk to flash.

<h3>How can I make a backup of flash?</h3>

You can make a backup of the flash of your NSLU2 with the following
command:

<div class="code">
<pre>
cat /dev/mtdblock* &gt; nslu2-backup
</pre>
</div>

