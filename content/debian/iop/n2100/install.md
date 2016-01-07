---
title: Installing Debian on the Thecus N2100
nav: Installing Debian
description: Installation instructions for Debian on the Thecus N2100
keywords: [Debian, Thecus, N2100, installation, guide, IOP, NAS, server, hack]
---

<% content_for :right do %>
<img src = "../images/r_n2100_debian.jpg" class="border" alt="Thecus N2100" width="133" height="148" />
<% end %>

<h1>Installing Debian on the Thecus N2100</h1>

While the Thecus N2100 is supported in Debian 7 (wheezy), it is no longer
supported in Debian 8 (jessie).

<h2>Requirements</h2>

In order to install Debian on an N2100, you need the following:

<ul>

<li>A Thecus N2100 machine or compatible device, such as the Allnet
ALL6500.</li>

<li>Another machine on which you have an SSH client.  Every Linux
distribution includes an OpenSSH client and there is <a href =
"http://www.chiark.greenend.org.uk/~sgtatham/putty/download.html">PuTTY</a>
for Windows.</li>

</ul>

<h2>Preparation</h2>

There are a number of issues you should be aware of before beginning with
the installation:

<ul>

<li>You have to be aware that by installing Debian you probably lose the
warranty on your N2100.</li>

<li>The installation of Debian will replace the Thecus firmware that is
shipped with your N2100.  It is not possible to keep both installed at the
same time.</li>

<li>When you install Debian, it will by default format your whole disk.  I
therefore recommend to make backup of any data you might have on your
machine.</li>

<li>Make sure that the J3/J4 jumper on your board is set to the J3
position.  This is the default position so you should not have to change
anything.</li>

</ul>

<h2>Upgrading the Firmware</h2>

Before installing Debian, make sure that you are running the <a href =
"http://www.thecus.com/dl.php">latest version</a> of the Thecus firmware.
In version 2.1.05 Thecus added the ability to the boot loader used on this
machine, RedBoot, to allow users to <a href = "../telnet/">connect to the
machine via telnet</a> while the machine is booting.  This gives you a
rescue mode in case something goes wrong with the installation.  I
therefore strongly advise you to upgrade to version 2.1.05 or higher before
installing Debian.  If you don't have a Thecus N2100, but an Allnet or
another box, you first need to make a simple change so that you can upgrade
to the Thecus firmware.  This change is documented on the Thecus wiki in
the page about <a href =
"http://naswebsite.com/wiki/N2100_ALLNET_to_Thecus">turning your
Allnet into a Thecus</a>.

<h2>Starting the Installer</h2>

In order to start the installation of Debian, you have to login to the
firmware of your Thecus N2100 to configure the network and to upgrade the
firmware to an installer image of Debian.  The N2100 is configured to have
the IP address `192.168.1.100`.  You can open this address in your web
browser and then login in as `admin`.  The default password is `admin`.

<p><img src = "../images/firmware-login.jpg" class="border" alt = "Thecus Firmware: Login" width="640" height="429" /></p>

<p><img src = "../images/firmware-login2.jpg" class="border" alt = "Thecus Firmware: Login" width="640" height="429" /></p>

The way the installation of Debian works is that you flash an upgrade
firmware that will start the installer.  The installer will then allow you
to connect via SSH to perform the installation.  This works because the
installer will read your network settings from your device and then bring
up SSH so you can connect.  That's why it's important to configure the
network settings in the Thecus firmware.  If you have used a static
configuration, these values will be used.  Otherwise, the installer will
ask a DHCP server in your network for an IP configuration.  If the
installer cannot find a DHCP server on your network, it will fall back to
the static configuration that is the default on the N2100, namely the IP
address `192.168.1.100` and a gateway and name server at `192.168.1.1`.  In
any case, make sure that your network is configured fully, including values
for DNS.  If your static IP configuration is not complete (i.e. is either
missing the IP address or DNS), the Debian installer will request an
address via DHCP.

<p><img src = "../images/firmware-network.jpg" class="border" alt = "Thecus Firmware: Network Config" width="640" height="429" /></p>

Once you have configured the network, you can go to `System`, followed by
`Firmware Upgrade`.  First, you have to download the <a href =
"http://ftp.uk.debian.org/debian/dists/wheezy/main/installer-armel/current/images/iop32x/network-console/n2100.bin">firmware
image</a> provided by Debian for the installation.  Afterwards you can
upload this image to the Thecus firmware.  It will ask you to confirm that
you want to upgrade to this new version.

<p><img src = "../images/firmware-upgrade1.jpg" class="border" alt = "Thecus Firmware: Upgrade" width="640" height="429" /></p>

<p><img src = "../images/firmware-upgrade2.jpg" class="border" alt = "Thecus Firmware: Upgrade" width="640" height="429" /></p>

<p><img src = "../images/firmware-upgrade3.jpg" class="border" alt = "Thecus Firmware: Upgrade" width="640" height="172" /></p>

<p><img src = "../images/firmware-upgrade4.jpg" class="border" alt = "Thecus Firmware: Upgrade" width="640" height="172" /></p>

Note that the progress bar is not updated during the upgrade process and
will remain at 1% until the end.

<p><img src = "../images/firmware-upgrade5.jpg" class="border" alt = "Thecus Firmware: Upgrade" width="640" height="172" /></p>

After a few minutes the upgrade process has completed and you have to
reboot the machine:

<p><img src = "../images/firmware-reboot.jpg" class="border" alt = "Thecus Firmware: Reboot" width="640" height="306" /></p>

The system will now restart and after about 5 minutes you can connect to
the installer via SSH.  Please ignore your web browser which tells you that
the system is soon restarting because no update will be shown there.  When
the web page has finished counting down and says `Reboot Complete`, the
installer will not be ready yet!  You need to wait about another minute.
When the installer is ready to accept connections via SSH, your N2100 will
beep three times.  The username is `installer` and the password is
`install`.  Note that you need a terminal which understands UTF-8 because
that's the character set the installer will use.

<div class="code">
<pre>
ssh installer@<span class="input">192.168.1.100</span>
</pre>
</div>

<h2>Installing Debian</h2>

The installation itself should be pretty standard and you can follow the <a
href = "http://www.debian.org/releases/wheezy/armel/">installation guide</a>.
It knows about the N2100 and at the end of the installation it will flash a
kernel and ramdisk that will automatically boot into Debian.

The whole installation will take about one hour.  After the installation is
complete, you will be able to log in as `root` or your newly created user
via SSH.

<h2>Usage</h2>

<h3><a id = "fan">Fan</a></h3>

By default, the fan should run at full speed.  If you need to regulate the
speed, you can write to the `pwm` files in `/sys`.  If you want to stop the
fan, you have to write the value zero to these files:

<div class="code">
<pre>
echo 0 &gt; /sys/bus/i2c/devices/0-002e/pwm2
echo 0 &gt; /sys/bus/i2c/devices/0-002e/pwm1
</pre>
</div>

You can activate full speed using the following commands:

<div class="code">
<pre>
echo 255 &gt; /sys/bus/i2c/devices/0-002e/pwm1
echo 255 &gt; /sys/bus/i2c/devices/0-002e/pwm2
</pre>
</div>

There's currently no script to regulate the fan automatically, so I suggest
you run the fan at full speed.

<h3><a id = "beeper">Beeper</a></h3>

You can install the `beep` package and then user the beeper in the
following way:

<div class="code">
<pre>
beep -e /dev/input/event0 -f 220 -l 500 -d 500 -r 3
</pre>
</div>

<%= render "paypal", :desc => "Debian/N2100 donation" %>

