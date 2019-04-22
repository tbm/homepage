---
title: "ledger2beancount 1.7 released"
date: 2019-04-22 13:38:14 +0700
---

I released version 1.7 of [ledger2beancount](https://github.com/zacchiro/ledger2beancount),
a ledger to beancount converter.

This release contains a number of bug fixes and a new feature:

* Don't misparse account and commodity with mixed tab/space separators
* Rename account names consisting of a root name without subaccount
* Warn when non-standard root names are used
* Avoid duplicate open directives for accounts with name collisions
* Don't warn for renamed tags that won't show up in the beancount file
* Add `account_regex` option to mass rename account names
* Add man page and improve documentation

You can get [ledger2beancount from GitHub](https://github.com/zacchiro/ledger2beancount).

Thanks to GitHub user Joradi98 for reporting some bugs.  Thanks to
Jelmer Vernooĳ for packaging ledger2beancount for Debian.

