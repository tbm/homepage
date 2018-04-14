---
title: Installing Debian on HP mv2120 and mv5020
nav: Installing Debian
description: Installation instructions for Debian on HP mv2120 and mv5020
keywords: [Debian, HP, mv2120, mv5020, installation]
---

<div class="right">
<img src = "../images/r_mv2120_front.jpg" class="border" alt="HP mv2120 from the front" width="148" height="212" />
</div>

<h1>Installing Debian on the HP mv2120 and mv5020</h1>

<h2>Overview</h2>

In a nutshell, the installation of Debian on your HP mv2120 and mv5020
works like this: you use the recovery mode of the mv2120 to load the Debian
installer image via the network.  Debian installer will start and allow you
to login via SSH to perform the installation.  Debian will be installed to
disk and the mv2120 will directly boot Debian from disk.

If you follow this procedure, Debian will be installed to your SATA disk
and the HP firmware on disk will be replaced with Debian.  Debian does not
install a web interface to configure your machine, although it's possible
to install such software.  If this is not what you want, please don't
proceed with the installation.

<h2>Requirements and Preparation</h2>

In order to install Debian on a HP mv2120, you need the following:

<ul>

<li>A HP mv2120 or compatible device (e.g. HP 5020, mv5140 or mv5150).</li>

<li>An internal SATA disk in the HP mv2120.</li>

<li>A network connection.</li>

<li>Another machine on which you have an SSH client.  SSH is included in
every Linux distribution as OpenSSH and there is <a href =
"http://www.chiark.greenend.org.uk/~sgtatham/putty/download.html">PuTTY</a>
for Windows.</li>

<li>Another machine with either the HP mv2120 recovery tool (Windows) or
uphpmvault (Linux and other systems).</li>

</ul>

<h2>Making a Backup</h2>

You have to make a backup of all the data stored on your HP mv2120 before
starting with the installation of Debian since Debian will format the whole
disk during the installation.

<h2>Starting the Installer</h2>

The HP mv2120 has a recovery mode through which it can request a boot image
via the local network.  This recovery mode will be used to load the Debian
installer.  HP ships a tool for Windows to serve recovery images to your
mv2120 and there is a tool called uphpmvault written by Marc Singer that
does the same on Linux and other systems.  You can obtain the Windows tool
by going to HP's web site.  First, search for `mv2120`, then choose
`Software & driver downloads` and then download the `HP Media Vault
Firmware Recovery Utility`.  uphpmvault is in Debian so you can simply
install it with `apt`.

Once you have installed uphpmvault or the Windows tool, you have to tell
the tool to serve the recovery image.  Download the <a href =
"http://ftp.nl.debian.org/debian/dists/stretch/main/installer-armel/current/images/orion5x/network-console/hp/mv2120/netboot.img">Debian
installer</a> image and start the tool.  If you want to use the Windows
tool, please follow <a href =
"http://tech.groups.yahoo.com/group/hackingthemediavault/message/376">these
instructions</a>.  To use uphpmvault, issue the following command:

<div class="code">
<pre>
uphpmvault netboot.img
</pre>
</div>

Now you have to put your mv2120 into recovery mode:

<ul>

<li>First of all, turn off your mv2120.</li>

<li>Press the reset button and keep it pressed.</li>

<li>Press the power button and keep it pressed.</li>

<li>After a few seconds, your HP mv2120 should go into recovery mode.  Your
recovery tool will say that it's recovering the device.  At this point, you
can release the reset and power buttons.  If the recovery mode doesn't
start within 5 seconds, please turn your device off and try again.</li>

</ul>

uphpmvault will show the MAC address of the mv2120 and will give a status
when it's recovering the device:

<div class="code">
<pre>
uphpmvault netboot.img
HP P2 NAS        00:0a:e4:83:64:1a (192.168.1.132)
Recovering 00:0a:e4:83:64:1a
File is 5849213 bytes in 11425 blocks of 512 bytes
</pre>
</div>

Once the recovery has completed, your HP mv2120 will automatically reboot
and the Debian installer will start.

<h2><a id = "install">The Installation</a></h2>

Since the HP mv2120 does not have any IO device, SSH will be used for the
installation.  The installer will bring up the network, start the OpenSSH
server and you can then connect to the device using SSH.  You have to wait
approximately two minutes after starting the system before you can connect.
When the installer is ready, it will change the health LED to to indicate
that you can now login via SSH.

Here is a list of stages and the corresponding signals the boot process of
Debian installer will go through:

<ul>

<li>Quickly blinking purple: The mv2120 is loading the Debian installer
image.</li>

<li>The SATA light goes on, the health light continues to blink quickly:
the Linux kernel has been loaded.</li>

<li>Health light goes blank: the Debian installer ramdisk has been
loaded.</li>

<li>Slowly blinking blue: Debian installer has finished some critical steps
of its startup process.</li>

<li>Solid blue: Debian installer is ready and you can login via SSH.</li>

</ul>

Since the HP mv2120 does not have an LCD, the installer cannot tell you
which IP address to connect to or which password to use.  With regards to
the IP address, the following strategy is used:

<ul>

<li>If your HP firmware is configured to use DHCP (the default
configuration from HP), Debian installer will try to acquire an IP address
with DHCP.  You can use the MAC address of your mv2120 to tell your DHCP
server to give out a specific IP address to your machine.</li>

<li>If you configured a static address in your HP firmware, this
configuration will be used.  However, if your network configuration was
incomplete (e.g. IP address or DNS were missing), the installer will use
DHCP instead.</li>

<li>If you're using a blank disk (or any disk without the HP firmware), the
installer will use DHCP.</li>

<li>If DHCP is used but your DHCP server does not respond, the HP mv2120
will use the fallback address `192.168.1.100`.  If you are unsure what the
address of your HP mv2120 is, unplug the Ethernet cable, start the machine
again, wait until Debian installer is ready for SSH and then plug the cable
back in and connect to this fallback address.</li>

</ul>

Please make sure that the HP mv2120 is on a local network to which only you
have access since the installer uses a very generic password, namely
`install`. The user is `installer`.  Connect to the installer (again,
replacing the address in the example with the actual IP address of your
mv2120):

<div class="code">
<pre>
ssh installer@<span class="input">192.168.1.100</span>
</pre>
</div>

The installation itself should be pretty standard and you can follow the <a
href = "http://www.debian.org/releases/stretch/armel/">installation
guide</a>.  The installer knows about the HP mv2120 and will by default
choose an appropriate partition layout.  If you partition the disk
manually, you have to make sure that `sda1` is a `/boot` partition with
type ext2 or ext3 (ext2 is recommended for the boot partition).  You also
have to set the bootable flag for this `/boot` partition, otherwise your
mv2120 will fail to boot.

During disk partitioning, Debian installer will find an existing LVM
logical volume on the disk and ask you whether it's okay to remove it.
This is the existing logical volume from the HP installation but it cannot
be used for your new Debian installation because the disk layout used by
the HP firmware will not work for Debian.  Please answer the question
whether the logical volume data should be removed with yes (or cancel the
installation and make a backup of your disk if you have not done so yet).

<img src = "../images/di-remove-logical-volume-data.png"
 alt = "Debian installer: remove existing locical volume data"
 width="644" height="316" />

At the end of the installation, the installer will create a boot image on
disk.  Afterwards you will get a confirmation that the installation is
complete.  Confirm, wait for the installer to finish and once your SSH
session terminates, wait a few minutes before you can connect to your newly
installed system via SSH.  The LEDs of your HP mv2120 will be used to
indicate when you can connect via SSH.  You will be able to log in as
your newly created user.

The health LED is used to signal the status of the boot process.  Here
is a list of stages and the corresponding signals the boot process will
go through:

<ul>

<li>Quickly blinking blue: the mv2120 is starting up and is loading the
boot image from disk.  This stage takes about 2 minutes.</li>

<li>The SATA light goes on, the health light continues to blink quickly:
the Linux kernel has been loaded.</li>

<li>Slowly blinking blue: the ramdisk has been loaded and is now trying
to mount your disk.</li>

<li>Solid purple: your root partition has been mounted and the boot process
will continue from disk.  If this stage takes a long time, the system might
be checking your disks.</li>

<li>Solid blue: the boot process has been completed and you can log in via
SSH.</li>

</ul>

<h2>Success</h2>

You should now have a complete Debian system running on your HP mv2120.
You can use `apt` and other tools to install additional software.  The
mv2120 is an ARM based device and the `armel` architecture is fully
supported by Debian.

In case you run into any bugs or problems, you may want to check the list
of <a href = "../known-issues/">known issues and bugs</a> with Debian on the
HP mv2120.

Go back to my <a href = "..">Debian on HP mv2120</a> page.

