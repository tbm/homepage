---
title: "ledger2beancount 2.3 released"
date: 2020-06-26 11:45:29 +0800
---

I released version 2.3 of [ledger2beancount](https://github.com/zacchiro/ledger2beancount),
a ledger to beancount converter.

There are three notable changes with this release:

1. Performance has significantly improved.  One large, real-world test case has gone from around 160 seconds to 33 seconds.  A smaller test case has gone from 11 seconds to ~3.5 seconds.
2. The documentation is [available online now](https://ledger2beancount.readthedocs.io/) (via Read the Docs).
3. The [repository has moved](https://github.com/beancount/ledger2beancount) to the beancount GitHub organization.

Here are the changes in 2.3:

* Improve speed of ledger2beancount significantly
* Improve parsing of postings for accuracy and speed
* Improve support for inline math
* Handle lots without cost
* Fix parsing of lot notes followed by a virtual price
* Add support for lot value expressions
* Make parsing of numbers more strict
* Fix behaviour of dates without year
* Accept default ledger date formats without configuration
* Fix implicit conversions with negative prices
* Convert implicit conversions in a more idiomatic way
* Avoid introducing trailing whitespace with hledger input
* Fix loading of config file
* Skip ledger directive `import`
* Convert documentation to `mkdocs`

Thanks to Colin Dean for some feedback.  Thanks to Stefano Zacchiroli for prompting me into investigating performance issues (and thanks to the developers of the Devel::NYTProf profiler).

You can get [ledger2beancount from GitHub](https://github.com/beancount/ledger2beancount)
