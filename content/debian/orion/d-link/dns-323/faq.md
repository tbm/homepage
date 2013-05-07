---
title: FAQ about Debian on D-Link DNS-323
nav: FAQ
description: FAQ about Debian on D-Link DNS-323
keywords: [Debian, D-Link, DNS-323, Conceptronic, CH3SNAS, FAQ, frequently asked questions, help, troubleshooting]
---

<% content_for :right do %>
<img src = "../images/r_ch3snas_front.jpg" class="border" alt="Conceptronic CH3SNAS from the front" width="148" height="146" />

<%= render "adsense-wideskyscaper-right" %>
<% end %>

<h1>Frequently Asked Questions (FAQ)</h1>

<h3>Is Debian on the D-Link DNS-323 and Conceptronic CH3SNAS fully supported?</h3>

Yes, Debian on the D-Link DNS-323 (revision A1 and B1) and Conceptronic
CH3SNAS is officially supported.  The D-Link DNS-323 revision C1 is not
supported.

<h3>Is Debian on the DNS-323 or CH3SNAS suited for people new to Linux?</h3>

No, I would not recommend you install Debian on your DNS-323 or CH3SNAS if
you don't have any experience with Linux and Debian.  Debian will not
install a web interface through which you can control your device, so I
recommend you stay with the original firmware.

<h3>Can I have both the original firmware and Debian?</h3>

No, Debian will completely replace the original firmware in flash.  You
have to choose between the original firmware and the Debian installation
described on my pages.  However, it is possible to make a small Debian
system on your disk with the original firmware; see the <a href =
"http://dns323.kood.org/howto:install_debian">instructions on the DNS-323
wiki</a>.

<h3>Which devices are supported?</h3>

The D-Link DNS-323 revision A1 and B1 are supported.  Revision C1 is
currently not supported.  You can find the revision by looking for "H/W
Ver" at the bottom of your DNS-323.  In addition to the D-Link DNS-323, the
Conceptronic CH3SNAS is supported.

<h3>Are other D-Link models, such as the DNS-321 or DNS-325, supported?</h3>

No, only the D-Link DNS-323 is supported.  I'm not planning to add support
for other D-Link devices but you're welcome to contribute patches to the
debian-arm list.

<h3>Is there a recovery mode?</h3>

There is no recovery mode that would allow you to load a rescue firmware
image via the network.  However, if you have a serial console, there is a
<a href = "../recovery/">recovery option</a>.

Go back to my <a href = "..">Debian on D-Link DNS-323 and Conceptronic
CH3SNAS</a> page.

<div class="bbf">
<%= render "adsense-banner-before-footer" %>
</div>

