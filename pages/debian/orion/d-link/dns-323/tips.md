---
title: Tips and tricks for for Debian on the D-Link DNS-323
nav: Tips
keywords: [Debian, D-Link, DNS-323, Conceptronic, CH3SNAS, tips, tricks]
---

<div class="right">
<img src = "../images/r_ch3snas_front.jpg" class="border" alt="Conceptronic CH3SNAS from the front" width="148" height="146" />
</div>

Here are some tips and tricks about running Debian on the D-Link DNS-323
and Conceptronic CH3SNAS.

<h2 id="fan-control">Controlling the fan</h2>

According to Anselmo Luginbuhl, you should be able to use the `lm-sensors`
package to automatically control the fan:

"Execute `pwmconfig`, it will make some tests and generate the fancontrol
config file. At the end of the procedure it will ask you to "Select fan
output to configure, or other action:", just be sure to pass through choice
"1" or it would not fill in the configuration file, save the configuration
and start the daemon `/etc/init.d/fancontrol`.

Probably the only thing that needs some attention to get an optimal result
is to choose the right parameters for max and min temperature at which the
fan should start or stop to minimize the °C and the noise."

