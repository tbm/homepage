---
title: Debian on Cobalt with little memory
nav: Installation With Low Memory
description: Installation guide of Debian for Cobalt machines with little memory
keywords: [Debian, installation, Cobalt]
---

<% content_for :right do %>
<%= render "adsense-wideskyscaper-right" %>
<% end %>

<h1>Installing Debian on Cobalt machines with little memory</h1>

Debian's installer requires 64 MB of memory in normal operation on MIPS
based Cobalt machines.  If your machine has less memory, you can still
install Debian but the method may be different.  Debian's installer
supports a `lowmem` mode in which less functionality is available (and
therefore the installer requires less memory).  If you do not have enough
memory for the lowmem mode, you can manually install a tar ball.

The following four different methods are available, depending on the amount
of memory your Cobalt machine has:

<ol>

<li>64 MB or more: you can follow the normal installation procedure <a href
= "../install/">described in my guide</a>.</li>

<li>33-63 MB: with this amount of RAM, Debian's installer will
automatically enter lowmem level 1.  Apart from a warning, you will see
little differences to the <a href = "../install/">normal installation
procedure</a>.</li>

<li>22-32 MB: Debian's installer will run in lowmem level 2.  You can
mostly follow the <a href = "../install/">normal installation procedure</a>
but you will get a screen where you can install additional modules not
installed by default.</li>

<li>21 MB or less: you won't be able to use Debian's installer but you can
<a href = "../unpack/">manually install Debian from a tar ball</a>.</li>

</ol>

<h2><a id = "modules">debian-installer lowmem level 2: choosing modules for Cobalt</a></h2>

In Debian's installer lowmem level 2, some installer modules are not
automatically loaded and you will therefore get a screen where you can
select additional installer modules.  However, you can simply skip this
menu and and follow the normal installation procedure <a href =
"../install/">described in my guide</a>.

Go back to my <a href = "..">Debian on Cobalt</a> page.

