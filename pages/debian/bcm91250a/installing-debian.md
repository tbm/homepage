---
title: Installing Debian on BCM91250A
nav: Installation
description: Installation guide for Debian on Broadcom SWARM
keywords: [SWARM, Broadcom, sarge, installation]
---

<b>Important note:</b> support for the BCM91250A board has been removed
from the Debian installer.  Therefore, the information from this page no
longer applies.  The page is only provided for historical purposes.

In order to install Debian on an BCM91250A evaluation board (SWARM), you
need the following:

<ul>

<li>an BCM91250A evaluation board from Broadcom with a recent version of
CFE (see my <a href = "../cfe/">page on upgrading CFE</a>).</li>

<li>a null modem cable.  (We will support desktop like installations with a
<a href = "../hardware/">compatible graphics card</a> and an USB keyboard in
the future, but this currently doesn't work.)</li>

<li>another machine (called the server from now on) on which you can
install a TFTP and a DHCP server.</li>

</ul>

<h2>Preparing the server</h2>

First, you have to install a TFTP and DHCP server.  While I will
demonstrate in the following how to configure these services on a Debian
machine, there is no special requirement that these services run on Debian.
Any TFTP and DHCP server will do, and they don't even have to be on the
same machine.

In order to install TFTP and DHCP packages, issue the following commands as
user `root`:

<div class="code">
<pre>
apt-get install tftpd
apt-get install isc-dhcp-server
</pre>
</div>

Secondly, you have to configure the TFTP and the DHCP server.  The TFTP
package should automatically put a proper configuration line in
`/etc/inetd.conf` but you might have to adapt it to your system.  By
default, it will use `/boot` as the directory to serve TFTP files.  Edit
the `/etc/inetd.conf` file and make sure it contains a line like this:

<div class="code">
<pre>
tftp dgram udp wait nobody /usr/sbin/tcpd /usr/sbin/in.tftpd /boot
</pre>
</div>

You also have to configure your DHCP server.  Edit `/etc/dhcp/dhcpd.conf`
and add an entry similar to the following:

<div class="code">
<pre>
host <span class="input">swarm</span> {
    hardware ethernet <span class="input">00:02:4C:FE:0D:09</span>;
    fixed-address <span class="input">192.168.1.67</span>;
    option routers <span class="input">192.168.1.1</span>;
    option host-name "<span class="input">swarm</span>";
}
</pre>
</div>

You have to adapt various values: you can choose your own host name, and
you need the MAC address of your BCM91250A evaluation board.  You can
obtain this value by issuing the `show devices` command in CFE.

Now, download and install the actual files needed for the installation.
Download the whole contents of the following directory to your TFTP
directory (`/boot` in the example above): <a href =
"http://ftp.uk.debian.org/debian/dists/stable/main/installer-mips/current/images/sb1-bcm91250a/netboot/">big-endian</a>
or <a href =
"http://ftp.uk.debian.org/debian/dists/stable/main/installer-mipsel/current/images/sb1-bcm91250a/netboot/">little-endian</a>.
Edit `sibyl.conf` and substitute 192.168.1.1 with the IP address or name of
your TFTP server.

Finally, restart the TFTP and DHCP server to activate all changes you have
made:

<div class="code">
<pre>
/etc/init.d/inetd restart
/etc/init.d/isc-dhcp-server restart
</pre>
</div>

<h2>Installing Debian</h2>

Now it's time to start the installation of Debian.  Connect the null modem
cable to the lower serial port of your BCM91250A and start a terminal
emulation program (minicom, cu or screen) with the settings 115200 8N1 (for
example, `screen /dev/ttyS0 115200`).  Start your BCM91250A and load the
installer with the <span class="input">marked commands</span> in the
transcript below (you have to type the IP address or name of your TFTP
server instead of 192.168.1.1):

<div class="code">
<pre>
CFE&gt; <span class="input">ifconfig eth0 -auto</span>
eth0: Link speed: 100BaseT FDX
Device eth0:  hwaddr 00-02-4C-FE-0D-09, ipaddr 192.168.1.3, mask 255.255.255.0
        gateway 192.168.1.1, nameserver 131.111.8.42, domain cyrius.com
*** command status = 0
CFE&gt; <span class="input">boot 192.168.1.1:/boot/sibyl</span>
Loader:raw Filesys:tftp Dev:eth0 File:192.168.1.1:/boot/sibyl Options:(null)
Loading: ....... 126648 bytes read
Entry at 0x0000000020000000
Closing network.
Starting program at 0x0000000020000000
SiByte Loader, version 2.4.2
Built on Jul 28 2004
Network device 'eth0' configured
Getting configuration file tftp:192.168.1.1:/boot/sibyl.conf...
Config file retrieved.
Loading kernel (ELF32):
    2387968@0x80100000
done
Loading ramdisk at 0x803b0000...2252049 bytes loaded
...
</pre>
</div>

The installation itself should be pretty standard and you can follow the <a
href = "http://www.debian.org/releases/stable/mipsel/install">installation
manual</a>.  The only thing you have to keep in mind is that you need a
specific partition setup for your BCM91250A.  SiByl has several limitations
we have to work with.  First, SiByl is bigger than the space dedicated for
the boot sector on a disk and by writing SiByl to your disk you effectively
overwrite your first partition if you don't take care!  You can work around
this by starting the first partition not directly at the beginning of the
hard drive or by having a dummy partition at the beginning which SiByl can
overwrite without causing any harm.  To make the latter easily possible in
Debian's installer, we have introduced a `sibyl` partition type called
`SiByl boot partition` (which will really create a partition of type FAT16
so SiByl won't try to look at it when loading its configuration file).  You
<i>have to</i> create a partition of type `sibyl` as your first primary
partition with a size of about 1 MB.

<p><img src = "../images/partman-sibyl-use-as.jpg" class="border" alt = "Make a sibyl partition" width="724" height="364" /></p>

<p><img src = "../images/partman-sibyl-boot-partition.jpg" class="border" alt = "The SiByl boot partition type" width="724" height="364" /></p>

The second restriction of SiByl is that it can only find its configuration
file and kernels if they are directly located in the root of a filesystem
(i.e. not in a sub-directory).  Therefore, you have to make `/boot` a
separate partition before creating a partition for your root filesystem.
If you keep both of these requirements in mind when creating your partition
layout, you will be fine and the installation will proceed smoothly.

The best solution is not to worry about making the partitions yourself but
use debian-installer's guided partitioning option.  It knows about the
BCM91250A evaluation board and will create a proper boot partition for you.

<p><img src = "../images/partman-guided.jpg" class="border" alt = "Guided Partioning" width="724" height="364" /></p>

<p><img src = "../images/partman-schemes.jpg" class="border" alt = "Guided Partioning: choosing a schema" width="724" height="364" /></p>

<p><img src = "../images/partman-overview.jpg" class="border" alt = "Partioning: overview" width="724" height="364" /></p>

When the installation is done, it will reboot.  You'll be dropped into CFE
again and now you can start Debian from disk:

<div class="code">
<pre>
CFE&gt; <span class="input">boot ide0.0:</span>
Loader:raw Filesys:raw Dev:ide0.0 File: Options:(null)
Loading: ........... 126976 bytes read
Entry at 0x0000000020000000
Closing network.
Starting program at 0x0000000020000000
SiByte Loader, version 2.4.2
Built on Jul 28 2004
Getting configuration file ext2:ide0.0:*:sibyl.conf...
Config file retrieved.
Available configurations:
  debian
Boot which configuration [debian]:
Loading kernel (ELF32):
    2387968@0x80100000
...
</pre>
</div>

You will then be able to finish the installation, create user accounts and
install more packages.  After that, you are done.  From now on, you can
boot into your Debian system easily by the command above which will load
SiByl from disk and then load the kernel and start Debian.

With some versions of CFE, you can also specify an environment variable
which allows your machine to boot from disk automatically.  Simply type the
following on the CFE command prompt once and your machine will automatically
boot Debian if you have the right version of CFE:

<div class="code">
<pre>
CFE&gt; <span class="input">setenv -p STARTUP "boot ide0.0:"</span>
</pre>
</div>

