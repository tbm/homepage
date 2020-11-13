---
title: "beancount2ledger 1.3 released"
date: 2020-11-13 20:12:16 +0800
---

I released version 1.3 of [beancount2ledger](https://beancount2ledger.readthedocs.io/), the beancount to ledger converter that was moved from `bean-report ledger` into a standalone tool.

You can get [beancount2ledger from GitHub](https://github.com/beancount/beancount2ledger) or via [pip install](https://pypi.org/project/beancount2ledger/).

Here are the changes in 1.3:

* Add rounding postings only when required ([issue #9](https://github.com/beancount/beancount2ledger/issues/9))
* Avoid printing too much precision for a currency ([issue #21](https://github.com/beancount/beancount2ledger/issues/21))
* Avoid creating two or more postings with null amount ([issue #23](https://github.com/beancount/beancount2ledger/issues/23))
* Add price to cost when needed by ledger ([issue #22](https://github.com/beancount/beancount2ledger/issues/22))
* Preserve posting order ([issue #18](https://github.com/beancount/beancount2ledger/issues/18))
* Add config option `indent`
* Show metadata with hledger output
* Support setting auxiliary dates and posting dates from metadata ([issue #14](https://github.com/beancount/beancount2ledger/issues/14))
* Support setting the code of transactions from metadata
* Support mapping of account and currency names ([issue #24](https://github.com/beancount/beancount2ledger/issues/24))
* Improve documentation:
    * Add user guide
    * Document limitations ([issue #12](https://github.com/beancount/beancount2ledger/issues/12))
