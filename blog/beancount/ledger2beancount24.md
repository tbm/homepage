---
title: "ledger2beancount 2.4 released"
date: 2020-07-27 16:07:57 +0800
---

I released version 2.4 of [ledger2beancount](https://github.com/beancount/ledger2beancount), a ledger to beancount converter.

There are two notable changes in this release:

1. I fixed two regressions introduced in the last release.  Sorry about the breakage!
2. I improved support for hledger.  I believe all syntax differences in hledger are supported now.

Here are the changes in 2.4:

* Fix regressions introduced in version 2.3
    * Handle price directives with comments
    * Don't assume implicit conversion when price is on second posting
* Improve support for hledger
    * Fix parsing of hledger tags
    * Support commas as decimal markers
    * Support digit group marks through `commodity` and `D` directives
    * Support `end aliases` directive
    * Support regex aliases
    * Recognise total balance assertions
    * Recognise sub-account balance assertions
* Add support for `define` directive
* Convert all uppercase metadata tags to all lowercase
* Improve handling of ledger lots without cost
* Allow transactions without postings
* Fix parsing issue in commodity declarations
* Support commodities that contain quotation marks
* Add `--version` option to show version
* Document problem of mixing `apply` and `include`

Thanks to Kirill Goncharov for pointing out one regressions, to Taylor R Campbell for for a patch, to Stefano Zacchiroli for some input, and finally to Simon Michael for input on hledger!

You can get [ledger2beancount from GitHub](https://github.com/beancount/ledger2beancount)
