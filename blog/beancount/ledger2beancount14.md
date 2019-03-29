---
title: "ledger2beancount 1.4 released"
date: 2018-12-01 14:42:37 +0200
---

Stefano Zacchiroli and I released version 1.4 of [ledger2beancount](https://github.com/zacchiro/ledger2beancount),
a ledger to beancount converter.

Version 1.4 contains a number of bug fixes:

* Don't parse trailing whitespace as part of the account name
* Replace commodities in lot costs
* Avoid mangling of lot cost with other lot information
* Don't require whitespace between `{}` and `@` in lot information

You can get [ledger2beancount from GitHub](https://github.com/zacchiro/ledger2beancount).

