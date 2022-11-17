---
title: FAQ about Debian on Plug Computers
nav: FAQ
description: FAQ about Debian on Plug Computers
keywords: [Debian, SheevaPlug, Marvell, FAQ, frequently asked questions, help, troubleshooting]
---

<div class="right">
<img src = "../images/r_sheevaplug_hand.jpg" class="border" alt="SheevaPlug in my hand" width="148" height="129" />
</div>

<h3>Which Plug Computers are supported by Debian?</h3>

There are many different Plug Computer models.  The SheevaPlug is the
original one and it is well supported.  Please check which <a href =
"../plugs/">other models</a> are supported.

<h3>How much space do I need to install Debian?</h3>

A normal installation of Debian (i.e. base system plus standard components)
will take about 400 MB, so a 1 GB USB stick or SD card is enough (even
though more is recommended).

<h3>How can I recover if U-Boot is not working?</h3>

The U-Boot binary mentioned on the [upgrade page](../uboot-upgrade) was
tested and is working.  However, in case you flashed a version of U-Boot
that does not work, you can use
[OpenOCD](https://packages.debian.org/stable/openocd) to recover your
SheevaPlug.

I don't have documentation on how to recover ("unbrick") using OpenOCD,
but the following two pages might be useful:

* [NewIT forum post](https://www.newit.co.uk/forum/index.php/topic,2835.0.html)
* [Blog post by Tadeu Bento](https://tadeubento.com/2018/sheevaplug-2018-unbrick/)

