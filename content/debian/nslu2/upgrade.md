---
title: Upgrading Debian on NSLU2
nav: Upgrading Debian
description: Upgrade instructions for Debian on Linksys NSLU2
keywords: [Debian, NSLU2, Linksys NSLU2, DebianSlug, IXP4xx, SlugDebian]
---

<% content_for :right do %>
<img src = "../images/r_nslu2_front.jpg" class="border" alt="A NSLU2 from the front" width="148" height="218" />

<%= render "adsense-wideskyscaper-right" %>
<% end %>

<h1>Upgrading Debian on the Linksys NSLU2</h1>

If you have installed Debian on your NSLU2 using debian-installer beta2 of
Debian etch (version 4.0) you need to follow the manual upgrade described
below.  Please note that debian-installer beta2 of Debian etch was released
several years ago and it's unlikely that you have to follow these steps.
So first of all, you should check whether you actually need to do this
upgrade process because most users don't.  If the output of the command
`uname -r` contains the string `ixp4xx` and the file `/proc/mtd` has a line
ending with `"Loader"` you don't have to follow the instructions here.  In
this case, you can simply upgrade your Debian system with these two
commands:

<div class="code">
<pre>
apt-get update
apt-get dist-upgrade
</pre>
</div>

On the other hand, if `uname -r` contains the string `nslu2` and your
`/proc/mtd` doesn't include the string `"Loader"`, you have to proceed with
the following instructions.  Please make sure that you and perform the
commands as user `root`.

<ol>

<li>

Edit `/etc/apt/sources.list` and make sure that APT is pointed at etch.
Then run:

<div class="code">
<pre>
apt-get update
</pre>
</div>

If you get errors from APT saying that it `couldn't stat source package
list`, then you have to switch to a mirror that carries ARM binaries:
`http://us.arm.mirror.debian.net`

</li>

<li>

Edit `/etc/kernel-img.conf` and remove the line starting with
`postinst_hook` (if there is one) and make sure there is a line

<div class="code">
<pre>
do_initrd = yes
</pre>
</div>

</li>

<li>

If `/lib/firmware/NPE-B` doesn't exist on your machine yet, please download
<a href = "http://www.cyrius.com/debian/nslu2/files/NPE-B">Intel's
proprietary NPE-B microcode</a> and put save it in `/lib/firmware`.

</li>

<li>

Install the new kernel:

<div class="code">
<pre>
apt-get install linux-image-2.6-ixp4xx
</pre>
</div>

</li>

<li>Edit `/etc/network/interface` and remove all `pre-up` lines that
mention `ixp400`.</li>

<li>

Turn your NSLU2 off, and put it into <a href =
"../install/#upgrade-mode">upgrade mode</a>.

</li>

<li>

On another Linux PC, install <a href =
"http://www.nslu2-linux.org/wiki/Main/UpSlug2">upslug2</a>.

</li>

<li>

Download http://www.cyrius.com/debian/nslu2/files/sda1-2.6.18-6.bin

</li>

<li>

Flash this new image:

<div class="code">
<pre>
upslug2 -i sda1-2.6.18-6.bin
</pre>
</div>

</li>

<li>

Once upslug2 has flashed the new image, it will reboot and have the new
layout.

</li>

<li>

Install the 2nd boot loader and a new package to flash the kernel:

<div class="code">
<pre>
apt-get install flash-kernel apex-nslu2 nslu2-utils
</pre>
</div>

</li>

<li>

Edit `/etc/kernel-img.conf` and add the following line:

<div class="code">
<pre>
postinst_hook = flash-kernel
</pre>
</div>

</li>

<li>

You can now remove the old nslu2 kernel:

<div class="code">
<pre>
apt-get remove linux-image-2.6-nslu2
</pre>
</div>

</li>

</ol>

<div class="bbf">
<%= render "adsense-banner-before-footer" %>
</div>

