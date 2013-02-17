---
title: Debian on the Thecus N2100
nav: Thecus N2100
description: Instructions for running Debian on the Thecus N2100
keywords: [Debian, Thecus, N2100, installation, guide, IOP, NAS, server]
---

<% content_for :right do %>
<img src = "images/r_n2100.jpg" class="border" alt="Thecus N2100" width="141" height="148" />

<%= render 'adsense-wideskyscaper-right' %>
<% end %>

<h1>Debian on the Thecus N2100</h1>

The Thecus N2100 is a Network Attached Storage (NAS) device based on
Intel's IOP 80219 CPU and it can be used to run Debian.  It offers the
following features:

<ul>

<li>Intel IOP 80219 CPU running at 600 MHz</li>

<li>2 SATA slots</li>

<li>1 DDR400 slot, populated with 128 MB RAM</li>

<li>3 USB 2.0 ports</li>

<li>2 GBit Ethernet</li>

<li>1 mini-PCI slot</li>

</ul>

These specs are similar to comparable NAS devices but one special feature
of the N2100 is that it features a normal, expandable DDR400 RAM slot.  In
theory, up to 1 GB are supported using 64-bit DDR RAM, but RedBoot needs
major modifications to support more than 512&nbsp;MB.

While this device is produced by Thecus and sold as the Thecus YES Box
N2100, it is also available from a number of other companies.  The only
difference is that some of those vendors include 256&nbsp;MB rather than
128&nbsp;MB RAM.  So far, the following devices based on the Thecus N2100
are known:

<ul>

<li>Allnet ALL6500</li>

<li>ARP Datacon NAS-2100</li>

<li>Evesham SilverSTOR M-Box</li>

</ul>

<h2>Information</h2>

<ul>

<li>An <a href = "install">installation guide</a> for Debian on the Thecus
N2100.</li>

<li>A list of <a href = "known-issues">known issues and bugs</a> with
Debian on the Thecus N2100.</li>

<li>A <a href = "status">status page</a> showing which components of the
Thecus N2100 are currently supported.</li>

<li>An <a href = "specs">internals page</a> listing the specs of the Thecus
N2100.</li>

<li>An <a href = "gallery">image gallery</a> with various pictures showing
the internals of the Thecus N2100.</li>

<li>Recovery mechanism using <a href = "telnet">telnet to RedBoot</a>.</li>

<li>Some <a href = "deinstall">de-installation instructions</a> in case you
want to go back to the original Thecus firmware.</li>

</ul>

<h2>External resources</h2>

<ul>

<li>David Karlström describes how to connect a <a href =
"http://david.thg.se/n2100/addserial.html">serial console</a>.</li>

<li>OpenBSD's <a href = "http://www.openbsd.org/armish.html">armish
port</a> supports the Thecus N2100.</li>

</ul>

<h2>Acknowledgements</h2>

Thecus for providing an N2100 to Lennert Buytenhek and me, for answering
some questions in great detail and for generally supporting this effort.
Lennert Buytenhek integrated support for the Thecus N2100 into the
mainline kernel and significantly improved generic IOP support.
David Karlström and Riku Voipio reverse-engineered various aspects
of this machine, and Riku also wrote a driver for the fan and LEDs.

<div class="bbf">
<%= render 'adsense-banner-before-footer' %>
</div>

