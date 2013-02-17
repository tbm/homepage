# TODO list

## v1.0 - Replicate existing homepage

* render: consistent use of quotation marks
* Verify that output is the same
* Apache redirects
* Remove whitespace caused by ERB
* Fix HTML validation errors

## v1.1 - Migrate blog from pyblosxom

* Convert existing blog entris to Markdown

## Later

* nav: Check consistency of upper/lower casing
* split out config data to config.yaml ("global site variable: store it in config.yaml and access it with @config[:stuff]")
* Convert more pages to Markdown
* nanoc 3.6: update left sidebare to use @item["/bio/"], etc
* blog: add "read more" tags?
* CV: automatically copy CV (pdf)?
* "Last updated" based on mtime or git log:
    * http://stackoverflow.com/questions/9184965/how-to-get-the-last-commit-date-of-a-file-with-ruby-grit
    * https://groups.google.com/forum/?fromgroups=#!topic/nanoc/tYR2FtP7p5o
* "Last updated": accept "pagespec"
* Add license to README and source files
* Add "outdated" banner and noindex

