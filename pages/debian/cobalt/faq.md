---
title: FAQ about Debian on Cobalt
nav: Frequently Asked Questions
description: Frequently Answered Questions regarding Debian on Cobalt
keywords: [Debian, Cobalt, FAQ, troubleshooting]
---

<div class="alert alert-danger">

Debian no longer supports MIPS-based Cobalt machines.  This information
is obsolete.

</div>

In the following, a number of frequently asked questions (FAQ) and their
answers are presented.  This may answer some of the questions you have and
may also help with troubleshooting.

<h2>Which devices are supported?</h2>

With the exception of the Qube 2700 (Qube 1), all MIPS based Cobalt devices
are supported.  This includes the Gateway Microserver and the Cobalt RaQ1,
Qube2, and RaQ2.

<h2>Will this installation procedure also work on RaQ3/RaQ4</h2>

No, the installation system described here will only work on MIPS based
Cobalt machines, i.e. RaQ1, Qube2 (Qube 2800) and RaQ2.  As far as I know,
there is no Debian installer that will simply work on those machines.

<h2>Is there an installation routine like NetBSD offers?</h2>

Apparently NetBSD has a CD-ROM which you can put in a PC and then a Cobalt
connected to this PC will automatically be installed.  This is also how the
installation of the old Cobalt OS worked.  I don't plan to support this.
However, debian-installer allows you to do fully automated installations
and you could use that instead.

<h2>Can I put a bigger hard drive in my Cobalt?</h2>

Generally, yes.  I have had reports from people successfully using a
160&nbsp;GB in their Cobalt.  However, there <em>may</em> be some Cobalt
machines with a very old firmware that have a limit of 30&nbsp;GB.  I'm not
really sure whether this restriction exists on some machines though.

<h2>What PCI cards can I put in my Qube?</h2>

The Qube2 has a PCI slot in which one PCI card can be put.  Generally, most
PCI cards should fine and the kernel supplied with Debian includes modules
for a number of cards.  However, please be aware that there is not terribly
much space in the Qube so big PCI card will not fit.  I've heard from
people successfully using USB, SCSI and sound cards in their Qube.

<h2>Where can I find more information regarding Linux on Cobalt?</h2>

The Linux/MIPS project maintains a wiki which has a <a href =
"http://www.linux-mips.org/wiki/Cobalt">page with Cobalt related
information.</a>

