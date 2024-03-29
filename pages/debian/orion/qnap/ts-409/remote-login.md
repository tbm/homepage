---
title: Activating remote login on QNAP TS-409
nav: Activating remote login
description: Activating remote login in the QNAP TS-409 firmware
keywords: [Debian, QNAP, TS-409, installation, firmware, remote, login, telnet, SSH]
---

<div class="right">
<img src = "../images/r_ts409_front.jpg" class="border" alt="QNAP TS-409 from the front" width="148" height="147" />
</div>

You can activate remote login (telnet and SSH) in the QNAP firmware by
following these steps.  First, click on <em>Administration</em> and enter
the password (by default the user is `admin` and the password is also
`admin`).  Then look for <em>Remote login</em>.  This can be found under
<em>System Tools</em> on older versions of the QNAP firmware and under
<em>Network Services</em> on newer versions.

<img src = "../../images/qnap-system-tools.png" class="border" alt = "QNAP firmware: overview" width="640" height="480" />

Finally, enable <em>telnet</em>, leave the port they use (13131) and press
<em>apply</em>.

<img src = "../../images/qnap-remote-login.png" class="border" alt = "QNAP firmware: remote login" width="640" height="480" />


