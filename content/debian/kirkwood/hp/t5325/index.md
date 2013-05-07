---
title: Debian on HP t5325
nav: t5325
description: Instructions for running Debian on the HP t5325 Thin Client
keywords: [Debian, NAS, HP, t5325, thin client]
---

<% content_for :right do %>
<%= render "adsense-wideskyscaper-right" %>
<% end %>

<h1>Debian on HP t5325</h1>

Debian has partial support for the HP t5325 thin client.  However, there
are two reasons why Debian is not suited for the HP t5325:

<ul>

<li>The t5325 only has 512 MB of storage and Debian is not adapted for such
small environments.</li>

<li>The t5325 has a flash device and Debian is not adapted for such
devices.  We'll use the ext2/ext3 filesystem and this is not good for flash
devices.

</li>

</ul>

Here are <a href = "install/">initial install pages</a>.

<div class="bbf">
<%= render "adsense-banner-before-footer" %>
</div>

