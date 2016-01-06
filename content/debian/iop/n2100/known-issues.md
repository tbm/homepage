---
title: Known issues of Debian on Thecus N2100
nav: Known issues
keywords: [Debian, Thecus, N2100, bugs, issues, defects]
---

<% content_for :right do %>
<img src = "../images/r_n2100_debian.jpg" class="border" alt="Thecus N2100" width="133" height="148" />

<%= render "adsense-wideskyscaper-right" %>
<% end %>

<h1>Known issues and bugs</h1>

Here is a list of known issues and bugs with Debian on the Thecus N2100.

<h2>Debian 7 (wheezy) with 3.2 kernel</h2>

<ul>

<li>Disk access is slow because of lack of support for the DMA engine on
the IOP32x chip.</li>

</ul>

<h2>Debian 8 (jessie)</h2>

* The IOP32x platform is no longer supported.  This means that support
for the Thecus N2100 was dropped.

<div class="bbf">
<%= render "adsense-banner-before-footer" %>
</div>

