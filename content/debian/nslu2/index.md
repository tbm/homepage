---
title: Debian on NSLU2
description: A page giving useful help for running Debian on the Linksys NSLU2
keywords: [Debian, NAS, NSLU2, Linksys NSLU2, DebianSlug, IXP4xx, SlugDebian]
---

<% content_for :right do %>
<img src = "images/r_nslu2_front.jpg" class="border" alt="A NSLU2 from the front" width="148" height="218" />

<%= render "adsense-wideskyscaper-right" %>
<% end %>

<h1>Debian on the Linksys NSLU2</h1>

The NSLU2 from Linksys is a small, sub $100 device that can be used for a
variety of tasks.  NSLU2 stands for Network Storage Link for USB 2.0 Disk
Drives, a description which pretty much summarizes the original purpose of
this device.  However, the NSLU2 (or Slug, as it's often referred to) can
be used for other tasks if you use a more powerful firmware for it.  Since
the device offers two USB ports, it's possible to connect a USB disk and
run a full Debian system on it.

In the following, I will describe what is needed to get Debian running on
your NSLU2.  Please note that this page only provides information on
running a full-blown Debian system on the NSLU2 on an external USB drive.
If you're looking for a firmware to be put in the flash of the NSLU2 (such
as Unslung or OpenSlug) or other information on this device, please go to
the <a href = "http://www.nslu2-linux.org/">NSLU2-Linux project</a> (in
particular, check out the <a href =
"http://www.nslu2-linux.org/wiki/FAQ/FirmwareMatrix">firmware matrix</a>).

Finally, please note that the NSLU2 is a very low-end device by today's
standards.  In particular, the NSLU2 has only 32 MB of RAM, which is not
much to run a modern operating system like Debian 6.0 (squeeze).  The
easy-to-use Debian installer is no longer available for the NSLU2 because
the device does not have enough RAM.  While it's still possible to install
Debian on the NSLU2 using the manual method described on this page, I
suggest you upgrade to a more modern devices, such as a <a href =
"../kirkwood/sheevaplug">SheevaPlug</a> or a <a href =
"../kirkwood/qnap">NAS device from QNAP</a>.

<h2>Information</h2>

<ul>

<li>An <a href = "unpack">installation guide</a> for Debian on the Linksys
NSLU2.</li>

<li>A set of <a href = "faq">Frequently Asked Questions (FAQ)</a>.</li>

<li><a href = "troubleshooting">Troubleshooting information</a> with common
problems and their solutions.</li>

<li>Some <a href = "tips">tips and tricks</a> about running Debian on the
Linksys NSLU2.</li>

<li>An <a href = "gallery">image gallery</a> with various pictures showing
the internals of the NSLU2.</li>

<li>An <a href = "specs">internals page</a> listing the specs of the
Linksys NSLU2.</li>

<li>Some advances guides: <a href = "clone">cloning a NSLU2</a> and <a href
= "repack">modifying a NSLU2 flash image</a>.  You can also find an <a href
= "boot">explanation of the boot process</a> of the NSLU2 running
Debian.</li>

</ul>

<h2>External Resources</h2>

<ul>

<li>The <a href = "http://www.nslu2-linux.org/">NSLU2-Linux project</a>
provides lots of information regarding Linux on the NSLU2.</li>

<li>Peter Korsgaard's guide on <a href =
"http://peter.korsgaard.com/articles/debian-nslu2.php">manually installing
Debian sarge</a>.  This is only of historical interest now that
debian-installer supports the NSLU2.</li>

</ul>

<h2>Help</h2>

If you have problems with Debian on NSLU2 and cannot solve them with
Google, there are the following resources you can consult:

<ul>

<li>The <a href = "http://lists.debian.org/debian-arm/">debian-arm list</a>
for questions specifically related to the installation or operation of
Debian on the NSLU2.</li>

<li>The <a href =
"http://www.nslu2-linux.org/wiki/Main/MailingLists">mailing lists</a> of
the NSLU2-Linux project for generic questions regarding Linux on
NSLU2.</li>

</ul>

<h2>Acknowledgements</h2>

I'd like to thank the <a href = "http://www.nslu2-linux.org/">NSLU2-Linux
project</a> for all their work on getting a modern version of Linux running
on this device and writing lots of documentation describing how this device
actually works.  Without their work, getting Debian to run would have been
much harder.  In particular, I'd like to thank Alessandro Zummo and John
Bowler for their kernel work and Rod Whitby for getting me excited about
the NSLU2 and answering all of the questions I asked while porting Debian
to this device.  Gordon Farquharson has done lots of testing of Debian on
NSLU2.  Joey Hess maintains the `nslu2-utils` package in Debian.  Finally,
I'd like to thank the <a href = "http://www.nslu2-linux.org/">NSLU2-Linux
project</a> again for donating a NSLU2 to me to help with Debian porting
efforts.

<div class="bbf">
<%= render "adsense-banner-before-footer" %>
</div>

