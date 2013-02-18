---
title: FAQ about Debian on HP mv2120
nav: FAQ
description: FAQ about Debian on HP mv2120
keywords: [Debian, HP, mv2120, FAQ, frequently asked questions, help, troubleshooting]
---

<% content_for :right do %>
<img src = "../images/r_mv2120_front.jpg" class="border" alt="HP mv2120 from the front" width="148" height="212" />

<%= render "adsense-wideskyscaper-right" %>
<% end %>

<h1>Frequently Asked Questions (FAQ)</h1>

<h3>Is Debian on the HP mv2120 fully supported?</h3>

Debian includes support for the HP mv2120.  However, some functionality
from the original firmware may not be available.  In particular, the hard
drive speed will be lower with Debian.  Please see the <a href =
"../status">status page</a> to see what is supported.

<h3>Is Debian on the HP mv2120 suited for people new to Linux?</h3>

No, I would not recommend you install Debian on your HP mv2120 if you don't
have any experience with Linux and Debian.  Debian will not install a web
interface through which you can control your HP mv2120, so I recommend you
stay with the original firmware from HP.

<h3>Can I have both the HP firmware and Debian?</h3>

No, Debian will completely replace the HP firmware on disk.  You have to
choose between the HP firmware and the Debian installation described on my
pages.  However, it would be possible to make a small Debian system on your
disk with the HP firmware by using `debootstrap` and `chroot`.

<h3>Will this installer work on the HP mv5020, mv5140 or mv5150?</h3>

Yes, all Media Vault generation 2 devices are supported.  This includes the
HP Media Vault mv2120 and the HP Media Vault Pro mv5000 and mv5100 series.
These devices are the same and only differ in their disk configuration.
The mv2120 (GX662AA) and mv5020 (GX666AA) have a single 500 GB drive, the
mv5140 (GX667AA) has two 500 GB drives and the mv5150 (GX668AA) has a pair
of 750 GB drives.

<h3>Will this installer work on the HP mv2010?</h3>

No, Media Vault generation 1 devices (mv2010, mv2020, and mv2040) are not
supported.  They are based on a MIPS compatible chip from Broadcom whereas
the generation 2 devices are based on Marvell's Orion chip that is ARM
compatible.

<h3>Will this installer work on the HP MediaSmart Server (EX470/EX475)?</h3>

No, the HP MediaSmart Server is based on a x86 chip and not supported by
this installation routine (although Debian might work on the MediaSmart
Server).

<h3>Is Debian on the HP mv2120 supported by HP?</h3>

No.  Even though I currently work for HP, all of this work was done in my
spare time.  Debian on the HP mv2120 is not supported by HP in any way.  I
should also mention that my work at HP is not related to the mv2120 or
other NAS devices at all.

<h3>Is there a recovery mode?</h3>

Yes, the HP mv2120 has a recovery mode through which it can request a boot
image over the local network.  You can serve a recovery image to your HP
mv2120 via the network with a HP supplied tool on Windows or with
uphpmvault on Debian and other systems.  You can put your HP mv2120 into
recovery mode by following these steps: hold the reset button down, then
press the power button and keep both buttons pressed for about 5 seconds.
Your HP mv2120 will now request a recovery image via your local network.

<h3>Is the serial header soldered onto the board already?</h3>

Yes, a serial header is on the main board.  You only need to prepare a
cable with a TTL level shifter for a <a href = "../serial">serial
console</a>.

<h3>Will I need a serial console to use Debian?</h3>

No, the installation and operation of Debian on your HP doesn't require a
serial console.

Go back to my <a href = "..">Debian on HP mv2120</a> page.

<div class="bbf">
<%= render "adsense-banner-before-footer" %>
</div>

