---
title: Installing Debian on QNAP TS-21x/TS-22x
nav: Installing Debian
description: Installation instructions for Debian on QNAP TS-21x/TS-22x
keywords: [Debian, QNAP, HS-210, TS-210, TS-212, TS-212-E, TS-212P, TS-219, TS-219P, TS-219P+, TS-220, TS-221, ARM, armel, installation]
---

<% content_for :right do %>
<img src = "../images/r_ts219p.jpg" class="border" alt="Open QNAP TS-219" width="148" height="188" />
<% end %>

<h1>Installing Debian on QNAP HS-210, TS-21x and TS-22x devices</h1>

<h2>Overview</h2>

In a nutshell, the installation of Debian on your QNAP HS-210, TS-21x or TS-22x works like
this: you use the QNAP firmware to write a Debian installer image to flash.
When you restart your device, Debian installer starts and allows you to
login via SSH to perform the installation.  Debian will be installed to
disk and a Debian kernel will be put in flash that will start Debian from
disk.

If you follow this procedure, Debian 8 (jessie) will be installed to
your SATA disk and the QNAP firmware on disk and in flash will be replaced
with Debian.  Debian does not install a web interface to configure your
machine, although it's possible to install such software.  If this is not
what you want, please don't proceed with the installation.

<h2>Requirements and Preparation</h2>

In order to install Debian on a QNAP TS-21x/TS-22x device, you need the following:

<ul>

<li>A QNAP HS-210, TS-210, TS-212, TS-212-E, TS-212P, TS-219, TS-219P, TS-219P+, TS-219P II, TS-220 or TS-221.</li>

<li>An internal SATA disk.</li>

<li>A network connection.</li>

<li>Another machine on which you have a telnet and an SSH client.  Telnet
is included in Linux and Windows.  SSH is included in every Linux
distribution as OpenSSH and there is <a href =
"http://www.chiark.greenend.org.uk/~sgtatham/putty/download.html">PuTTY</a>
for Windows.</li>

</ul>

<h2>Making a Backup</h2>

You have to make a backup of all the data stored on your QNAP before
starting with the installation of Debian since Debian will format the whole
disk during the installation.  Also, Debian will replace the QNAP firmware
in flash, so it's also recommended to make a copy of the flash (mtd)
partitions.  Debian will only modify two flash partitions but
it's a good idea to keep a copy of all partitions as you may need them to
use the recovery mode.  More detailed instructions for making a backup of
your flash partitions will be given later.

<h2>Starting the Installer</h2>

Start your QNAP device and login via SSH.  Some time after you start your
machine, you will hear a beep and a bit later you'll hear a longer beep.
Wait for a few more seconds and then connect to the machine via SSH.  The
username is `admin` and the password is `admin` too.

Once you are logged in, you can save the content of your flash partitions
to a USB stick.  Connect a USB stick to your QNAP and wait for the system
to mount it.  In my case, it was mounted at `/share/external/sdi1` but you
can find the location with the following command:

<div class="code">
<pre>
mount | grep external
/dev/sdi1 on /share/external/<span class="input">sdi1</span> type vfat [...]
</pre>
</div>

On systems that have never been initialized with the QNAP firmware, the
VFAT module may not be available.  If your USB stick does not get mounted,
put it back in your PC and format it with the `ext3` or `ext4` filesystem.

Now go to this directory and make a backup of your flash partitions:

<div class="code">
<pre>
cd /share/external/sdi1
cat /dev/mtdblock0 &gt; mtd0
cat /dev/mtdblock1 &gt; mtd1
cat /dev/mtdblock2 &gt; mtd2
cat /dev/mtdblock3 &gt; mtd3
cat /dev/mtdblock4 &gt; mtd4
cat /dev/mtdblock5 &gt; mtd5
cd
umount /share/external/sdi1
</pre>
</div>

Disconnect your USB stick from your QNAP, connect it to your PC and to add
the `mtdX` files to your regular backup.

Now you can go ahead and download the installer.

<h3><a id = "download">Download and Flash the Installer</a></h3>

Issue the following commands to download the Debian installer images:

<div class="code">
<pre>
cd /tmp
busybox wget http://ftp.debian.org/debian/dists/stable/main/installer-armel/current/images/kirkwood/network-console/qnap/ts-219/initrd.gz
busybox wget http://ftp.debian.org/debian/dists/stable/main/installer-armel/current/images/kirkwood/network-console/qnap/ts-219/kernel
busybox wget http://ftp.debian.org/debian/dists/stable/main/installer-armel/current/images/kirkwood/network-console/qnap/ts-219/flash-debian
busybox wget http://ftp.debian.org/debian/dists/stable/main/installer-armel/current/images/kirkwood/network-console/qnap/ts-219/model
</pre>
</div>

These commands will download the Debian kernel, the installer ramdisk, a
file with information about the support QNAP model, and a script to write
the kernel and ramdisk to flash.  You can now run the script by executing
the following command:

<div class="code">
<pre>
sh flash-debian
</pre>
</div>

Please note that this command will take about three minutes to run.  You
will see the following on your screen:

<div class="code">
<pre>
Updating MAC address...
Your MAC address is 00:08:9B:8C:xx:xx
Writing debian-installer to flash... done.
Please reboot your QNAP device.
</pre>
</div>

Once the command has completed, you can reboot your QNAP device:

<div class="code">
<pre>
reboot
exit
</pre>
</div>

<h2><a id = "install">The Installation</a></h2>

After you have flashed the Debian installer image and restarted your QNAP
device, the Debian installer will start.  Since the TS-21x/TS-22x does not have
any IO device, SSH will be used for the installation.  The installer will
bring up the network, start the OpenSSH server and you can then connect to
the device using SSH.  You have to wait a few minutes after starting the
system before you can connect.  When the installer is ready, the status LED
will change to solid green and your device will beep briefly to indicate
that you can now login via SSH.

<a id = "net-config"></a>

Since the TS-21x/TS-22x does not have an LCD, the installer cannot tell you which
IP address to connect to or which password to use.  With regards to the IP
address, the following strategy is used:

<ul>

<li>If your QNAP firmware is configured to use DHCP (the default
configuration from QNAP), Debian installer will try to acquire an IP
address with DHCP.  If you have not initialized your QNAP firmware with
QFinder, DHCP will be used.  You can use the MAC address of your QNAP
device to tell your DHCP server to give out a specific IP address to your
machine.</li>

<li>If you configured a static address in your QNAP firmware, this
configuration will be used.  However, if your network configuration was
incomplete (e.g. IP address or DNS were missing), the installer will use
DHCP instead.</li>

<li>If DHCP is used but your DHCP server does not respond, the device will
use the fallback address `192.168.1.100`.  If you are unsure what the
address of your QNAP is, unplug the Ethernet cable, start the machine
again, wait until Debian installer is ready for SSH and then plug the cable
back in and connect to this fallback address.</li>

</ul>

Please make sure that the QNAP is on a local network to which only you
have access since the installer uses a very generic password, namely
`install`. The user is `installer`.  Before you can connect to the
installer via SSH, you have to remove the SSH key from the QNAP firmware
from your `known_hosts` file:

<div class="code">
<pre>
ssh-keygen -f ~/.ssh/known_hosts -R <span class="input">192.168.1.100</span>
</pre>
</div>

Now connect to the installer (again, replacing the address in the
example with the actual IP address of your QNAP) and login as user
`installer` with the password `install`:

<div class="code">
<pre>
ssh installer@<span class="input">192.168.1.100</span>
</pre>
</div>

The installation itself should be pretty standard and you can follow the <a
href = "http://www.debian.org/releases/stable/armel/">installation
guide</a>.  The installer knows about the TS-21x/TS-22x and at the end of the
installation it will flash a kernel and ramdisk that will automatically
boot into Debian.  It will also install the `qcontrol` package that can be
used to control the fan, LEDs and beeper on your QNAP device.

Since the TS-21x/TS-22x boots from flash you don't have many limitations as to how
you partition your hard drive.  You can use LVM and RAID and a number of
filesystems.

At the end of the installation, the installer will write the new kernel to
flash.  Afterwards you will get a confirmation that the installation is
complete.  Confirm, wait for the installer to finish and once your SSH
session terminates, wait a few minutes before you can connect to your newly
installed system via SSH.  Your QNAP device will beep when you can connect via
SSH.  You will be able to log in as `root` or your newly created user.

<h2>Success</h2>

You should now have a complete Debian system running on your QNAP.  You can
use `apt-get` and other tools to install additional software.  The
TS-21x/TS-22x is an ARM based device and the `armel` architecture is fully
supported by Debian.

Finally, make sure to read the <a href = "../tips/">tips and tricks</a>
about running Debian on the QNAP TS-21x/TS-22x.

Go back to my <a href = "..">Debian on QNAP TS-21x/TS-22x</a> page.

<%= render "paypal", :desc => "Debian/QNAP TS-21x/TS-22x donation" %>

