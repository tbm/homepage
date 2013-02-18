---
title: Debian on SGI O2
description: Installation guide for Debian on SGI O2
keywords: [Debian, SGI, O2, sarge, installation]
---

<% content_for :right do %>
<img src = "images/r_sgi_o2.jpg" class="border" alt="SGI O2" width="148" height="188" />

<%= render "adsense-wideskyscaper-right" %>
<% end %>

In the following, I will describe how to install Debian 5.0 (lenny) on SGI
O2 (IP32) machines with R5000, R5200 or RM7000 processors.

Note that I will only discuss issues related to the installation on O2 and
not go into any details concerning SGI in general.  Please read other
Debian on SGI HOWTOs, such as <a href =
"http://www.pvv.org/~pladsen/Indy/HOWTO.html">this</a> and <a href =
"http://www.zorg.org/linux/indy.shtml">that</a> document as well as <a href
= "http://www.debian.org/releases/stable/mips">Debian's installation guide
for MIPS</a>, before starting.  In particular, take a look at Jiann-Ming
Su's <a href = "http://js1.kicks-ass.org/~js1/debianO2.html">detailed
run-through</a> with the O2 images I've prepared.  Once you're familiar
with how to set up an environment to load the installer for SGI, you can
download the <a href =
"ftp://ftp.nl.debian.org/debian/dists/lenny/main/installer-mips/current/images/r5k-ip32/">installer
image for O2</a>.  This image supports installations both via serial
console as well as framebuffer.

The installation on O2 is just like on any other platform.  Towards the end
of the installation, Arcboot will be installed which lets you boot your SGI
from disk with the `boot` command.

<h2>Acknowledgements</h2>

Thiemo Seufer has done lots of MIPS work on the installer and the kernel.
He thoroughly tested the 2.6 kernel on O2 and prepared Debian packages.
Also, the debian-installer team has done a great job making an easy-to-use
installer which supports many platforms.  Finally, I'd also like to thank
Jö Fahlke for making an O2 available to me.

<h2>Help</h2>

If you need any help getting Debian running on your O2 after reading
this installation guide and using Google, you can contact the <a href =
"http://lists.debian.org/debian-mips/">Debian MIPS</a> mailing list.

<div class="bbf">
<%= render "adsense-banner-before-footer" %>
</div>

