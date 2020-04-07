---
title: "ledger2beancount 2.1 released"
date: 2020-04-06 19:38:00 +0800
---

I released version 2.1 of [ledger2beancount](https://github.com/zacchiro/ledger2beancount),
a ledger to beancount converter.

Here are the changes in 2.1:

* Handle postings with posting dates and comments but no amount
* Show transactions with only one posting (without `bucket`)
* Adding spacing between automatic declarations
* Preserve preliminary info at the top

You can get [ledger2beancount from GitHub](https://github.com/zacchiro/ledger2beancount).

Thanks to Thierry (thdox) for reporting a bug and for fixing some
typos in the documentation.  Thanks to Stefano Zacchiroli for
some good feedback.

