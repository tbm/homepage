---
title: Tips and tricks for Debian on OpenRD
nav: Tips
description: Tips and tricks for Debian on OpenRD
keywords: [Debian, OpenRD, VGA, xgi, tips, tricks]
---

<h1>Tips and tricks for Debian on OpenRD</h1>

Here are some tips and tricks about running Debian on the OpenRD.

<h2><a id = "vga">Making use of the VGA chip</a></h2>

The OpenRD-Client and OpenRD-Ultimate feature a graphics chip from XGI.
This section describes how you can configure your machine so you can use
it as a desktop.

First of all, edit `/etc/inittab` and make sure that the getty entries for
tty1 to tty6 are activated (in other words: not commented out).

Then edit `/etc/initramfs-tools/modules` and add the following two lines:

<div class="code">
<pre>
xgifb
fbcon
</pre>
</div>

Now run the following command in order to activate this change:

<div class="code">
<pre>
update-initramfs -u
</pre>
</div>

The graphics driver is now included in the ramdisk that Debian loads
during the boot process.  This means that you'll be able to see boot
messages on your screen.

Finally, you have to restart your machine to configure the boot loader
so that boot messages from Linux will be shown on the screen.  Reboot
and issue the following commands in u-boot:

<div class="code">
<pre>
setenv bootargs_console console=ttyS0,115200 console=tty0
saveenv
run bootcmd
</pre>
</div>

When Debian boots, you will now see the boot process on the screen.

If you want to run a graphical user environment, you can install X.Org
and start X:

<div class="code">
<pre>
apt-get install xorg
startx
</pre>
</div>

X.Org will start without a configuration file.  However, if you want to
change the screen resolution, you have to create a simple configuration
file for X.Org (see <a href = "../files/xorg.conf">this example</a>).

If you want to install a full desktop environment, you can run `tasksel`
and choose `Graphical desktop environment`.

Go back to my <a href = "..">Debian on OpenRD</a> page.

<%= render "paypal", :desc => "Debian/OpenRD donation" %>

