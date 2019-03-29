---
title: "ledger2beancount 1.1 released"
date: 2018-05-01 10:19:08 +0200
---

Stefano Zacchiroli and I have published version 1.1 of [ledger2beancount](https://github.com/zacchiro/ledger2beancount),
a ledger to beancount converter.

Incompatible changes: If you already use ledger2beancount, please note
that the `payee_match` variable changed from a Yaml hash to a list (to
make the order deterministic).

Version 1.1 includes a number of bug fixes and enhancements based on
feedback from users.

Changes in version 1.1:

* Happy International Workers' Day release!
* Handle block comments without indentation correctly
* Preserve comments for postings with lots
* Use beancount's `pushtag/poptag` for ledger's `apply tag`
* Handle `tag` directives with associated commands correctly
* Allow option `link_match` to work with `tag_as_metadata: true`
* Handle posting-level tags without indentation correctly with
  `tag_as_metadata: false`
* Ensure `payee_match` is predictable
* Preserve comments for postings with lots
* Embed an optional beancount header to the converted file to
  specify beancount options
* Convert ledger metadata keys to valid beancount metadata keys
* Add conversion notes when accounts, commodities or metadata
  keys are automatically renamed by ledger2beancount
* Add capability to ignore certain lines
* Keep whitespace intact when renaming account names.
* Improve documentation on assigning payees based on transactions
* Add more test cases
* Run the test suite only if something has changed

You can get [ledger2beancount from GitHub](https://github.com/zacchiro/ledger2beancount).

