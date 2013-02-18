---
title: De-installing Debian on the Kurobox Pro
nav: De-installing Debian
description: Restoring the original Buffalo firmware on the Kurobox Pro
keywords: [Buffalo, Revogear, Kurobox Pro, original firmware, guide]
---

<% content_for :right do %>
<img src = "../images/r_kuroboxpro_front.jpg" class="border" alt="Kurobox Pro from the front" width="148" height="231" />

<%= render "adsense-wideskyscaper-right" %>
<% end %>

<h1>Restoring the original Buffalo firmware</h1>

Restoring the original Buffalo firmware is easy because Debian was
installed to SATA disk whereas the Buffalo firmware is stored in flash and
flash was not changed during the installation of Debian.  The only change
was to the configuration environment of u-boot in order to boot from disk
rather than flash memory.

In order to boot the original Buffalo firmware again, you simply have to
configure the u-boot environment so the device will boot from flash.  First
of all, install the Debian package `uboot-envtools` which allows you to
manipulate the u-boot environment.  You then have to copy the configuration
file `kurobox-pro.config` from `/usr/share/doc/uboot-envtools/examples` to
`/etc/fw_env.config`:

<div class="code">
<pre>
cp /usr/share/doc/uboot-envtools/examples/kurobox-pro.config /etc/fw_env.config
</pre>
</div>

Now you can change the variable `bootcmd` so the device will boot from
flash:

<div class="code">
<pre>
fw_setenv bootcmd 'nboot $(default_kernel_addr) 0 20000; setenv bootargs $(bootargs_base) $(bootargs_root) $(buffalo_ver); bootm $(default_kernel_addr)'
</pre>
</div>

When you next boot, the device will run the original Buffalo firmware from
MTD flash.

If you then want to go back and use the Debian system on hard disk, you can
issue the following command from the Buffalo firmware:

<div class="code">
<pre>
nvram -c set bootcmd 'ide reset; ext2load ide 0:1 $(default_kernel_addr) /$(kernel); ext2load ide 0:1 $(default_initrd_addr) /$(initrd); setenv bootargs $(bootargs_base); bootm $(default_kernel_addr) $(default_initrd_addr)'
</pre>
</div>

Go back to my <a href = "..">Debian on Kurobox Pro</a> page.

<div class="bbf">
<%= render "adsense-banner-before-footer" %>
</div>

