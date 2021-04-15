---
title: "ledger2beancount 2.6 released"
date: 2021-04-15 13:18:30 +0800
---

I released version 2.5 of [ledger2beancount](https://github.com/beancount/ledger2beancount), a ledger to beancount converter.

Here are the changes in 2.6:

* Round calculated total if needed for `price==cost` comparison
* Add `narration_tag` config variable to set narration from metadata
* Retain unconsummated payee/payer metadata
* Ensure UTF-8 output and assume UTF-8 input
* Document UTF-8 issue on Windows systems
* Add option to move posting-level tags to the transaction itself
* Add support for the `alias` sub-directive of `account` declarations
* Add support for the `payee` sub-directive of `account` declarations
* Support configuration file called `.ledger2beancount.yaml`
* Fix uninitialised value warning in hledger mode
* Print warning if account in assertion has sub-accounts
* Set commodity for commodity-less balance assertion
* Expand path name of `beancount_header` config variable
* Document handling of buckets
* Document pre- and post-processing examples
* Add `Dockerfile` to create Docker image

Thanks to Alexander Baier, Daniele Nicolodi, and GitHub users bratekarate, faaafo and mefromthepast for various bug reports and other input.

Thanks to Dennis Lee for adding a Dockerfile and to Vinod Kurup for fixing a bug.

Thanks to Stefano Zacchiroli for testing.

You can get [ledger2beancount from GitHub](https://github.com/beancount/ledger2beancount).
