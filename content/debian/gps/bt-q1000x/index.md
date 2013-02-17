---
title: Qstarz BT-Q1000X and Debian
nav: Qstarz BT-Q1000X
keywords: [Qstarz, BT-Q1000X, GPS, MTK II, Debian, Linux, mtkbabel]
---

<% content_for :right do %>
<img src = "images/r_bt-q1000x_hand.jpg" class="border" alt="Qstarz BT-Q1000X in my hand" width="148" height="136" />

<%= render 'adsense-wideskyscaper-right' %>
<% end %>

<h1>Qstarz BT-Q1000X and Debian</h1>

The <a href =
"http://www.qstarz.com/Products/GPS%20Products/BT-Q1000X-F.htm">Qstarz
BT-Q1000X</a> (Travel Recorder X) is a GPS device that can act as data
logger and as receiver.  That is, the device can record GPS data while
you're moving around so you can later download this information to your PC,
and it can also broadcast the GPS information via Bluetooth as you're
moving around so you can receive the information on another device and do
something with it immediately (for example, display maps of where you're
going).  The BT-Q1000X can also log and broadcast data at the same time.

The Qstarz BT-Q1000X ships with some software for Windows, but I'm using it
with Linux (specifically, with Debian).  On this page, I'll describe how to
use the BT-Q1000X on Debian (and other Linux variants).

<h2>Connecting the Qstarz BT-Q1000X via USB</h2>

You can connect the Qstarz BT-Q1000X via USB to your PC in order to
download the GPS information stored on the device.  You have to load the
`cdc-acm` module in order to access the Qstarz BT-Q1000X.  On Debian and
other modern distributions, the module should get loaded automatically when
you plug in the device and turn it on (you can set the device either to
navigate or log but I use navigate).  The GPS chip used in the Qstarz
BT-Q1000X is supported by the Linux kernel since 2.6.29; if you're using an
older kernel, you have to <a href =
"http://git.kernel.org/?p=linux/kernel/git/torvalds/linux-2.6.git;a=commitdiff;h=0f9c7b4a1cc24d6f05a848f0acf72dbff7c5d42d">apply
this fix</a>.  On Debian, you can either use 2.6.29 or higher, or 2.6.26-16
or higher (Debian lenny 5.0.2 or newer will work).  When you connect your
BT-Q1000X via USB and turn it on, the device will show up as
`/dev/ttyACM0`.

<h2>Qstarz BT-Q1000X and gpsbabel</h2>

gpsbabel can read data from the BT-Q1000X and store it as GPX information.
You can read the information with this command:

<div class="code">
<pre>
gpsbabel -t -w -i mtk -f /dev/ttyACM0 -o gpx -F out.gpx
</pre>
</div>

This will store the information in GPX format in the file `out.gpx`.  After
you've verified the information, you can erase it with the following
command:

<div class="code">
<pre>
gpsbabel -t -w -i mtk,erase -f /dev/ttyACM0
</pre>
</div>

<h2>Qstarz BT-Q1000X and mtkbabel</h2>

<a href =
"http://www.rigacci.org/wiki/doku.php/doc/appunti/hardware/gps_logger_i_blue_747">mtkbabel</a>
is a command line tool to manage devices that use MTK chips.  I'm using
mtkbabel just fine with the Qstarz BT-Q1000X which uses a MTK II chip.
mtkbabel comes with a man page that explains the command line options.  The
most common commands are the following two.  First, download the data and
store it as the file "gpsdata":

<div class="code">
<pre>
mtkbabel -p /dev/ttyACM0 -f gpsdata -t -w -c
</pre>
</div>

And then erase the data from the device:

<div class="code">
<pre>
mtkbabel -p /dev/ttyACM0 -E
</pre>
</div>

<div class="bbf">
<%= render 'adsense-banner-before-footer' %>
</div>

