---
title: Telnet to RedBoot on the Thecus N2100
nav: Using telnet to access RedBoot
description: Instructions for using telnet to connect to RedBoot
keywords: [Debian, Thecus, N2100, installation, RedBoot, telnet]
---

<% content_for :right do %>
<img src = "../images/r_n2100.jpg" class="border" alt="Thecus N2100" width="141" height="148" />
<% end %>

<h1>Using telnet to access RedBoot</h1>

RedBoot, the boot loader used in the N2100, has a feature which allows you
to connect to it via telnet.  This makes it possible to run some RedBoot
commands without access to the serial console.  In old firmware versions of
the N2100, no IP address is set in RedBoot so it's not possible to connect
to it by telnet.  However, telnet is enabled when you upgrade to firmware
version 2.1.05 or higher.

In order to connect to RedBoot with telnet, you need the `telnet` package.
Additionally, I suggest you install the `iputils-arping` package.  This
allows you to easily find out when you can connect to RedBoot.  Simply run
the following command, turn on your N2100 and wait for telnet to connect:

<div class="code">
<pre>
<span class="input">arping -f 192.168.1.100 &amp;&amp; telnet 192.168.1.100 9000</span>
WARNING: interface is ignored: Operation not permitted
ARPING 192.168.1.100 from 192.168.1.104 eth0
Unicast reply from 192.168.1.100 [00:14:FD:10:33:8E]  6.473ms
Sent 9 probes (9 broadcast(s))
Received 1 response(s)
Trying 192.168.1.100...
Connected to 192.168.1.100.
Escape character is '^]'.
== Executing boot script in 2.650 seconds - enter ^C to abort
^C
RedBoot&gt;
RedBoot&gt;
</pre>
</div>

Now that you've interrupted RedBoot's boot script, RedBoot will wait for
you to type commands.  You can now do a number of things, such as loading
an alternative kernel and initrd via TFTP.  This is useful as a rescue mode
in case the installation of Debian failed and you want to load the original
firmware again.  In order to do this, you need to extract the `ramdisk.arm`
and `zImage` files as described in the <a href =
"../deinstall/">de-installation page</a>.  You need to put this on a TFTP
server and then you can load it with:

<div class="code">
<pre>
ip -h 192.168.1.2
load -r ramdisk.arm -b 0x00800000
load -r zImage -b 0x00200000
exec -c "console=ttyS0,115200 root=/dev/ram0 initrd=0xa0800000,42M"
</pre>
</div>

This will start the original Thecus firmware but note that it has not yet
been written to flash.  You can do this with the firmware upgrade option,
simply by &quot;upgrading&quot; to the version you previously used.

