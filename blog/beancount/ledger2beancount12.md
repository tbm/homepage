---
title: "ledger2beancount 1.2 released"
date: 2018-05-17 13:22:06 +0200
---

Stefano Zacchiroli and I released version 1.2 of [ledger2beancount](https://github.com/zacchiro/ledger2beancount),
a ledger to beancount converter.

This version of ledger2beancount is compatible with beancount 2.1, which
was released a few days ago.

Changes in version 1.2:

* Updates for beancount 2.1.0:
    * Allow UTF-8 letters and digits in account names
    * Allow full-line comments in transactions
    * Allow transaction tags and links on multiple lines
* Handle posting tags on multiple lines
* Always convert posting-level tags to metadata
* Improve parsing of the transaction header

You can get [ledger2beancount from GitHub](https://github.com/zacchiro/ledger2beancount).

