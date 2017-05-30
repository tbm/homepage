# Homepage of Martin Michlmayr

This is the source for my personal homepage at <http://www.cyrius.com/>

I am currently in the process of converting this site to [nanoc](http://nanoc.ws/).
Everything has been converted to nanoc except for the blog.

## Requirements

Ruby dependencies are managed using bundler:

    bundle install

On Debian 8 (jessie), you can install the dependencies like this:

    apt-get install nanoc pandoc
    gem install pandoc-ruby w3c_validators

The site also requires various Debian packages:

    apt-get install make hunspell myspell-en-gb myspell-en-us

## Style guidelines

* All images in the right sidebar need to have a width of 148 pixels.

