---
title: Tips for reducing memory usage
description: Tips for reducing memory usage
keywords: [Debian, NSLU2, Linksys NSLU2, memory, RAM, usage]
---

<div class="right">
<img src = "../images/r_nslu2_front.jpg" class="border" alt="A NSLU2 from the front" width="148" height="218" />
</div>

<h2>by David Härdeman &lt;david@hardeman.nu&gt;</h2>

<div class="alert alert-danger">

This document describes Debian etch (4.0).  Some of the hints may still
apply, but some may not.

</div>

<ul>

<li>If you do not have a serial port on your NSLU2, you can remove the
getty on the serial line by commenting the corresponding line in
<code>/etc/inittab</code>, e.g. change the line

<div class="code">
<pre>
T0:23:respawn:/sbin/getty -L ttyS0 115200 linux
</pre>
</div>

to

<div class="code">
<pre>
<span class="input">#</span>T0:23:respawn:/sbin/getty -L ttyS0 115200 linux
</pre>
</div>

then run

<div class="code">
<pre>
telinit q
</pre>
</div>

to tell init to re-read the inittab file.</li>

<li>If you are not using LVM, <code>/etc/init.d/libdevmapper1.02</code> will
still load the device-mapper kernel modules.  Since libblkid1 depends on
libdevmapper1.02 and mount depends on libblkid1, it is not possible to
remove libdevmapper1.02.  Instead you can prevent the script from loading
the modules by inserting

<div class="code">
<pre>
exit 0
</pre>
</div>

on the second line of <code>/etc/init.d/libdevmapper1.02</code>.</li>

<li>If you are not using IPv6, you can prevent the module from being
automatically loaded by adding the line

<div class="code">
<pre>
blacklist ipv6
</pre>
</div>

to <code>/etc/modprobe.d/blacklist</code>. The same goes for any other kernel
module which is automatically loaded which you know you won't need.</li>

<li>Removing daemons that are not needed will of course also help.
Starting aptitude and marking all packages as auto-installed by selecting
the <code>Installed packages</code> line and pressing <code>M</code>, and
thereafter checking through the list and manually marking the packages you
want to keep by pressing <code>+</code> is usually a good start.</li>

<li>openbsd-inetd will only start if there are services activated in
<code>/etc/inetd.conf</code>.  Often the only services provided are old Unix
services which are not necessary and inetd can be disabled by commenting
all services in <code>/etc/inetd.conf</code>.</li>

</ul>

This article has been contributed by David Härdeman &lt;david@hardeman.nu&gt;

