---
title: Installing Debian on HP t5325
nav: Installation
description: Installation instructions for Debian on the HP t5325 Thin Client
keywords: [Debian, NAS, HP, t5325, thin client]
---

<h1>Installing Debian on HP t5325</h1>

<em>Note: first of all, if you follow these instructions you'll end up with
a system that does not boot.  I no longer have to look into this... so
continue Debian on the HP t5325 as unsupported.</em>  Below are some
installation instructions.

<h2>Configure the device</h2>

First of all, you have to use the HP operating system to change some
settings.  Start the HP system, click on the HP logo and choose
`Administrator/User Mode Switch`.  Enter the administrative password (in my
case, this was `root`).  Then go to the ThinPro Control Center, open
Control Panel, go to Management and then click on SSHD Manager.  Enable
`Enable Incoming Secure Shell Access` and click on OK.

Then go to System Information in the ThinPro Control Center, choose Network
and write down the IP address for eth0.

From another system, connect to your HP t5325 via SSH.  Login as root.  Now
you have to change the `thinpro` environment variable.  We want to change
the load address from 0x200000 to 0x800000 so it's possible to load Debian.
If you make a mistake here, you may need a serial console to recover, so
please make sure you type exactly what is written here:

<div class="code">
<pre>
fw_printenv thinpro
fw_setenv thinpro 'ide reset; ext2load ide 0:1 0x800000 /boot/uImage; wol; setenv bootargs ${thinpro_bootargs}; bootm 0x800000'
fw_printenv thinpro
</pre>
</div>

The `fw_printenv` calls are there so you can verify that only the load
address was changed from 0x200000 to 0x800000.

Now shut down the device.

<h2>Loading Debian installer</h2>

Format a USB stick with VFAT, create a directory called `boot` and download
the installer files to this directory.

Connect the USB stick to the HP device and press power.  After a second,
press power again so the device will load the image from USB.  Debian
installer will now load.

<h2>Installation</h2>

Beware:

<ul>

<li>Partitioner: make a single ext2/ext3 partition.  The partitioner will
complain that there's no swap space but just ignore this.</li>

<li>Software selection: deselect everything, including Standard system
utilities; there is not enough space.</li>

</ul>

<h2>After installation</h2>

The system will fail to boot.  Maybe we have to modify `thinpro_bootargs`
too?

Login and run the following command to remove some temporary files to make
more space:

<div class="code">
<pre>
apt-get clean
</pre>
</div>

