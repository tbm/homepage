---
title: "Debian on Broadcom's BCM91250A evaluation board"
nav: Debian on the BCM91250A
description: "Useful information for running Debian on Broadcom's SWARM board"
keywords: [BCM91250A, MIPS, evaluation board, Debian]
---

<% content_for :right do %>
<img src = "images/r_swarm_mobo.jpg" class="border" alt="SWARM motherboard" width="148" height="184" />
<% end %>

<b>Important note:</b> I no longer own an BCM91250A board, so these pages
are not out-of-date and no longer updated.  They are only provided in the
hope that some of the information might be useful.

<h1>Debian on the BCM91250A evaluation board</h1>

The BCM91250A is an ATX form factor evaluation board from Broadcom based on
their SiByte processor family.  Specifically, the BCM91250A uses the
BCM1250 processor which features two Broadcom SB-1 (SiByte) MIPS64 CPU
cores.  On this page, I have collected and offer various technical
information which I hope is useful in getting Linux (and <a href =
"http://www.debian.org/">Debian</a> in particular) running on the BCM1250
evaluation board (which is also known under the name <i>SWARM</i>) and
possibly other boards based on the SiByte processor family.

The BCM91250A can function in both big and little endian mode and Linux as
well as Debian support both modes of operation.  You need a version of CFE,
the firmware used by Broadcom's SiByte evaluation boards, which supports
the mode you wish to use.  Broadcom has kindly provided me with a bi-endian
image which supports both modes depending on your hardware setting.  You
set the mode through a jumper on the board (J1) as explained in the
BCM91250A User Manual.  Information about installing this bi-endian image
of CFE on your board can be <a href = "cfe/">found here</a>.

In addition to CFE, which acts as firmware, there is a program which can be
used to load Linux.  While CFE itself can boot Linux too, SiByl (the SiByte
Loader) offers more features, such as the ability to boot from an IDE hard
drive and to load an initial ramdisk.  SiByl is <a href =
"http://packages.debian.org/sibyl">packaged for Debian</a>.  SiByl is used
by Debian to offer a full Linux installation to IDE hard drive with the
ability to boot from disk.

<h2>Getting started</h2>

I suggest to start by reading the various bits of information which are
available about this evaluation board.  Unfortunately, not all of the
information has been collected in one place, but instead it is spread
around several places.  The first document to read is definitely the BCM91250A
Evaluation Board User Manual, followed by the CFE manual found in CFE's tar
ball.

<h2>Technical Information</h2>

<ul>

<li><a href = "hardware/">Hardware which works on the BCM91250A</a>: the
BCM91250A has standard PCI slots (32 and 64 bit, 3.3v only) but not all PCI
cards (especially graphics cards) are supported.  This page lists some of
the hardware which has been tested on the BCM91250A.</li>

<li><a href = "installing-debian/">Installing Debian on the BCM91250A</a>:
this page offers detailed instructions about installing Debian on an IDE
hard drive connected to the BCM91250A. (Note: this is no longer
supported)</li>

<li><a href = "cfe/">CFE</a> and the BCM91250A: upgrade your firmware and
install a version which supports big and little endian.</li>

</ul>

<h2>Resources</h2>

<ul>

<li>There is a <a href =
"http://www.bitmover.com/mailman/listinfo/sibyte-users">sibyte-users</a>
mailing list for users of Broadcom/SiByte evaluation boards and technical
discussion of SiByte processors.</li>

</ul>

<h2>Help</h2>

If you need any help getting Debian running on your BCM91250A after reading
this installation guide and using Google, you can contact the <a href =
"http://lists.debian.org/debian-mips/">Debian MIPS</a> mailing list.

A note for individuals who do not have such an evaluation board yet and
wish to have one after reading this page: unfortunately, these boards are
not made for end-users and given the low production run they are too
expensive for individuals to acquire.

