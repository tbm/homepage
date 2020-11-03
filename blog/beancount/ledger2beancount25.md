---
title: "ledger2beancount 2.5 released"
date: 2020-11-03 15:52:18 +0800
---

I released version 2.5 of [ledger2beancount](https://github.com/beancount/ledger2beancount), a ledger to beancount converter.

Here are the changes in 2.5:

* Don't create negative cost for lot without cost
* Support complex implicit conversions
* Handle typed metadata with value `0` correctly
* Set per-unit instead of total cost when cost is missing from lot
* Support commodity-less amounts
* Convert transactions with no amounts or only `0` amounts to notes
* Fix parsing of transaction notes
* Keep tags in transaction notes on same line as transaction header
* Add beancount config options for non-standard root names automatically
* Fix conversion of fixated prices to costs
* Fix removal of price when `price==cost` but when they use different number formats
* Fix removal of price when `price==cost` but per-unit and total notation mixed
* Fix detection of tags and metadata after posting/aux date
* Use `D` directive to set default commodity for hledger
* Improve support for postings with commodity-less amounts
* Allow empty comments
* Preserve leading whitespace in comments in postings and transaction headers
* Preserve indentation for tags and metadata
* Preserve whitespace between amount and comment
* Refactor code to use more data structures
* Remove dependency on `Config::Onion` module

Thanks to input from Remco Rĳnders, Yuri Khan, and Thierry. Thanks to Stefano Zacchiroli and Kirill Goncharov for testing my changes.

You can get [ledger2beancount from GitHub](https://github.com/beancount/ledger2beancount)
