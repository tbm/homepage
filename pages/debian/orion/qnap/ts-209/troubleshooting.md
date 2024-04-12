---
title: Troubleshooting Debian on QNAP TS-209
nav: Troubleshooting
description: Troubleshooting Debian on QNAP TS-209
keywords: [Debian, QNAP, NAS, TS-209, troubleshooting, problems]
---

<div class="right">
<img src = "../images/r_ts209_front.jpg" class="border" alt="QNAP TS-209 from the front" width="148" height="97" />
</div>

This page describes common problems that users of Debian on the QNAP TS-209
have run into.  If you have any problems with your QNAP TS-209, either
while trying to install Debian or when running Debian, please look through
this page carefully to see whether you can find a solution.  If your
problem is not covered here, feel free to contact the <a href =
"http://lists.debian.org/debian-arm/">debian-arm list</a> for help.

<h2 id="installer">Debian installer</h2>

<h3 id="ssh-ip">I hear a beep after flashing Debian installer but cannot connect with SSH</h3>

After writing the Debian installer to flash and rebooting, you have to wait
a few minutes for it to start and then connect by SSH to perform the
installation.  When the installer is ready to accept SSH connections, it
will make one short beep and set the status LED to green.

Some people report that they are not able to connect to their QNAP via SSH
at this point.  The most common problem is that the wrong IP address is
used to connect to the QNAP.  Debian installer will read the network
configuration from the original QNAP firmware and use that but in some
cases different network settings have to be used (for example, because the
settings in the original firmware were incomplete).

If you cannot connect to your QNAP, here are some things you can try:

* Read the explanation of how the Debian installer <a href =
"../install/#net-config">creates the network settings</a>.
* Check the logs of your DHCP server to see whether your QNAP has
requested an IP address.  Alternatively, you can also install the `nast`
package on your PC and run `nast -m` to find all machines on your network.
The MAC address of your QNAP probably starts with `00:08:9B`.  The
hostname is probably <code>NAS</code> followed by the last 3 elements of
the MAC address (NAS<span class="input">CCDCA1</span> for 00:08:9B:<span
class="input">CC:DC:A1</span>).</li>
* Remove all hard drives from the QNAP.  In this case, Debian installer
won't find your existing network configuration on disk and will use
DHCP.
* If everything else fails, disconnect the Ethernet cable from your QNAP
and start your device again.  In this case, it is possible that the IP
address `192.168.1.100` is used.

<h3 id="ssh-password">Connections to the QNAP via SSH are possible but my password is not accepted</h3>

Some users report that they can connect to their QNAP via SSH just fine but
that the password is not accepted.  The account details depend on where you
are in the installation process.  If you have just flashed the installer
and want to install Debian, you have to connect with the user `installer`
and the password `install`.  However, after you have completed the
installation, you have to login with your newly created user.  You have to
use the password you chose during the installation.  You cannot login as
`installer` as this point anymore since this login is only valid for the
installer.  Note that you also cannot login as `root` user since that
option is disabled in SSH by default.

<h3 id="di-network">Debian installer fails to download components</h3>

The Debian installer that's written to flash is not the complete installer
so further components have to be downloaded from the network.  Some people
say that the installer starts fine and they can login via SSH but then the
installer fails to download components from the network.  The installer
might say that it cannot download the `Release` file.

The reason for this problem is usually wrong network settings.  It's
possible that either a wrong DNS server or a wrong gateway are specified.
To find out what the problem is, go to the menu in the Debian installer
(you might have to select `go back` to get to the menu) and execute a shell
(last but one point in the menu).  Now try to download something:

<div class="code">
<pre>
wget http://130.89.148.14/
wget http://www.debian.org/
</pre>
</div>

If the first command succeeds but the second one fails, the DNS server is
wrong (check the file `/etc/resolv.conf`).  If both commands fail to
download something, the gateway is probably wrong.  You can check your
network settings this way:

<div class="code">
<pre>
ip address
ip route
</pre>
</div>

The best way to fix the network settings are to update the configuration of
your DHCP server and to start the installer on your QNAP again.

<h3 id="partman-stuck">Formatting the disk is stuck at 33%</h3>

Formatting the disk may take a long time, especially if you have a large
disk.  Unfortunately, the progress bar is not updated while the disk is
being formatted so you may think that it is stuck (at 33%).  If this
happens, just be patient.  The installer is in fact formatting your disk.

<h3 id="bootable">Make the system bootable step fails</h3>

There can be a number of reasons why the "Make the system bootable" step
fails.  If this happens, open a shell in the installer and look at
`/var/log/syslog`.  Look towards the end for messages involving
"flash-kernel".

The QNAP TS-209 only has 4 MB for the ramdisk so the most likely cause is
that the ramdisk doesn't fit in flash.  You can find a message like this in
`/var/log/syslog`:

    Not enough space for initrd in MTD 'RootFS1' (need 4647643 but is actually 4194304).

If this is the case, you can apply the following workaround:

    echo "COMPRESS=xz" > /target/etc/initramfs-tools/conf.d/compress

This configures initramfs-tools to use XZ compression, which offers
better compression, and might mean that the ramdisk will now fit in
flash.  Unfortunately, it might still not fit if you use RAID or LVM.
In this case, install without RAID or LVM.

Exit the shell and repeat the "make the system bootable" step.

<h2 id="debian">Debian</h2>

<h3 id="no-boot">My QNAP no longer boots</h3>

There can be many reasons why a QNAP running Debian no longer boots,
ranging from a broken disk, to a bad upgrade or configuration.
Unfortunately, it's often impossible to say what the problem is without the
use of a serial console.  The best solution is to connect a serial console
to see what the problem is but not everyone can do that.

Before you do anything, you should listen.  Maybe your QNAP is performing
its regular filesystem check and this will delay the boot process.  This
delay can be considerable if you have a large disk.  If you can hear that
your hard drive is being accessed, just wait for a few hours.

If your hard drive is quiet and Debian doesn't start, you should try is to
connect your USB drive to another PC and to check the log files:

<div class="code">
<pre>
sudo mount /dev/sda2 /mnt
</pre>
</div>

Now you can look at the files in `/mnt/var/log`, in particular at the file
`syslog`.  If this file doesn't contain any information about the last boot
attempt (which is quite likely), you can enable `bootlogd` which will
record early boot messages:

<div class="code">
<pre>
sudo sed -i "s/BOOTLOGD_ENABLE=No/BOOTLOGD_ENABLE=yes/" /mnt/etc/default/bootlogd
sudo umount /mnt
</pre>
</div>

Connect the drive to your QNAP, boot it, wait a few minutes, then turn it
off and connect the drive to your PC again and mount it.  Now look at the
file `/mnt/var/log/boot` which might tell you more.

One common cause for boot problems is related to filesystem checks and
running `fsck` over all partitions may help.  There are several reasons why
this might help.  For example, the Linux ext3 filesystem has to be checked
periodically.  Even though Debian has been configured not to prompt the
user during the filesystem check, it might still do so in case of serious
errors.  Without a serial console, this prompt means that your QNAP will
hang waiting for user input.

Turn your QNAP off, connect the disk to another machine running Linux and
run `fsck` over all partitions containing data.  On a normal Debian
installation, this includes `sda1` (`/boot`), `sda2` (`/`) and `sda6`
(`/home`):

<div class="code">
<pre>
sudo fsck /dev/sda1
sudo fsck /dev/sda2
sudo fsck /dev/sda6
</pre>
</div>

If none of this helps, I'm afraid you probably have to connect <a href =
"../serial/">a serial console</a> or use the <a href =
"../recovery/">recovery mode</a> to flash the Debian installer and to
perform a new installation.

<h3 id="ramdisk">The ramdisk doesn't fit in flash</h3>

The flash partition on the QNAP TS-209 is rather small and there is only
limited space for the ramdisk (initrd).  This may lead to errors after
kernel upgrades because the new ramdisk no longer fits in flash,
especially if you use RAID or LVM.  The error messages say "The initial
ramdisk is too large" and "Not enough space for initrd in MTD 'RootFS1'".
To avoid this problem, you can configure your system to use `xz`
compression of the ramdisk, which will result in a much smaller ramdisk
compared to the default compression with `gzip`.

Please follow these steps to enable `xz` compression of the ramdisk.
First, configure `initramfs-tools`:

<div class="code">
<pre>
echo "COMPRESS=xz" | sudo tee /etc/initramfs-tools/conf.d/compress
</pre>
</div>

Second, ensure that the `xz-utils` package is installed:

<div class="code">
<pre>
sudo apt install xz-utils
</pre>
</div>

Finally, update the ramdisk:

<div class="code">
<pre>
sudo update-initramfs -u
</pre>
</div>

If you use a custom kernel rather than a kernel provided by Debian, please
ensure that the `CONFIG_RD_XZ` setting is enabled.

Unfortunately, several components have grown substantially in Debian 10
(buster), which means that the ramdisk might still not fit into flash,
in particular if you use LVM.

