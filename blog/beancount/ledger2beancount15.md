---
title: "ledger2beancount 1.5 released"
date: 2019-01-30 10:38:16 -0300
---

Stefano Zacchiroli and I released version 1.5 of [ledger2beancount](https://github.com/zacchiro/ledger2beancount),
a ledger to beancount converter.

This release contains a number of bug fixes and new features:

* Replace commodities in balance assertions
* Add support for posting-level dates
* Add support for hledger features
* Add support for balance assignments
* Handle comments on the same line as the payee
* Handle comments, tags and metadata on postings with balance assertions
* Handle metadata on postings with cost or price information
* Handle simple implicit conversions

You can get [ledger2beancount from GitHub](https://github.com/zacchiro/ledger2beancount).

