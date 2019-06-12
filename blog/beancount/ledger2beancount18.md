---
title: "ledger2beancount 1.8 released"
date: 2019-06-12 16:32:51 +0700
---

I released version 1.8 of [ledger2beancount](https://github.com/zacchiro/ledger2beancount),
a ledger to beancount converter.

I ran ledger2beancount over the ledger test suite and made it much more
robust.  If ledger2beancount 1.8 can't parse your ledger file properly,
I'd like to know about it.

Here are the changes in 1.8:

* Add support for `apply year`
* Fix incorrect account mapping of certain accounts
* Handle fixated commodity and postings without amount
* Improve behaviour for invalid `end` without `apply`
* Improve error message when date can't be parsed
* Deal with account names consisting of a single letter
* Ensure account names don't end with a colon
* Skip ledger directives `eval`, `python`, and `value`
* Don't assume all filenames for `include` end in `.ledger`
* Support `price` directives with commodity symbols
* Support decimal commas in `price` directives
* Don't misparse balance assignment as commodity
* Ensure all beancount commodities have at least 2 characters
* Ensure all beancount metadata keys have at least 2 characters
* Don't misparse certain metadata as implicit conversion
* Avoid duplicate `commodity` directives for commodities with name collisions
* Recognise deferred postings
* Recognise `def` directive

Thanks to Alen Siljak for reporting a bug.

You can get [ledger2beancount from GitHub](https://github.com/zacchiro/ledger2beancount).

