---
title: "Debian"
date: 2007-03-14 09:42:53 +0100
---

The aim of Debian is to integrate software produced by other projects to
create a complete operating system based on free software.  In recent
years, the project has faced increasingly delayed and unpredictable
releases.  Most notably, the release process of Debian&nbsp;3.1 was
characterized by major delays.  Initially announced for December 1, 2003,
the software was finally released in June 2005: a delay of one and a half
years.  Since then, the project has made a number of improvements to its
release process.

<table class="table table-hover">

<thead>
<tr>
<th>Version</th>
<th>Date</th>
<th>Months</th>
</tr>
<thead>

<tbody>
<tr>
<td>1.1</td>
<td>1996-06-17</td>
<td></td>
</tr>

<tr>
<td>1.2</td>
<td>1996-12-12</td>
<td class="months">6</td>
</tr>

<tr>
<td>1.3</td>
<td>1997-06-02</td>
<td class="months">6</td>
</tr>

<tr>
<td>2.0</td>
<td>1998-07-24</td>
<td class="months">14</td>
</tr>

<tr>
<td>2.1</td>
<td>1999-03-09</td>
<td class="months">7</td>
</tr>

<tr>
<td>2.2</td>
<td>2000-08-14</td>
<td class="months">17</td>
</tr>

<tr>
<td>3.0</td>
<td>2002-07-19</td>
<td class="months">23</td>
</tr>

<tr>
<td>3.1</td>
<td>2005-06-06</td>
<td class="months">35</td>
</tr>
</tbody>

</table>

<h3>Past Problems</h3>

<ul>

<li>Release management was not very organized and release updates were
posted only infrequently.  Because of this and the lack of a roadmap,
freezes were often announced out of the blue.</li>

<li>Due to the unorganized nature of the release, several new and
unexpected blockers were found during the release process, leading to
delays.</li>

<li>The unexpected delays meant that software was frozen for a long time,
in the case of Debian 3.1 for over a year.  When this release was finally
published, many components were already out of date and would often not
meet user demands.</li>

<li>The fact that Debian has experienced significant delays with several of
its recent releases has led to problems with the image of the project.
There is a perception that Debian is slow and cannot meet deadlines.  This
is also associated with frustration in the developer and user
community.</li>

</ul>

<h3>Solutions</h3>

<ul>

<li>The project has implemented better release management structures.  In
particular, Debian moved from a single release manager to a team during the
3.1 release cycle.  The release is now handled by two release managers with
the help of several release assistants.</li>

<li>A release date for the next release <a href =
"http://lists.debian.org/debian-devel-announce/2005/10/msg00004.html">was
set well in advance</a> and there is more planning.</li>

<li>Release announcements are sent more frequently and various information
sources have been implemented through which developers can stay informed
about the release status.</li>

<li>Release targets have been defined better and there is <a href =
"http://lists.debian.org/debian-devel-announce/2006/07/msg00005.html">a
distinction between blockers and goals</a>.  Only blockers hold up the
release whereas goals can be postponed for a future release.  For example,
the XFree86 to X.org transition and the integration of AMD64 support were
blockers, while LSB 3.1 compatibility and SE Linux support were only goals
for Debian&nbsp;4.0.</li>

<li>The release team has shifted the responsibility of achieving targets to
specific developers and teams.  There are also better criteria now defining
these responsibilities.  For example, <a href =
"https://release.debian.org/etch/arch_policy.html">criteria have been
published</a> that architectures need to fulfil for inclusion in
Debian&nbsp;4.0 and there is <a href =
"https://release.debian.org/etch/arch_qualify.html">a page indicating the
status</a> of each architecture.</li>

<li>The release team is increasingly giving encouragement to developers to
help out with software packages and bugs which normally do not fall into
their domain.</li>

<li>A staged freeze has been implemented according to which software is
frozen in stages according to its importance.  The toolchain and base
system are frozen earlier than the majority of package.  The majority of
software is now frozen when most blockers have been resolved.</li>

<li>The use of the experimental repository has been promoted to make sure
that the main development repository is in a good shape most of the
time.</li>

</ul>

<h3>Outstanding problems</h3>

<ul>

<li>Developers still need to be convinced that targets can be met, that
deadlines are real and that Debian can release on time.</li>

</ul>

