---
title: Updating the u-boot config for Debian on HP mv2120
nav: u-boot configuration
keywords: [Debian, HP, mv2120, u-boot, stretch, upgrade]
---

<div class="right">
<img src = "../images/r_mv2120_front.jpg" class="border" alt="HP mv2120 from the front" width="148" height="212" />
</div>

# U-boot configuration for Debian upgrade

Before you can upgrade Debian from Debian 8 (jessie) to Debian 9
(stretch), you have to change a setting in the u-boot configuration.
Unfortunately, the default settings no longer work with Debian 9.
The new settings are compatible with Debian 8 (jessie) and Debian 9
(stretch), so I suggest you make the changes now.

If you have serial console access to the mv2120, you can run some
commands in u-boot.  Simply interrupt the boot process by pressing a key
and type the following:

    setenv loadAddr 0x0600000
    setenv bootcmd 'bootext2 0,1:1,2 0x0600000 /boot/uImage /dev/sda /dev/sdb'
    saveenv

If you don't have a serial console, you can make the changes from within
Debian.  Run the following commands:

    cat >/etc/fw_env.config <<EOF
    /dev/mtd0           0x00000         0x1000     0x20000
    EOF

    fw_setenv loadAddr 0x0600000
    fw_setenv bootcmd "bootext2 0,1:1,2 0x0600000 /boot/uImage /dev/sda /dev/sdb"

This creates a config file so the u-boot environment can be modified and
uses `fw_setenv` to update two boot variables.

Once you made the changes, upgrades to Debian 9 should work fine and you
can also use the [Debian installer](../install) if you want to perform a
new installation.

Please note that Debian 9 is the last release to support the HP mv2120.

