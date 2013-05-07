---
title: HP nc4000 and Debian
nav: Debian on HP nc4000
description: Installation guide for Debian on the HP nc4000 and nc4010 laptops
keywords: [Debian, lenny, installation, HP, Compaq nc4000, Compaq nc4010, laptop]
---

<% content_for :right do %>
<img src = "images/r_nc4000.jpg" class="border" alt="HP nc4000" width="148" height="122" />

More <a href = "gallery/">pictures are available</a>.

<%= render "adsense-wideskyscaper-right" %>
<% end %>

<h1>Debian GNU/Linux on the HP Compaq nc4000</h1>

In the following, I'm going to describe how to install Debian GNU/Linux 5.0
(lenny) on a HP Compaq nc4000 notebook.  This page only contains
nc4000-specific information and should therefore be read together with
Debian's more general <a href =
"http://www.debian.org/releases/stable/i386/">installation guide</a>.

Please note that I no longer own a HP Compaq nc4000 notebook, so I won't
provide further updates to this page.

<h2><a id = "install">Installing Debian</a></h2>

There are multiple ways to install Debian.  The most convenient method is
probably net booting via PXE.  Alternatively, you can boot from an USB
CD-ROM drive if you have the docking station with a CD drive or an external
USB drive.  Finally, it is also possible to boot from an USB memory stick.

<h3><a id = "install-pxe">Installation via the net using PXE</a></h3>

In order to perform the installation via booting from the net using PXE,
you first have to configure a PXE server.  Joe Nahmias wrote a good <a href
=
"http://lists.debian.org/debian-testing/2003/debian-testing-200311/msg00098.html">summary</a>
about this, and there is a <a href =
"http://wiki.debian.org/PXEBootInstall">wiki entry</a> with more
information.  Once you have a PXE server to boot from, you have to
configure your laptop to enable net booting.  When you boot, press `F10` to
get into the BIOS.  Then, select `Security`, `Device Security` and
`Internal Network`.  There, you have to enable `adapter boot` and set `Boot
mode` to `PXE`.  After you've enabled PXE, you'll be able to select
`Notebook NIC` when the nc4000 asks you where to boot from.  If your PXE
server is configured properly, it will be found automatically.

<h3><a id = "install-cd">Installation from a CD</a></h3>

First, you have to download a CD image with Debian on it.  Torrents are <a
href = "http://www.debian.org/CD/torrent-cd/">available</a>.  Once you have
a CD with Debian, you can boot from your USB CD-ROM drive.  For this, you
have to first turn `Enable USB Legacy Support` on in your BIOS.  You will
then have the choice to boot either from the laptop hard drive or from the
USB CD-ROM drive.

<h3><a id = "boot-usb-stick">Booting from USB memory stick</a></h3>

Aleksandr Koltsoff wrote that he was able to boot from a USB memory stick.
He said that you have to do some trickery:

<ol>
<li>instead of partitioning the flash, you make the msdos-filesystem
  directly on it (/dev/sda instead of /dev/sda1).</li>
<li>then run syslinux on /dev/sda</li>
</ol>

(or whatever the memory stick is instead of `/dev/sda`)

<h2><a id = "ethernet">Ethernet</a></h2>

The nc4000 has a Broadcom NetXtreme BCM5705M chip which supports Gigabit
Ethernet (10/100/1000).  The Linux kernel includes the `tg3` driver for
these types of chipsets.

<h2><a id = "sound">Sound</a></h2>

The laptop has an ALi Corporation M5451 audio chip which is supported by
Linux.  By default, ALSA will be used and the `snd_ali5451` module is
loaded.

<h2><a id = "video">Video</a></h2>

The nc4000 features a ATI Radeon IGP 340M graphics chip.  As far as I know,
this chip is also known as Mobility U1.  During the installation, X.org
will be installed and it will automatically work, using the `ati` driver.

<h2><a id = "touchpad">Touchpad</a></h2>

Both the touchpad and pointer stick work without any problems.

<h2><a id = "buttons">Additional Buttons</a></h2>

Aki Mimoto mentioned that you can also get the 7 special buttons on the
upper side of the keyboard to work.  Simply add the following lines to your
`~/.Xmodmap` file:

<pre>
keycode 160 = F21
keycode 174 = F22
keycode 176 = F23
keycode 136 = F24
keycode 248 = F25
keycode 138 = F26
</pre>

(160 = cpqmute, 174 = cpqvoldown, 176 = cpqvolup, 136 = cpqpresentation,
248 = cpqwireless, 138 = cpqlock)

<h2><a id = "usb">USB</a></h2>

USB works without any problems.

<h2><a id = "wireless">Wireless</a></h2>

The Linux 2.6.26 kernel shipped in Debian lenny has the `ath5k` module with
which wireless works without any problems.  You don't need any binary
firmware to use wireless.

<h2><a id = "pm">Power management</a></h2>

ACPI correctly reports the battery status as well as information about the
fans.  Frequency scaling is done automatically.

<h3><a id = "powerplay">Radeon PowerPlay</a></h3>

Fabian Kneißl pointed out to me that the Radeon IGP video chip has a
power-saving feature known as PowerPlay which can be activated in X.org
with the following line:

<pre>
       Option            "DynamicClocks"          "true"
</pre>

You can use my <a href = "info/xorg.conf">info/xorg.conf</a> file and save
it as `/etc/X11/xorg.conf`.  You should see the following in
`/var/log/Xorg.0.log` when starting X:

<pre>
(**) RADEON(0): Option "DynamicClocks" "true"
...
(II) RADEON(0): Dynamic Power Management Enabled
</pre>

<h2><a id = "swsusp">Software Suspend</a></h2>

You can use `s2disk` to hibernate your system (i.e. to write the content to
disk and power it off).  Suspend to memory does not work on the nc4000.

<h2><a id = "modem">Modem</a></h2>

Not tested.  Bdale Garbee said he got it to work.

<h2><a id = "irda">IRDA</a></h2>

Not tested.

<h2><a id = "pcmcia">PCMCIA</a></h2>

It works without any problems.  All modules are loaded automatically.

<h2><a id = "tools">Useful utilities</a></h2>

Michael Rasmussen pointed out that <a href =
"http://packages.debian.org/laptop-mode-tools">laptop-mode-tools</a> is a
useful package for laptops.  The package contains several userland scripts
that can be used to save considerable battery power.  By default, this
package remounts your partitions with the `noatime` parameter when you are
on battery.  Unfortunately, this breaks mutt, a popular e-mail client.
Please be sure to read through the documentation of this package and to
look at the configuration file, `/etc/laptop-mode/laptop-mode.conf`.

<h2><a id = "caveats">Caveats</a></h2>

<ul>

<li>Aleksandr Koltsoff told me that <a href =
"http://www.syslinux.org/wiki/index.php/MEMDISK">memdisk</a> (a program to boot e.g.
from a floppy image via the network) does not work; interestingly, I
observed the same so this seems to be a bug in the nc4000.  Aleksandr
observes that &quot;there's definitely something fishy about the BIOS since
for example using memdisk with syslinux doesn't work on nc4000, although on
nc6000 it works as expected.&quot;</li>

<li>When the laptop is in the docking station and I connect a USB memory
stick during bootup, the system freezes hard.</li>

</ul>

<h2><a id = "config">Configuration Files</a></h2>

The <a href = "info/lspci">output of `lspci`</a> is available, along with
the output from <a href = "info/lspciv">`lspci -v`</a> and <a href =
"info/lspcivv">`lspci -vv`</a>.  The output of <a href =
"info/dmesg">`dmesg`</a> from a 2.6 kernel can be viewed as well.

<h2><a id = "links">Links</a></h2>

<ul>

<li>Bob Proulx's <a href = "http://www.proulx.com/~bob/nc4000/"> Debian
GNU/Linux on the HP Compaq nc4000 Laptop</a> page.</li>

<li>Matt Taggart's <a href =
"http://lackof.org/matt/hacking/hpnc4010/">Debian GNU/Linux on the HP
nc4010 laptop</a> page.</li>

</ul>

<h2><a id = "ack">Acknowledgements</a></h2>

Thanks to Herbert Xu for kernel related help.  Jerullah K. and Aki Mimoto
for various tips.  Michael Schulz for telling me that wireless works, and
Bdale Garbee for miscellaneous help.  Aleksandr Koltsoff for information on
booting from an USB memory stick.  Bob Proulx for various stuff.  Michael
Rasmussen for information about swsusp, X.org and the wireless LED.  Fabian
Kneißl for information about Radeon's PowerPlay feature.

<div class="bbf">
<%= render "adsense-banner-before-footer" %>
</div>

