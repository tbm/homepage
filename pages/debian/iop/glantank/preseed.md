---
title: Preseeding configuration values on GLAN Tank
nav: Preseeding
description: Preseeding instructions for Debian on GLAN Tank
keywords: [IOP, GLAN Tank, Supertank, SOTO-HDLGW, IO-Data, ARM, Debian, installation]
---

<h1>Preseeding network values</h1>

If you need to change the default network settings, you have to change the
preseeding file included in the image.  As user `root`, create a temporary
directory, go into it and unpack the initrd:

<div class="code">
<pre>
mkdir x
cd x
zcat ../initrd | cpio -if -
</pre>
</div>

Then edit the file `preseed.cfg`.  After you're done, you have to make a
new initrd and copy it to the hard drive:

<div class="code">
<pre>
find | cpio --quiet -o -H newc &gt; ../i
cd ..
gzip -9 i
sudo cp i.gz /mnt/initrd
</pre>
</div>

Go back to my <a href = "../install/">Debian installation guide for GLAN Tank</a> page.

