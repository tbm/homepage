---
title: "beancount2ledger 1.1 released"
date: 2020-07-24 15:04:56 +0800
---

Martin Blais recently [announced that he'd like to re-organize the beancount code](https://groups.google.com/forum/#!topic/beancount/kM4s4raf1y4) and split out some functionality into separate projects, including the beancount to ledger/hledger conversion code previously provided by bean-report.

I agreed to take on the maintenance of this code and I've now released [beancount2ledger, a beancount to ledger/hledger converter](https://github.com/beancount/beancount2ledger/).

You can install beancount2ledger with pip:

    pip3 install beancount2ledger

Please [report issues to the GitHub tracker](https://github.com/beancount/beancount2ledger/issues).

There are a number of outstanding issues I'll fix soon, but please report any other issues you encounter.

Note that I'm not very familiar with hledger.  I intend to sync up with hledger author Simon Michael soon, but please file an issue if you notice any problems with the hledger conversion.

Version 1.1 contains a number of fixes compared to the latest code in bean-report:

## 1.1 (2020-07-24)

* Preserve metadata information ([issue #3](https://github.com/beancount/beancount2ledger/issues/3))
* Preserve cost information (lot dates and lot labels/notes) ([issue #5](https://github.com/beancount/beancount2ledger/issues/5))
* Avoid adding two prices in hledger ([issue #2](https://github.com/beancount/beancount2ledger/issues/2))
* Avoid trailing whitespace in account open declarations ([issue #6](https://github.com/beancount/beancount2ledger/issues/6))
* Fix indentation issue in postings ([issue #8](https://github.com/beancount/beancount2ledger/issues/8))
* Fix indentation issue in price entries
* Drop time information from price (`P`) entries
* Add documentation
* Relicense under GPL-2.0-or-later ([issue #1](https://github.com/beancount/beancount2ledger/issues/1))

## 1.0 (2020-07-22)

* Split ledger and hledger conversion from `bean-report` into a standalone tool
* Add man page for `beancount2ledger`(1)

