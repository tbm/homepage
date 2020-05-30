---
title: "ledger2beancount 2.2 released"
date: 2020-05-30 10:22:02 +0800
---

I released version 2.2 of [ledger2beancount](https://github.com/zacchiro/ledger2beancount),
a ledger to beancount converter.

Here are the changes in 2.2:

* Show warning for unknown `apply` directive
* Recognize `apply rate` directive (an alias of `apply fixed`)
* Don't convert meta-data on ignored virtual postings but keep as comments
* Update location of beancount repository

You can get [ledger2beancount from GitHub](https://github.com/zacchiro/ledger2beancount).

Thanks to GitHub user MarinBernard for reporting a bug with virtual
postings!
