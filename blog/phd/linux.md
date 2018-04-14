---
title: "Linux kernel"
date: 2007-03-15 16:31:49 +0100
section: phd
---

The Linux kernel project has seen major changes to its development and
release strategy in the last few years, in particular since the first
stable release of the 2.6 series in December 2003.  This series was opened
almost three years after the 2.4 series in January 2001, which many felt
was too long.  A problem that resulted from the long interval between major
releases was that vendors had to back- and forward-port a lot of patches.
Nowadays, major development happens on the 2.6 series and new releases are
published every three to four months.  This new development model has faced
much controversy.  While some people, in particular developers of the
kernel, claim that the new model is working very well, some users are
worried about the number of significant changes and lack of stability in
the kernel.  Andrew Morton, a lead developer, has expressed several times
that he believes the kernel is getting buggier.

<table class="phd">

<tr>
<th>Version</th>
<th>Date</th>
<th>Months</th>
</tr>

<tr>
<td>1.0</td>
<td>1994-03-14</td>
<td></td>
</tr>

<tr>
<td>1.2</td>
<td>1995-03-07</td>
<td class="months">12</td>
</tr>

<tr>
<td>2.0</td>
<td>1996-06-09</td>
<td class="months">15</td>
</tr>

<tr>
<td>2.2</td>
<td>1999-01-25</td>
<td class="months">31</td>
</tr>

<tr>
<td>2.4</td>
<td>2001-01-04</td>
<td class="months">23</td>
</tr>

<tr>
<td>2.6</td>
<td>2003-12-17</td>
<td class="months">35</td>
</tr>

</table>

<h3>Past problems</h3>

<ul>

<li>Because of the long release cycle, many changes accumulated.  It was
hard to get the development stable and there were few testers.</li>

<li>Features got out very slowly because of the long release cycle.</li>

<li>Hardware support and crucial features had to be backported to the
latest stable kernel.</li>

<li>Vendors backported many features to their own releases.  The code base
from different vendors diverged a lot from each other and from the official
development version.</li>

</ul>

<h3>Solutions</h3>

<ul>

<li>New versions are now released every two or three months.  There is a
two week merge window after each release during which new features are
accepted; subsequently, the focus is on stabilization.</li>

<li>There is now a steady flow of code into production and many people get
to test the new code.</li>

<li>Features get out more quickly.</li>

<li>Vendors can directly work with current releases and get their changes
into official versions easily.</li>

</ul>

<h3>Outstanding problems</h3>

<ul>

<li>There is no long-term stable version based on the 2.6 kernel.  This is
being addressed with Adrian Bunk's 2.6.16 long-term maintenance tree but
whether it will have a big impact remains to be seen.</li>

<li>Regressions between versions are introduced more frequently.  Better
control and tracking of regressions are needed.</li>

<li>The Bugzilla bug tracker needs to be integrated better into the
development process and it would be helpful to have a QA person.  In
January 2007, Google announced that they're looking for a kernel QA person
who'd work together with Andrew Morton.</li>

</ul>

