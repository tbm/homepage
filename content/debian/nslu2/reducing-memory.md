---
title: Tips for reducing memory usage
description: Tips for reducing memory usage
keywords: [Debian, NSLU2, Linksys NSLU2, memory, RAM, usage]
---

<% content_for :right do %>
<img src = "../images/r_nslu2_front.jpg" class="border" alt="A NSLU2 from the front" width="148" height="218" />
<% end %>

<h1>Tips for reducing memory usage</h1>

<h2>by David Härdeman &lt;david@hardeman.nu&gt;</h2>

<em>Note:</em> this document currently describes Debian etch (4.0) and
needs to be updated to Debian squeeze (6.0) and Debian wheezy (7.0).
Some of the hints may still apply, but some may not.

<ul>

<li>If you do not have a serial port on your NSLU2, you can remove the
getty on the serial line by commenting the corresponding line in
`/etc/inittab`, e.g. change the line

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

<li>If you are not using LVM, `/etc/init.d/libdevmapper1.02` will
still load the device-mapper kernel modules.  Since libblkid1 depends on
libdevmapper1.02 and mount depends on libblkid1, it is not possible to
remove libdevmapper1.02.  Instead you can prevent the script from loading
the modules by inserting

<div class="code">
<pre>
exit 0
</pre>
</div>

on the second line of `/etc/init.d/libdevmapper1.02`.</li>

<li>If you are not using IPv6, you can prevent the module from being
automatically loaded by adding the line

<div class="code">
<pre>
blacklist ipv6
</pre>
</div>

to `/etc/modprobe.d/blacklist`. The same goes for any other kernel
module which is automatically loaded which you know you won't need.</li>

<li>Removing daemons that are not needed will of course also help.
Starting aptitude and marking all packages as auto-installed by selecting
the `Installed packages` line and pressing `M`, and
thereafter checking through the list and manually marking the packages you
want to keep by pressing `+` is usually a good start.</li>

<li>openbsd-inetd will only start if there are services activated in
`/etc/inetd.conf`.  Often the only services provided are old Unix
services which are not necessary and inetd can be disabled by commenting
all services in `/etc/inetd.conf`.</li>

</ul>

This article has been contributed by David Härdeman &lt;david@hardeman.nu&gt;

Go back to the <a href = "..">Debian on NSLU2</a> page.

