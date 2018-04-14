---
title: "Open Source Contributor Agreements: Some Examples"
date: 2010-08-18 16:10:16 +0100
section: fossbazaar
---

The <a href =
"/blog/fossbazaar/contributor-agreements-purpose-scope">first part</a>
of this article explained the purpose and scope of Contributor
Agreements in open source projects.  This article presents an overview
of some Contributor Agreements that are used in the community.

Contributor Agreements come in all shape and forms, ranging from
full-fledged Contributor License Agreements (CLA) that have to be signed
to informal consent to some set of rules.  This article will take a look
at a number of different agreements in order to show that community
norms can vary widely.

<h3>Apache's Individual Contributor License Agreement</h3>

The Apache Software Foundation (ASF) maintains two formal Contributor
License Agreements (CLA), one for individual contributors and one for
corporate contributions.  The <a href =
"http://www.apache.org/licenses/icla.txt">Individual CLA</a> covers the
following points:

<ul>

<li>Contributors grant the ASF and recipients of software distributed by
the ASF a broad copyright license.</li>

<li>Contributors grant a patent license to their contributions.</li>

<li>Contributors acknowledge that they are legally entitled to grant the
above license.</li>

<li>Contributors acknowledge that each of their contributions is their
original creation.</li>

<li>Contributors are not expected to provide support for their
contributions, except to the extent they desire to provide support.</li>

<li>How to handle submissions of work that that is not their original
creation (i.e. works by a third-party).</li>

<li>Contributors agree to notify the ASF when any circumstances
change.</li>

</ul>

<h3>Fedora Project Contributor Agreement</h3>

Fedora is in the process of adopting the Fedora Project Contributor
Agreement (FPCA), which covers the following points:

<ul>

<li>Contributors have to ensure that they have proper permission to make
a contribution.  For example, they can ask their employers to put the
contribution under an open source license that Fedora accepts.</li>

<li>If a contribution has a license, this license is followed.</li>

<li>Fedora defines some default licenses for contributions which don't
explicitly state the license.  For code contributions, the MIT is used;
the Creative Commons Attribution ShareAlike 3.0 Unported license is used
for content.</li>

</ul>

The Fedora Project Contributor Agreement does not require contributors
to assign copyright to Fedora or Red Hat.

<h3>Linux kernel Developer's Certificate of Origin</h3>

The Linux kernel project has adopted the Developer's Certificate of
Origin.  Developers use it to assert the following points:

<ul>

<li>The contribution was created by me and I have the right to submit it
under the indicated open source license.</li>

<li>The contribution is based on previous work that is also under the
indicated license.</li>

<li>The contribution was provided directly to me by someone who
certified it and I didn't modify it. -- This clause is useful because
contributions pass through subsystem maintainers without modification
until they reach Linus Torvalds, the maintainer of the Linux
kernel.</li>

<li>I understand that the contribution and project are public and
recorded. -- This has nothing to do with code origin but with privacy,
as all the work on the Linux kernel is done in the public.</li>

</ul>

The way by which developers accept the Developer's Certificate of Origin
for each contribution is to put a `Signed-off-by` line with their
name between the description of their change and the actual change.

<h3>Debian's Social Contract</h3>

While Debian has no formal Contributor Agreement per se, all
contributors who become official members of the project have to accept
<a href = "http://www.debian.org/social_contract">Debian's Social
Contract</a> for their Debian related activities.  Among other things,
the Social Contract states that "Debian will remain 100% free" (free
according to the Debian Free Software Guidelines).  Therefore, it can be
implied that all contributions to Debian made by members of the project
are open source.  The license of contributions without explicit license
statements is not clear since Debian does not define a default license
like Fedora.  However, Debian developers are encouraged to specify the
copyright and license information for their submissions in the
`debian/copyright` file of their software packages.

