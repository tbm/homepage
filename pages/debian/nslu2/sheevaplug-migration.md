---
title: Migrate Debian on NSLU2 to SheevaPlug
nav: Migration to SheevaPlug
description: Migrate Debian on NSLU2 to SheevaPlug
keywords: [NSLU2, Linksys NSLU2, Marvell, SheevaPlug, migration]
---

<div class="right">
<img src = "../images/r_nslu2_front.jpg" class="border" alt="A NSLU2 from the front" width="148" height="218" />
</div>

While the Linksys NSLU2 is a nice device, its performance does not meet the
requirements of today's software.  A great alternative to the NSLU2 is the
<a href = "/debian/kirkwood/sheevaplug/">SheevaPlug from Marvell</a>, a
sub-100$ device that offers 512 MB of RAM and a 1.2 GHz CPU.  The following
guide describes how you can migrate your existing Debian installation from
your NSLU2 to a SheevaPlug.  Please note that the Debian installer is <a
href = "/debian/kirkwood/sheevaplug/install/">supported on the
SheevaPlug</a>.  If you want to keep your NSLU2 installation in addition to
the SheevaPlug, I suggest you perform a new installation.  This guide
describes how to migrate your <em>existing</em> Debian installation to the
SheevaPlug.

There are some important notes that you should keep in mind before going
ahead with this migration:

<ul>

<li>This guide is written in a way that you change your NSLU2 installation
in a way that you cannot go back.  After making the changes described here,
your drive won't work with the NSLU2 anymore.  It is therefore a good idea
to first make a backup of your data to another drive. (See the <a href =
"../clone/">NSLU2 cloning guide</a> on how to make a 1:1 copy of your USB
drive.)</li>

<li>Support for USB hard disks is currently quite broken on the SheevaPlug.
You can go ahead if you want to migrate a USB stick.  But if you have a USB
hard drive, I suggest you either wait for a new version of the boot loader
for SheevaPlug with better USB support or you copy your disk to a USB stick
and migrate that.</li>

<li>This guide assumes that you migrate from USB.  If you want to migrate
from a USB drive on the NSLU2 to a SD card on the SheevaPlug, please <a
href = "/contact/">contact me</a> and I'll try to extend this guide.</li>

</ul>

<h2>The migration</h2>

First of all, you have to check which flavour of the ARM port you're
running:

<div class="code">
<pre>
dpkg --print-architecture
</pre>
</div>

There is the old `arm` port as well as the new `armel` port (based on ARM
EABI).  If you're running the old `arm` port you're unfortunately out of
luck since Debian on the SheevaPlug is not supported for the old `arm`
port.  In this case, you have to perform a new <a href =
"/debian/kirkwood/sheevaplug/">installation on the SheevaPlug</a>.  If
you're using the `armel` port, you can continue.

The Debian installer has configured `initramfs-tools` to put only modules
you actually need into the ramdisk.  Since we have to generate a ramdisk
for a different device, this strategy won't work.  We therefore remove that
configuration for `initramfs-tools` (another reason for removing it is that
it doesn't make much sense on the SheevaPlug):

<div class="code">
<pre>
rm -f /etc/initramfs-tools/conf.d/driver-policy
</pre>
</div>

Next, edit `/etc/kernel-img.conf` and check if there is a line like this:

<div class="code">
<pre>
postinst_hook = flash-kernel
</pre>
</div>

If so, remove this line and save the file.  The `postinst_hook` is no
longer necessary and will cause problems during this migration.

udev contains a rules file to ensure that your Ethernet device will remain
consistent.  This is based on the MAC address, which will of course change
when you move to the SheevaPlug.  Therefore, edit
`/etc/udev/rules.d/70-persistent-net.rules`, remove the existing rules and
add the following rule which will work with all SheevaPlug devices
(independent of the MAC address):

<div class="code">
<pre>
# Unknown net device (/class/net/eth0) (mv643xx_eth_port)
SUBSYSTEM=="net", ACTION=="add", DRIVERS=="mv643xx_eth_port", ATTR{type}=="1", KERNEL=="eth*", NAME="eth0"
</pre>
</div>

Let's remove some packages that are NSLU2-specific:

<div class="code">
<pre>
apt-get --purge remove apex-nslu2 nslu2-utils slugimage
</pre>
</div>

And finally, let's install the kernel for the SheevaPlug.  If you're
running Debian 5.0 (lenny), on your NSLU2 you have to edit
`/etc/apt/sources.list` and add the following line:

<div class="code">
<pre>
deb http://people.debian.org/~tbm/orion lenny main
</pre>
</div>

This is not necessary if you run Debian 6.0 (squeeze) or Debian 7 (wheezy)

Now install the new kernel:

<div class="code">
<pre>
gpg --keyserver pgp.earth.li --recv-keys 68FD549F
gpg --export -a 68FD549F | apt-key add -
mv /usr/sbin/flash-kernel /usr/sbin/flash-kernel.bak
apt-get update
apt-get install flash-kernel uboot-mkimage linux-image-kirkwood
mv /usr/sbin/flash-kernel.bak /usr/sbin/flash-kernel
flash-kernel --machine "Marvell SheevaPlug Reference Board"
</pre>
</div>

Now you can disconnect your drive and connect it to the SheevaPlug.  Make
sure to configure it to boot from USB according to the <a href =
"/debian/kirkwood/sheevaplug/install/">instructions in the install
guide</a>.

Your SheevaPlug will now boot your existing Debian installation!

Now that everything is working, you can remove the NSLU2 kernel packages:

<div class="code">
<pre>
apt-get remove --purge linux-image-2.6-ixp4xx
dpkg -l | grep linux-image-2.6 | grep ixp4xx
</pre>
</div>

Look at the output of the last command and remove the packages with
`apt-get remove --purge`.

You're done.  Enjoy your SheevaPlug!

