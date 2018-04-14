---
title: "X.org"
date: 2007-03-17 11:49:18 +0100
section: phd
---

In previous times, most Linux distributions and other free software
projects relied on the XFree86 system.  Over the years, the structures
within the XFree86 project became were rigid and the project failed to
innovate and keep up with the pace of the wider free software community.
When XFree86 changed its license in February 2004, the active community and
the majority of vendors quickly moved to X.org.  X.org is a very active
community and they decided to break up the monolithic code base and to
adopted a more modern build system.  As of X.org 7.0, the project moved to
the modular system in which components are developed and released
separately.  Effectively, the project introduced a development mechanism
which features two release mechanisms: individual components can be
released as needed and there is an overall release of X.org in which all
stable components are put together.  These roll-up releases take place
every six months.

<table class="table table-hover">

<thead>
<tr>
<th>Version</th>
<th>Date</th>
<th>Months></th>
</tr>
</thead>

<tbody>
<tr>
<td>7.0</td>
<td>2005-12-21</td>
<td></td>
</tr>

<tr>
<td>7.1</td>
<td>2006-05-22</td>
<td class="months">5</td>
</tr>

<tr>
<td>7.2</td>
<td>2007-02-15</td>
<td class="months">9</td>
</tr>
</tbody>

</table>

<h3>Past problems</h3>

<ul>

<li>XFree86 made only infrequent releases every few years, had no plan, and
the project's structures were very rigid.</li>

<li>The code base was huge and monolithic.  It had an archaic build system
that few new developers were comfortable with.  This made it hard for new
contributors to get involved and was bad for testing.</li>

</ul>

<h3>Solutions</h3>

<ul>

<li>X.org moved from a monolithic to a modular system.  This made it easier
to perform testing and it made it possible to give contributors write
access to specific components.</li>

<li>The move to the modular system allowed them the introduction of two
release mechanisms: individual components can make releases on an ongoing
basis and roll-up releases take place every six months.</li>

<li>The roll-up releases have a fall back mechanism in case a specific
component is not ready for release: the former release of this component
can be incorporated.</li>

</ul>

<h3>Outstanding problems</h3>

<ul>

<li>The project needs to work the interface between the server and drivers,
so updates to hardware drivers can be released more often than other
components.</li>

</ul>

