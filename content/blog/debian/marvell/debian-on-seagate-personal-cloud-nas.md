---
title: "Debian on Seagate Personal Cloud and Seagate NAS"
created_at: 2016-07-21 19:50:27 -0700
kind: article
---

The majority of NAS devices supported in Debian are based on Debian's
Kirkwood platform.  This platform is quite dated now and can only run
Debian's `armel` port.

Debian now supports the Seagate Personal Cloud and Seagate NAS devices.
They are based on Marvell's Armada 370, a platform which can run
Debian's `armhf` port.  Unfortunately, even the Armada 370 is a bit
dated now, so I would not recommend these devices for new purchases.
If you have one already, however, you now have the option to run native
Debian.

There are some features I like about the Seagate NAS devices:

* Network console: you can connect to the boot loader via the network.
This is useful to load Debian or to run recovery commands if needed.
* Mainline support: the devices are supported in the mainline kernel.
* Good contacts: Seagate engineer Simon Guinot is interested in Debian
support and is a joy to work with.  There's also a community for [LaCie
NAS devices](http://lacie-nas.org/) (Seagate acquired LaCie).

If you have a Seagate Personal Cloud and Seagate NAS, you can follow the
[instructions on the Debian
wiki](https://wiki.debian.org/InstallingDebianOn/Seagate/PersonalCloud).

If Seagate releases more NAS devices on Marvell's Armada platform, I
intend to add Debian support.

