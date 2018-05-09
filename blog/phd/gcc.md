---
title: "GCC"
date: 2007-03-14 15:41:55 +0100
---

The GNU Compiler Collection (GCC) is a compiler suite which supports a
number of programming languages, such as C and C++.  It is a very important
development tool and is the standard compiler among free software projects.
GCC was quite stagnant in the middle of the 1990s until the EGCS project
formed.  EGCS took over development of the official GCC in October 1998 and
instituted rigorous processes, such as high levels of peer review, and
created a steering committee which has the power to appoint maintainers and
make important decisions.  In theory, the project follows a time based
release with an interval of six months.  In practice, the project has
released only one new version every year in recent times.

<table class="table table-hover">

<thead>
<tr>
<th>Version</th>
<th>Date</th>
<th>Months</th>
</tr>
</thead>

<tbody>
<tr>
<td>3.0</td>
<td>2001-06-18</td>
<td></td>
</tr>

<tr>
<td>3.1</td>
<td>2002-05-15</td>
<td class="months">11</td>
</tr>

<tr>
<td>3.2</td>
<td>2002-08-14</td>
<td class="months">3</td>
</tr>

<tr>
<td>3.3</td>
<td>2003-05-13</td>
<td class="months">9</td>
</tr>

<tr>
<td>3.4.0</td>
<td>2004-04-18</td>
<td class="months">11</td>
</tr>

<tr>
<td>4.0.0</td>
<td>2005-04-20</td>
<td class="months">12</td>
</tr>

<tr>
<td>4.1.0</td>
<td>2006-02-28</td>
<td class="months">10</td>
</tr>
</tbody>

</table>

<h3>Past problems</h3>

<ul>

<li>The GCC project suffered from a closed development style in the past:
few people could make code changes and the mailing list was by invitation
only.</li>

<li>There was a long time between releases and development snapshots, which
contained bug fixes and features, were not available to the public.</li>

<li>When development opened and picked up, significant code changes were
often made which required a long stabilization phase.</li>

</ul>

<h3>Solutions</h3>

<ul>

<li>The project moved to a more open development style and established a
steering committee which has the power to appoint new maintainers and make
important decisions.</li>

<li>The development process was divided into <a href =
"http://gcc.gnu.org/develop.html">three stages</a> in order to coordinate
code submissions and keep the development tree reasonable stable.  Major
changes that developers wish to make during stage 1 and stage 2 have to be
<a href = "http://gcc.gnu.org/wiki/GCC_4.3_Release_Planning">proposed on
the project's wiki</a>.  Proposals are reviewed by the release manager who
also assign a sequence to proposed projects which says when they can be
applied to the development tree.</li>

<li>All patches are peer reviewed on the development mailing list and need
approval before they can be applied.  The steering committee appoints
maintainers who can approve patches that touch particular areas.  There are
maintainers for the C front-end, various port maintainers, and maintainers
for other areas.</li>

<li>Each development stage lasts two months, theoretically yielding a
release every six months.  A regular release cycle ensures that it is not
the end of the world if a feature does not make it into the following
release.</li>

</ul>

<h3>Outstanding problems</h3>

<ul>

<li>The release manager is busy and has not pushed the release forwards as
much as would be possible.</li>

<li>The branch criteria may need revision to make it easier to create a
branch which leads to the next stable version.  At the moment, the branch
criteria is to have 100 or less regressions on the development tree.
However, this number may include regressions that are also present in
previous releases, which makes it fairly hard to reach this criteria.</li>

</ul>

