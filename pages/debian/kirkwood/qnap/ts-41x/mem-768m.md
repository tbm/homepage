---
title: Setting mem=768M on QNAP TS-41x/TS-42x
nav: mem=768M
description: Setting mem=768M on the QNAP TS-41x/TS-42x
keywords: [Debian, QNAP]
---

Debian doesn't work on QNAP devices with 1 GB of RAM (i.e. TS-420U,
TS-421 and TS-421U).  Even though we reported this to the Linux kernel
developers, they found it difficult to investigate this issue and it
never got fixed.  The best workaround is to add `mem=768M` to the kernel
command line to limit the RAM.

# QNAP firmware

If you have the QNAP firmware, you can make the change with the
following commands.  These commands will:

* Write the current u-boot configuration to `/tmp/debian.uboot` and add
`mem=768M` to `bootargs`.
* Output `bootargs` from the file so you can verify it looks good.
* Write the new u-boot configuration to flash.

<div class="code">
<pre>
ubootcfg -b 0 -f /dev/mtdblock4 -o - | sed "s/^\(bootargs=.*\)/\1 mem=768M/" &gt; /tmp/debian.uboot
grep "^bootargs" /tmp/debian.uboot # Check it looks sane
ubootcfg -b 0 -f /dev/mtdblock4 -i /tmp/debian.uboot
</pre>
</div>

# Debian

If you're running Debian (1 GB was working fine with Debian jessie), you
can change the kernel arguments as follows.

<div class="code">
<pre>
sudo cp /usr/share/doc/u-boot-tools/examples/qnap_ts119-219.config /etc/fw_env.config
sudo fw_printenv bootargs
</pre>
</div>

**Note:** I'm not sure if this configuration will work on the
TS-41x/TS-42x.  I believe it should.  If the command gives the right
output, it's working.  If so, please email me at tbm@cyrius.com to
confirm.

The output should be something like this:

<div class="code">
<pre>
bootargs=console=ttyS0,115200 root=/dev/ram initrd=0xa00000,0x900000 ramdisk=34816
</pre>
</div>

You have to append `mem=768M` to these boot arguments in order to restrict
the memory to 768 MB.

<div class="code">
<pre>
sudo fw_setenv bootargs "console=ttyS0,115200 root=/dev/ram initrd=0xa00000,0x900000 ramdisk=34816 mem=768M"
</pre>
</div>

Finally, you can run `sudo fw_printenv bootargs` again to verify that
`mem=768M` has been adding to the boot arguments.

Now you can either perform an upgrade or [put the installer in
flash](../deinstall/#reinstall) and perform a new installation.
