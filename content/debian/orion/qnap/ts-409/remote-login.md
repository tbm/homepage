---
title: Activating remote login on QNAP TS-409
nav: Activating remote login
description: Activating remote login in the QNAP TS-409 firmware
keywords: [Debian, QNAP, TS-409, installation, firmware, remote, login, telnet, SSH]
---

<% content_for :right do %>
<img src = "../images/r_ts409_front.jpg" class="border" alt="QNAP TS-409 from the front" width="148" height="147" />

<%= render 'adsense-wideskyscaper-right' %>
<% end %>

<h1>QNAP firmware: activating remote login</h1>

You can activate remote login (telnet and SSH) in the QNAP firmware by
following these steps.  First, click on <em>Administration</em> and enter
the password (by default the user is `admin` and the password is also
`admin`).  Then click on <em>Remote login</em> under <em>System Tools</em>.

<img src = "../../images/qnap-system-tools.png" class="border" alt = "QNAP firmware: overview" width="640" height="480" />

Finally, enable <em>telnet</em>, leave the port they use (13131) and press
<em>apply</em>.

<img src = "../../images/qnap-remote-login.png" class="border" alt = "QNAP firmware: remote login" width="640" height="480" />

Go back to the <a href = "../install">installing Debian on QNAP TS-409</a>
page.

<div class="bbf">
<%= render 'adsense-banner-before-footer' %>
</div>

