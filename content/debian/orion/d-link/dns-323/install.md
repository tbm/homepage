---
title: Installing Debian on the D-Link DNS-323
nav: Installing Debian
description: Installation instructions for Debian on the D-Link DNS-323
keywords: [Debian, D-Link, DNS-323, Conceptronic, CH3SNAS, installation]
---

<% content_for :right do %>
<img src = "../images/r_ch3snas_front.jpg" class="border" alt="Conceptronic CH3SNAS from the front" width="148" height="146" />

<%= render "adsense-wideskyscaper-right" %>
<% end %>

<h1>Installing Debian on the D-Link DNS-323 and Conceptronic CH3SNAS</h1>

<h2>Overview</h2>

In a nutshell, the installation of Debian on your D-Link DNS-323 or
Conceptronic CH3SNAS device works like this: you use the original firmware
of your device to install a "firmware upgrade" which in reality contains
the Debian installer.  When you restart your device, Debian installer
starts and allows you to login via SSH to perform the installation.  Debian
will be installed to disk and a Debian kernel will be put in flash that
will start Debian from disk.

If you follow this procedure, Debian will be installed to your SATA disk
and the original firmware in flash will be replaced with Debian and your
disk will be erased.  Since Debian is installed on disk, your machine will
not boot without the disk.  Debian does not install a web interface to
configure your machine, although it's possible to install such software.
Furthermore, the D-Link DNS-323 and Conceptronic CH3SNAS devices don't have
a recovery mechanism that would allow you to load a firmware image via the
network.  If something goes wrong, you'll have to connect a serial console
to access the <a href = "../recovery/">recovery mechanism</a>.  Please
proceed only if you want to replace your firmware with Debian and if you
can make a <a href = "http://dns323.kood.org/hardware:serial">serial
console</a> for your device in case there are problems.  If you don't want
to replace the original firmware in flash or retain the capability of
booting without a disk, you can install a <a href =
"http://dns323.kood.org/howto:install_debian">Debian chroot</a> instead.

<h2>Requirements and Preparation</h2>

In order to install Debian, you need the following:

<ul>

<li>A D-Link DNS-323 (revision A1 or B1; C1 is not supported!) or a
Conceptronic Grab'n'GO CH3SNAS.</li>

<li>An internal SATA disk in the device.</li>

<li>A network connection.</li>

<li>Another machine on which you have an SSH client.  SSH is included in
every Linux distribution as OpenSSH and there is <a href =
"http://www.chiark.greenend.org.uk/~sgtatham/putty/download.html">PuTTY</a>
for Windows.</li>

<li>While a <a href = "http://dns323.kood.org/hardware:serial">serial
console</a> is not required for the installation, you have to be able to
make one in case something goes wrong during the installation or later
during the operation of Debian.</li>

</ul>

<h2>Making a Backup</h2>

You have to make a backup of all the data stored on your D-Link or
Conceptronic device before starting with the installation of Debian since
Debian will format the whole disk during the installation.

<h2>Starting the Installer</h2>

First of all, check in the original firmware that your network settings are
correct.  The Debian installer will use the same settings as your original
firmware, so please choose either DHCP or configure a valid IP address,
gateway and DNS.

Now you can go ahead and download the installer image to your PC.  Please
download the right image for your device:

<ul>

<li><a href = "http://ftp.nl.debian.org/debian/dists/stable/main/installer-armel/current/images/orion5x/network-console/d-link/dns-323/netboot.img">D-Link DNS-323</a></li>

<li><a href = "http://ftp.nl.debian.org/debian/dists/stable/main/installer-armel/current/images/orion5x/network-console/conceptronic/ch3snas/netboot.img">Conceptronic CH3SNAS</a></li>

</ul>

Now you can access the admin interface of your device with your web browser
in order to install the firmware image containing the Debian installer.
Log in as user `admin` (the default password is empty), go to `Tools` and
choose `Firmware`.  Hit the `Browse` button and select the installer image
you downloaded before (look for `netboot.img`).  Press `Apply` and the
Debian installer will be written to flash.  When the firmware update has
completed, restart your device.  After a few minutes, you will be able to
connect to the Debian installer.

Here's what the firmware upgrade process looks like on the Conceptronic
CH3SNAS:

<p><img src = "../images/firmware-select.png" class="border" alt = "Firmware upgrade: selected the firmware image" width="887" height="498" /></p>

<p><img src = "../images/firmware-update.png" class="border" alt = "Firmware upgrade: update is in progress" width="695" height="214" /></p>

<p><img src = "../images/firmware-successful.png" class="border" alt = "Firmware upgrade: successful update" width="697" height="157" /></p>

<p><img src = "../images/firmware-restart.png" class="border" alt = "Firmware upgrade: restarting the device" width="482" height="336" /></p>

The firmware upgrade page on the D-Link DNS-323 looks very similar:

<p><img src = "../images/firmware-select-dns323.jpg" class="border" alt = "Firmware upgrade on the D-Link DNS-323" width="650" height="418" /></p>

<h2><a id = "install">The Installation</a></h2>

After you have flashed the Debian installer image and restarted your
device, the Debian installer will start.  Since the DNS-323 and CH3SNAS do
not have any IO device, SSH will be used for the installation.  The
installer will bring up the network, start the OpenSSH server and you can
then connect to the device using SSH.  You have to wait a few minutes after
starting the system before you can connect.  Unfortunately, the installer
currently doesn't use the LED to signal when it's ready, so you just have
to wait a few minutes.

Since the DNS-323 and CH3SNAS do not have an LCD, the installer cannot tell
you which IP address to connect to or which password to use.  With regards
to the IP address, the following strategy is used:

<ul>

<li>If your original firmware is configured to use DHCP (the default
configuration from D-Link and Conceptronic), Debian installer will try to
acquire an IP address with DHCP.  You can use the MAC address listed at the
bottom of your device to tell your DHCP server to give out a specific IP
address to your machine.</li>

<li>If you configured a static address in your original firmware, this
configuration will be used.  However, if your network configuration was
incomplete (e.g. IP address or DNS were missing), the installer will use
DHCP instead.</li>

<li>If DHCP is used but your DHCP server does not respond, the installer
will use the fallback address `192.168.0.32`.  This is the default IP
address used by the D-Link firmware, but please note that it is different
to the default IP address from the Conceptronic firmware.  If you are
unsure what the address of your device is, unplug the Ethernet cable, start
the machine again, wait until Debian installer is ready for SSH and then
plug the cable back in and connect to this fallback address.</li>

</ul>

Please make sure that your device is on a local network to which only you
have access since the installer uses a very generic password, namely
`install`. The user is `installer`.  Connect to the installer (again,
replacing the address in the example with the actual IP address of your
device):

<div class="code">
<pre>
ssh installer@<span class="input">192.168.1.100</span>
</pre>
</div>

**Important note:** When you connect to the installer, one of the first
screens will allow you to select additional installer modules.  Make sure
to select the `ext3` module.  If you don't select the `ext3` module, the
installer will not work correctly due to <a
href="http://bugs.debian.org/729445">a bug</a>.

The installation itself should be pretty standard and you can follow the <a
href = "http://www.debian.org/releases/stable/armel/">installation
guide</a>.  The installer knows about the DNS-323 and CH3SNAS and at the
end of the installation it will flash a kernel and ramdisk that will
automatically boot into Debian.

Since your device boots from flash you don't have many limitations as to
how you partition your hard drive.  You can use LVM and RAID and a number
of filesystems.

At the end of the installation, the installer will write the new kernel to
flash.  Afterwards you will get a confirmation that the installation is
complete.  Confirm, wait for the installer to finish and once your SSH
session terminates, wait a few minutes before you can connect to your newly
installed system via SSH.  You will be able to log in as `root` or your
newly created user.

<h2>Success</h2>

You should now have a complete Debian system running on your DNS-323 or
CH3SNAS.  You can use `apt-get` and other tools to install additional
software.  The D-Link DNS-323 and Conceptronic CH3SNAS are ARM based
devices and the `armel` architecture is fully supported by Debian.

Finally, make sure to read the <a href = "../tips/">tips and tricks</a>
about running Debian on the D-Link DNS-323 and Conceptronic CH3SNAS.  In
case you run into any bugs or problems, you may want to check the list of
<a href = "../known-issues/">known issues and bugs</a>.

Go back to my <a href = "..">Debian on D-Link DNS-323 and
Conceptronic CH3SNAS</a> page.

<div class="bbf">
<%= render "adsense-banner-before-footer" %>
</div>

