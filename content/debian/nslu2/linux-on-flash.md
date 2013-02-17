---
title: Tips for running Linux on a flash device
description: Tips for running Linux on a flash device
keywords: [Debian, NSLU2, flash, Linux]
---

<% content_for :right do %>
<img src = "../images/r_nslu2_front.jpg" class="border" alt="A NSLU2 from the front" width="148" height="218" />

<%= render 'adsense-wideskyscaper-right' %>
<% end %>

<h1>Tips for running Linux on a flash device</h1>

<h2>by David Härdeman &lt;david@hardeman.nu&gt;</h2>

If you are running your NSLU2 on a USB flash key, there are a number of
things you might want to do in order to reduce the wear and tear on the
underlying flash device (as it only supports a limited number of writes).

<em>Note:</em> this document currently describes Debian etch (4.0) and
needs to be updated to Debian squeeze (6.0).  Some of the hints may still
apply, but some may not.

* The ext3 filesystem per default writes metadata changes every five
seconds to disk.  This can be increased by mounting the root filesystem
with the `commit=N` parameter which tells the kernel to delay writes to
every `N` seconds.
* The kernel writes a new atime for each file that has been read which
generates one write for each read. This can be disabled by mounting the
filesystem with the `noatime` option.
* Both of the above can be done by adding e.g.  `noatime,commit=120,...` to
`/etc/fstab`.  This can also be done on an already mounted filesystem by
running the command:
<div class="code">
<pre>
mount -o remount,noatime,commit=120 /
</pre>
</div>
* The system will run `updatedb` every day which creates a database of all
files on the system for use with the `locate` command. This will also put
some stress on the filesystem, so you might want to disable it by adding
<div class="code">
<pre>
exit 0
</pre>
</div>
early in the `/etc/cron.daily/find` script.
* syslogd will in the default installation sync a lot of log files to disk
directly after logging some new information. You might want to change
`/etc/syslog.conf` so that every filename starts with a `-` (minus) which
means that writes are not synced immediately (which increases the risk that
some log messages are lost if your system crashes).  For example, a line
such as:
<div class="code">
<pre>
kern.*                          /var/log/kern.log
</pre>
</div>
would be changed to:
<div class="code">
<pre>
kern.*                          <span class="input">-</span>/var/log/kern.log
</pre>
</div>
You also might want to disable some classes of messages altogether by
logging them to `/dev/null` instead, see `syslog.conf(5)` for
details.
* In addition, syslogd likes to write `-- MARK --` lines to log files every
20 minutes to show that syslog is still running. This can be disabled by
changing `SYSLOGD` in `/etc/default/syslogd` so that it reads
<div class="code">
<pre>
SYSLOGD="-m 0"
</pre>
</div>
After you've made any changes, you need to restart syslogd by running
<div class="code">
<pre>
/etc/init.d/syslogd restart
</pre>
</div>
* If you have a swap partition or swap file on the flash device, you might
want to move it to a different part of the disk every now and then to make
sure that different parts of the disk gets hit by the frequent writes that
it can generate.  For a swap file this can be done by creating a new swap
file before you remove the old one.
* If you have a swap partition or swap file stored on the flash device, you
can make sure that it is used as little as possible by setting
`/proc/sys/vm/swappiness` to zero.
* The kernel also has a setting known as `laptop_mode`, which makes it
delay writes to disk (initially intended to allow laptop disks to spin down
while not in use, hence the name). A number of files under `/proc/sys/vm/`
controls how this works:
    * `/proc/sys/vm/laptop_mode`: How many seconds after a read should a
writeout of changed files start (this is based on the assumption that a
read will cause an otherwise spun down disk to spin up again).
    * `/proc/sys/vm/dirty_writeback_centisecs`: How often the kernel should
check if there is "dirty" (changed) data to write out to disk (in
centiseconds).
    * `/proc/sys/vm/dirty_expire_centisecs`: How old "dirty" data should be
before the kernel considers it old enough to be written to disk. It is in
general a good idea to set this to the same value as
`dirty_writeback_centisecs` above.
    * `/proc/sys/vm/dirty_ratio`: The maximum amount of memory (in percent)
to be used to store dirty data before the process that generates the data
will be forced to write it out. Setting this to a high value should not be
a problem as writeouts will also occur if the system is low on memory.
    * `/proc/sys/vm/dirty_background_ratio`: The lower amount of memory (in
percent) where a writeout of dirty data to disk is allowed to stop.  This
should be quite a bit lower than the above `dirty_ratio` to allow the
kernel to write out chunks of dirty data in one go.

All of the above kernel parameters can be tuned by using a custom init
script, such as <a href = "../files/kernel-params">this example script</a>.
Store it to e.g. `/etc/init.d/kernel-params`, make it executable with

<div class="code">
<pre>
chmod a+x /etc/init.d/kernel-params
</pre>
</div>

and make sure it is executed by running

<div class="code">
<pre>
update-rc.d kernel-params defaults
</pre>
</div>

<em>Note:</em> Most of these settings reduce the number of writes to disk
by increasing memory usage. This increases the risk for out of memory
situations (which can trigger the dreaded OOM killer in the kernel). This
can even happen when there is free memory available (for example when the
kernel needs to allocate more than one contiguous page and there are only
fragmented free pages available).

As with any tweaks, you are advised to keep a close eye on the amount of
free memory and adapt the tweaks (e.g. by using less aggressive caching and
increasing the swappiness) depending on your workload.

This article has been contributed by David Härdeman &lt;david@hardeman.nu&gt;

Go back to the <a href = "..">Debian on NSLU2</a> page.

<div class="bbf">
<%= render 'adsense-banner-before-footer' %>
</div>

