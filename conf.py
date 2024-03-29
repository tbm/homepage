# -*- coding: utf-8 -*-

from __future__ import unicode_literals
import time

BLOG_AUTHOR = "Martin Michlmayr"
BLOG_TITLE = "Martin Michlmayr"
BLOG_EMAIL = "tbm@cyrius.com"
SITE_URL = "https://www.cyrius.com/"
BLOG_DESCRIPTION = "Martin Michlmayr's homepage"

DEFAULT_LANG = "en"

TRANSLATIONS = {
    DEFAULT_LANG: "",
}

NAVIGATION_LINKS = {
    DEFAULT_LANG: (
        ("/bio/", "Biography"),
        ("/blog/", "Blog"),
        ("/publications/", "Publications"),
        ("/foss-foundations/", "FOSS Foundations"),
        ("/debian/", "Debian HOWTOs"),
        ("/contact/", "Contact"),
    ),
}

# Alternative navigation links. Works the same way NAVIGATION_LINKS does,
# although themes may not always support them. (translatable)
# (Bootstrap 4: right-side of navbar, Bootblog 4: right side of title)
NAVIGATION_ALT_LINKS = {
    DEFAULT_LANG: (
        ("/blog/feed/", '<i class="fas fa-rss"></i>'),
        ("https://github.com/tbm", '<i class="fab fa-github"></i>'),
        ("https://twitter.com/MartinMichlmayr", '<i class="fab fa-twitter"></i>'),
        ("https://www.linkedin.com/in/martinmichlmayr/", '<i class="fab fa-linkedin"></i>'),
    ),

}

THEME = "bootstrap4"

THEME_COLOR = '#2C3E50'

POSTS = (
    ("blog/*.md", "blog", "post.tmpl"),
    ("blog/*.rst", "blog", "post.tmpl"),
)
PAGES = (
    ("pages/*.md", "", "page.tmpl"),
    ("pages/*.rst", "", "page.tmpl"),
)

TIMEZONE = "UTC"

FILES_FOLDERS = {'files': ''}

COMPILERS = {
    "rest": ('.rst', '.txt'),
    "markdown": ('.md', '.mdown', '.markdown'),
    "html": ('.html', '.htm'),
}

METADATA_FORMAT = "YAML"

# Writes tag cloud data in form of tag_cloud_data.json.
# Warning: this option will change its default value to False in v8!
WRITE_TAG_CLOUD = False

# Final locations are:
# output / TRANSLATION[lang] / TAG_PATH / index.html (list of tags)
# output / TRANSLATION[lang] / TAG_PATH / tag.html (list of posts for a tag)
# output / TRANSLATION[lang] / TAG_PATH / tag.xml (RSS feed for a tag)
# (translatable)
TAG_PATH = "blog/tags"

# By default, the list of tags is stored in
#     output / TRANSLATION[lang] / TAG_PATH / index.html
# (see explanation for TAG_PATH). This location can be changed to
#     output / TRANSLATION[lang] / TAGS_INDEX_PATH
# with an arbitrary relative path TAGS_INDEX_PATH.
# (translatable)
# TAGS_INDEX_PATH = "tags.html"

# If TAG_PAGES_ARE_INDEXES is set to True, each tag's page will contain
# the posts themselves. If set to False, it will be just a list of links.
# TAG_PAGES_ARE_INDEXES = False

# Set descriptions for tag pages to make them more interesting. The
# default is no description. The value is used in the meta description
# and displayed underneath the tag list or index page’s title.
# TAG_PAGES_DESCRIPTIONS = {
#    DEFAULT_LANG: {
#        "blogging": "Meta-blog posts about blogging about blogging.",
#        "open source": "My contributions to my many, varied, ever-changing, and eternal libre software projects."
#    },
# }

# Set special titles for tag pages. The default is "Posts about TAG".
# TAG_PAGES_TITLES = {
#    DEFAULT_LANG: {
#        "blogging": "Meta-posts about blogging",
#        "open source": "Posts about open source software"
#    },
# }

# If you do not want to display a tag publicly, you can mark it as hidden.
# The tag will not be displayed on the tag list page, the tag cloud and posts.
# Tag pages will still be generated.
#HIDDEN_TAGS = ['mathjax']

# Final locations are:
# output / TRANSLATION[lang] / CATEGORY_PATH / index.html (list of categories)
# output / TRANSLATION[lang] / CATEGORY_PATH / CATEGORY_PREFIX category.html (list of posts for a category)
# output / TRANSLATION[lang] / CATEGORY_PATH / CATEGORY_PREFIX category RSS_EXTENSION (RSS feed for a category)
# (translatable)
# CATEGORY_PATH = "categories"
# CATEGORY_PREFIX = "cat_"

# By default, the list of categories is stored in
#     output / TRANSLATION[lang] / CATEGORY_PATH / index.html
# (see explanation for CATEGORY_PATH). This location can be changed to
#     output / TRANSLATION[lang] / CATEGORIES_INDEX_PATH
# with an arbitrary relative path CATEGORIES_INDEX_PATH.
# (translatable)
CATEGORIES_INDEX_PATH = "blog/categories/index.html"

# If CATEGORY_ALLOW_HIERARCHIES is set to True, categories can be organized in
# hierarchies. For a post, the whole path in the hierarchy must be specified,
# using a forward slash ('/') to separate paths. Use a backslash ('\') to escape
# a forward slash or a backslash (i.e. '\//\\' is a path specifying the
# subcategory called '\' of the top-level category called '/').
CATEGORY_ALLOW_HIERARCHIES = True
# If CATEGORY_OUTPUT_FLAT_HIERARCHY is set to True, the output written to output
# contains only the name of the leaf category and not the whole path.
CATEGORY_OUTPUT_FLAT_HIERARCHY = False

# If CATEGORY_PAGES_ARE_INDEXES is set to True, each category's page will contain
# the posts themselves. If set to False, it will be just a list of links.
# CATEGORY_PAGES_ARE_INDEXES = False

# Set descriptions for category pages to make them more interesting. The
# default is no description. The value is used in the meta description
# and displayed underneath the category list or index page’s title.
CATEGORY_DESCRIPTIONS = {
   DEFAULT_LANG: {
        "beancount": "Open source accouting, including beancount and fava",
        "fossbazaar": "Posts from the open source governance site FOSSBazaar",
        "phd": "PhD research on open source release management",
   },
}

# Set special titles for category pages. The default is "Posts about CATEGORY".
CATEGORY_TITLES = {
    DEFAULT_LANG: {
        "debian": "Posts about Debian",
        "fossbazaar": "Posts from FOSSBazaar",
        "phd": "Posts about my PhD research"
    },
}

# If you do not want to display a category publicly, you can mark it as hidden.
# The category will not be displayed on the category list page.
# Category pages will still be generated.
HIDDEN_CATEGORIES = []

# A list of dictionaries specifying categories which translate to each other.
# Format: a list of dicts {language: translation, language2: translation2, …}
# See TAG_TRANSLATIONS example above.
# CATEGORY_TRANSLATIONS = []

# If set to True, a category in a language will be treated as a translation
# of the literally same category in all other languages. Enable this if you
# do not translate categories, for example.
# CATEGORY_TRANSLATIONS_ADD_DEFAULTS = True

# If no category is specified in a post, the destination path of the post
# can be used in its place. This replaces the sections feature. Using
# category hierarchies is recommended.
CATEGORY_DESTPATH_AS_DEFAULT = True

# If True, the prefix will be trimmed from the category name, eg. if the
# POSTS destination is "foo/bar", and the path is "foo/bar/baz/quux",
# the category will be "baz/quux" (or "baz" if only the first directory is considered).
# Note that prefixes coming from translations are always ignored.
CATEGORY_DESTPATH_TRIM_PREFIX = True

# If True, only the first directory of a path will be used.
CATEGORY_DESTPATH_FIRST_DIRECTORY_ONLY = True

# Map paths to prettier category names. (translatable)
CATEGORY_DESTPATH_NAMES = {
    DEFAULT_LANG: {
    },
}

# By default, category indexes will appear in CATEGORY_PATH and use
# CATEGORY_PREFIX. If this is enabled, those settings will be ignored (except
# for the index) and instead, they will follow destination paths (eg. category
# 'foo' might appear in 'posts/foo'). If the category does not come from a
# destpath, first entry in POSTS followed by the category name will be used.
# For this setting, category hierarchies are required and cannot be flattened.
CATEGORY_PAGES_FOLLOW_DESTPATH = True


# Final location for the main blog page and sibling paginated pages is
# output / TRANSLATION[lang] / INDEX_PATH / index-*.html
INDEX_PATH = "blog"


# Optional HTML that displayed on “main” blog index.html files.
# May be used for a greeting. (translatable)
FRONT_INDEX_HEADER = {
    DEFAULT_LANG: ''
}

# Create per-month archives instead of per-year
# CREATE_MONTHLY_ARCHIVE = False
# Create one large archive instead of per-year
CREATE_SINGLE_ARCHIVE = True
# Create year, month, and day archives each with a (long) list of posts
# (overrides both CREATE_MONTHLY_ARCHIVE and CREATE_SINGLE_ARCHIVE)
CREATE_FULL_ARCHIVES = True
# If monthly archives or full archives are created, adds also one archive per day
# CREATE_DAILY_ARCHIVE = False
# Create previous, up, next navigation links for archives
# CREATE_ARCHIVE_NAVIGATION = False
# Final locations for the archives are:
# output / TRANSLATION[lang] / ARCHIVE_PATH / ARCHIVE_FILENAME
# output / TRANSLATION[lang] / ARCHIVE_PATH / YEAR / index.html
# output / TRANSLATION[lang] / ARCHIVE_PATH / YEAR / MONTH / index.html
# output / TRANSLATION[lang] / ARCHIVE_PATH / YEAR / MONTH / DAY / index.html
ARCHIVE_PATH = "blog"
ARCHIVE_FILENAME = "archive/index.html"

# If ARCHIVES_ARE_INDEXES is set to True, each archive page which contains a list
# of posts will contain the posts themselves. If set to False, it will be just a
# list of links.
# ARCHIVES_ARE_INDEXES = False

# URLs to other posts/pages can take 3 forms:
# rel_path: a relative URL to the current page/post (default)
# full_path: a URL with the full path from the root
# absolute: a complete URL (that includes the SITE_URL)
# URL_TYPE = 'rel_path'

# Final location for the blog main RSS feed is:
# output / TRANSLATION[lang] / RSS_PATH / rss.xml
# (translatable)
RSS_PATH = "blog/feed/"

# Slug the Tag URL. Easier for users to type, special characters are
# often removed or replaced as well.
# SLUG_TAG_PATH = True

# Slug the Author URL. Easier for users to type, special characters are
# often removed or replaced as well.
# SLUG_AUTHOR_PATH = True

# A list of redirection tuples, [("foo/from.html", "/bar/to.html")].
#
# A HTML file will be created in output/foo/from.html that redirects
# to the "/bar/to.html" URL. notice that the "from" side MUST be a
# relative URL.
#
# If you don't need any of these, just set to []
REDIRECTIONS = []

# Presets of commands to execute to deploy. Can be anything, for
# example, you may use rsync:
# "rsync -rav --delete output/ joe@my.site:/srv/www/site"
# And then do a backup, or run `nikola ping` from the `ping`
# plugin (`nikola plugin -i ping`).  Or run `nikola check -l`.
# You may also want to use github_deploy (see below).
# You can define multiple presets and specify them as arguments
# to `nikola deploy`.  If no arguments are specified, a preset
# named `default` will be executed.  You can use as many presets
# in a `nikola deploy` command as you like.
# DEPLOY_COMMANDS = {
#     'default': [
#         "rsync -rav --delete output/ joe@my.site:/srv/www/site",
#     ]
# }

# github_deploy configuration
# For more details, read the manual:
# https://getnikola.com/handbook.html#deploying-to-github
# You will need to configure the deployment branch on GitHub.
GITHUB_SOURCE_BRANCH = 'src'
GITHUB_DEPLOY_BRANCH = 'master'

# The name of the remote where you wish to push to, using github_deploy.
GITHUB_REMOTE_NAME = 'origin'

# Whether or not github_deploy should commit to the source branch automatically
# before deploying.
GITHUB_COMMIT_SOURCE = True

# Where the output site should be located
# If you don't use an absolute path, it will be considered as relative
# to the location of conf.py
# OUTPUT_FOLDER = 'output'

# where the "cache" of partial generated content should be located
# default: 'cache'
# CACHE_FOLDER = 'cache'

# Filters to apply to the output.
# A directory where the keys are either: a file extensions, or
# a tuple of file extensions.
#
# And the value is a list of commands to be applied in order.
#
# Each command must be either:
#
# A string containing a '%s' which will
# be replaced with a filename. The command *must* produce output
# in place.
#
# Or:
#
# A python callable, which will be called with the filename as
# argument.
#
# By default, only .php files uses filters to inject PHP into
# Nikola’s templates. All other filters must be enabled through FILTERS.
#
# Many filters are shipped with Nikola. A list is available in the manual:
# <https://getnikola.com/handbook.html#post-processing-filters>
#
# from nikola import filters
# FILTERS = {
#    ".html": [filters.typogrify],
#    ".js": [filters.closure_compiler],
#    ".jpg": ["jpegoptim --strip-all -m75 -v %s"],
# }

# Executable for the "yui_compressor" filter (defaults to 'yui-compressor').
# YUI_COMPRESSOR_EXECUTABLE = 'yui-compressor'

# Executable for the "closure_compiler" filter (defaults to 'closure-compiler').
# CLOSURE_COMPILER_EXECUTABLE = 'closure-compiler'

# Executable for the "optipng" filter (defaults to 'optipng').
# OPTIPNG_EXECUTABLE = 'optipng'

# Executable for the "jpegoptim" filter (defaults to 'jpegoptim').
# JPEGOPTIM_EXECUTABLE = 'jpegoptim'

# Executable for the "html_tidy_withconfig", "html_tidy_nowrap",
# "html_tidy_wrap", "html_tidy_wrap_attr" and "html_tidy_mini" filters
# (defaults to 'tidy5').
# HTML_TIDY_EXECUTABLE = 'tidy5'

# List of XPath expressions which should be used for finding headers
# ({hx} is replaced by headers h1 through h6).
# You must change this if you use a custom theme that does not use
# "e-content entry-content" as a class for post and page contents.
# HEADER_PERMALINKS_XPATH_LIST = ['*//div[@class="e-content entry-content"]//{hx}']
# Include *every* header (not recommended):
# HEADER_PERMALINKS_XPATH_LIST = ['*//{hx}']

# File blacklist for header permalinks. Contains output path
# (eg. 'output/index.html')
# HEADER_PERMALINKS_FILE_BLACKLIST = []

# Expert setting! Create a gzipped copy of each generated file. Cheap server-
# side optimization for very high traffic sites or low memory servers.
# GZIP_FILES = False
# File extensions that will be compressed
# GZIP_EXTENSIONS = ('.txt', '.htm', '.html', '.css', '.js', '.json', '.atom', '.xml')
# Use an external gzip command? None means no.
# Example: GZIP_COMMAND = "pigz -k {filename}"
# GZIP_COMMAND = None
# Make sure the server does not return a "Accept-Ranges: bytes" header for
# files compressed by this option! OR make sure that a ranged request does not
# return partial content of another representation for these resources. Do not
# use this feature if you do not understand what this means.

# Compiler to process LESS files.
# LESS_COMPILER = 'lessc'

# A list of options to pass to the LESS compiler.
# Final command is: LESS_COMPILER LESS_OPTIONS file.less
# LESS_OPTIONS = []

# Compiler to process Sass files.
# SASS_COMPILER = 'sass'

# A list of options to pass to the Sass compiler.
# Final command is: SASS_COMPILER SASS_OPTIONS file.s(a|c)ss
# SASS_OPTIONS = []

# #############################################################################
# Image Gallery Options
# #############################################################################

# One or more folders containing galleries. The format is a dictionary of
# {"source": "relative_destination"}, where galleries are looked for in
# "source/" and the results will be located in
# "OUTPUT_PATH/relative_destination/gallery_name"
# Default is:
# GALLERY_FOLDERS = {"galleries": "galleries"}
# More gallery options:
# THUMBNAIL_SIZE = 180
# MAX_IMAGE_SIZE = 1280
# USE_FILENAME_AS_TITLE = True
# EXTRA_IMAGE_EXTENSIONS = []
#
# If set to False, it will sort by filename instead. Defaults to True
# GALLERY_SORT_BY_DATE = True

# If set to True, EXIF data will be copied when an image is thumbnailed or
# resized. (See also EXIF_WHITELIST)
# PRESERVE_EXIF_DATA = False

# If you have enabled PRESERVE_EXIF_DATA, this option lets you choose EXIF
# fields you want to keep in images. (See also PRESERVE_EXIF_DATA)
#
# For a full list of field names, please see here:
# http://www.cipa.jp/std/documents/e/DC-008-2012_E.pdf
#
# This is a dictionary of lists. Each key in the dictionary is the
# name of a IDF, and each list item is a field you want to preserve.
# If you have a IDF with only a '*' item, *EVERY* item in it will be
# preserved. If you don't want to preserve anything in a IDF, remove it
# from the setting. By default, no EXIF information is kept.
# Setting the whitelist to anything other than {} implies
# PRESERVE_EXIF_DATA is set to True
# To preserve ALL EXIF data, set EXIF_WHITELIST to {"*": "*"}

# EXIF_WHITELIST = {}

# Some examples of EXIF_WHITELIST settings:

# Basic image information:
# EXIF_WHITELIST['0th'] = [
#    "Orientation",
#    "XResolution",
#    "YResolution",
# ]

# If you want to keep GPS data in the images:
# EXIF_WHITELIST['GPS'] = ["*"]

# Embedded thumbnail information:
# EXIF_WHITELIST['1st'] = ["*"]

# Folders containing images to be used in normal posts or pages.
# IMAGE_FOLDERS is a dictionary of the form {"source": "destination"},
# where "source" is the folder containing the images to be published, and
# "destination" is the folder under OUTPUT_PATH containing the images copied
# to the site. Thumbnail images will be created there as well.

# To reference the images in your posts, include a leading slash in the path.
# For example, if IMAGE_FOLDERS = {'images': 'images'}, write
#
#   .. image:: /images/tesla.jpg
#
# See the Nikola Handbook for details (in the “Embedding Images” and
# “Thumbnails” sections)

# Images will be scaled down according to IMAGE_THUMBNAIL_SIZE and MAX_IMAGE_SIZE
# options, but will have to be referenced manually to be visible on the site
# (the thumbnail has ``.thumbnail`` added before the file extension by default,
# but a different naming template can be configured with IMAGE_THUMBNAIL_FORMAT).

IMAGE_FOLDERS = {'images': 'images'}
# IMAGE_THUMBNAIL_SIZE = 400
# IMAGE_THUMBNAIL_FORMAT = '{name}.thumbnail{ext}'

# #############################################################################
# HTML fragments and diverse things that are used by the templates
# #############################################################################

# Data about post-per-page indexes.
# INDEXES_PAGES defaults to ' old posts, page %d' or ' page %d' (translated),
# depending on the value of INDEXES_PAGES_MAIN.
#
# (translatable) If the following is empty, defaults to BLOG_TITLE:
# INDEXES_TITLE = ""
#
# (translatable) If the following is empty, defaults to ' [old posts,] page %d' (see above):
# INDEXES_PAGES = ""
#
# If the following is True, INDEXES_PAGES is also displayed on the main (the
# newest) index page (index.html):
#tbm?
INDEXES_PAGES_MAIN = False
#
# If the following is True, index-1.html has the oldest posts, index-2.html the
# second-oldest posts, etc., and index.html has the newest posts. This ensures
# that all posts on index-x.html will forever stay on that page, now matter how
# many new posts are added.
# If False, index-1.html has the second-newest posts, index-2.html the third-newest,
# and index-n.html the oldest posts. When this is active, old posts can be moved
# to other index pages when new posts are added.
#INDEXES_STATIC = False
#
# (translatable) If PRETTY_URLS is set to True, this setting will be used to create
# prettier URLs for index pages, such as page/2/index.html instead of index-2.html.
# Valid values for this settings are:
#   * False,
#   * a list or tuple, specifying the path to be generated,
#   * a dictionary mapping languages to lists or tuples.
# Every list or tuple must consist of strings which are used to combine the path;
# for example:
#     ['page', '{number}', '{index_file}']
# The replacements
#     {number}     --> (logical) page number;
#     {old_number} --> the page number inserted into index-n.html before (zero for
#                      the main page);
#     {index_file} --> value of option INDEX_FILE
# are made.
# Note that in case INDEXES_PAGES_MAIN is set to True, a redirection will be created
# for the full URL with the page number of the main page to the normal (shorter) main
# page URL.
INDEXES_PRETTY_PAGE_URL = ['page', '{number}', '{index_file}']

# If the following is true, a page range navigation will be inserted to indices.
# Please note that this will undo the effect of INDEXES_STATIC, as all index pages
# must be recreated whenever the number of pages changes.
# SHOW_INDEX_PAGE_NAVIGATION = False

# If the following is True, a meta name="generator" tag is added to pages. The
# generator tag is used to specify the software used to generate the page
# (it promotes Nikola).
# META_GENERATOR_TAG = True

# Color scheme to be used for code blocks. If your theme provides
# "assets/css/code.css" this is ignored. Leave empty to disable.
# Can be any of:
# algol, algol_nu, autumn, borland, bw, colorful, default, emacs, friendly,
# fruity, igor, lovelace, manni, monokai, murphy, native, paraiso-dark,
# paraiso-light, pastie, perldoc, rrt, tango, trac, vim, vs, xcode
# This list MAY be incomplete since pygments adds styles every now and then.
# Check with list(pygments.styles.get_all_styles()) in an interpreter.
# CODE_COLOR_SCHEME = 'default'

# FAVICONS contains (name, file, size) tuples.
# Used to create favicon link like this:
# <link rel="name" href="file" sizes="size"/>
# FAVICONS = (
#     ("icon", "/favicon.ico", "16x16"),
#     ("icon", "/icon_128x128.png", "128x128"),
# )

# Show teasers (instead of full posts) in indexes? Defaults to False.
# INDEX_TEASERS = False

# HTML fragments with the Read more... links.
# The following tags exist and are replaced for you:
# {link}                        A link to the full post page.
# {read_more}                   The string “Read more” in the current language.
# {reading_time}                An estimate of how long it will take to read the post.
# {remaining_reading_time}      An estimate of how long it will take to read the post, sans the teaser.
# {min_remaining_read}          The string “{remaining_reading_time} min remaining to read” in the current language.
# {paragraph_count}             The amount of paragraphs in the post.
# {remaining_paragraph_count}   The amount of paragraphs in the post, sans the teaser.
# {post_title}                  The title of the post.
# {{                            A literal { (U+007B LEFT CURLY BRACKET)
# }}                            A literal } (U+007D RIGHT CURLY BRACKET)

# 'Read more...' for the index page, if INDEX_TEASERS is True (translatable)
INDEX_READ_MORE_LINK = '<p class="more"><a href="{link}">{read_more}…</a></p>'
# 'Read more...' for the feeds, if FEED_TEASERS is True (translatable)
FEED_READ_MORE_LINK = '<p><a href="{link}">{read_more}…</a> ({min_remaining_read})</p>'

# Append a URL query to the FEED_READ_MORE_LINK in Atom and RSS feeds. Advanced
# option used for traffic source tracking.
# Minimum example for use with Piwik: "pk_campaign=feed"
# The following tags exist and are replaced for you:
# {feedRelUri}                  A relative link to the feed.
# {feedFormat}                  The name of the syndication format.
# Example using replacement for use with Google Analytics:
# "utm_source={feedRelUri}&utm_medium=nikola_feed&utm_campaign={feedFormat}_feed"
FEED_LINKS_APPEND_QUERY = False

# A HTML fragment describing the license, for the sidebar.
# (translatable)
LICENSE = """<a rel="license" href="https://creativecommons.org/licenses/by-sa/4.0/">Creative Commons Attribution-ShareAlike 4.0 International License</a>"""

# A small copyright notice for the page footer (in HTML).
# (translatable)
CONTENT_FOOTER = """
<div class="footer-line">
  <div id="copyright">&copy; {date} {author}</div>
</div>
<div class="footer-line">
  <div id="license">{license}</div>
</div>
"""

EXTRA_HEAD_DATA = """<script defer src="https://use.fontawesome.com/releases/v5.0.10/js/all.js" integrity="sha384-slN8GvtUJGnv6ca26v8EzVaR9DC58QEwsIk9q1QXdCU8Yu8ck/tL/5szYlBbqmS+" crossorigin="anonymous"></script>"""

CONTENT_FOOTER_FORMATS = {
    DEFAULT_LANG: (
        (),
        {
            "email": BLOG_EMAIL,
            "author": BLOG_AUTHOR,
            "date": time.gmtime().tm_year,
            "license": LICENSE,
        }
    )
}

# Things that will be passed to CONTENT_FOOTER.format().  This is done
# for translatability, as dicts are not formattable.  Nikola will
# intelligently format the setting properly.
# The setting takes a dict. The keys are languages. The values are
# tuples of tuples of positional arguments and dicts of keyword arguments
# to format().  For example, {'en': (('Hello'), {'target': 'World'})}
# results in CONTENT_FOOTER['en'].format('Hello', target='World').
# If you need to use the literal braces '{' and '}' in your footer text, use
# '{{' and '}}' to escape them (str.format is used)
# WARNING: If you do not use multiple languages with CONTENT_FOOTER, this
#          still needs to be a dict of this format.  (it can be empty if you
#          do not need formatting)
# (translatable)

# A simple copyright tag for inclusion in RSS feeds that works just
# like CONTENT_FOOTER and CONTENT_FOOTER_FORMATS
RSS_COPYRIGHT = 'Contents © {date} <a href="mailto:{email}">{author}</a> {license}'
RSS_COPYRIGHT_PLAIN = 'Contents © {date} {author} {license}'
RSS_COPYRIGHT_FORMATS = CONTENT_FOOTER_FORMATS

# To use comments, you can choose between different third party comment
# systems.  The following comment systems are supported by Nikola:
#   disqus, facebook, googleplus, intensedebate, isso, livefyre, muut
# You can leave this option blank to disable comments.
COMMENT_SYSTEM = ""
# And you also need to add your COMMENT_SYSTEM_ID which
# depends on what comment system you use. The default is
# "nikolademo" which is a test account for Disqus. More information
# is in the manual.
COMMENT_SYSTEM_ID = ""

# Create index.html for page folders?
# WARNING: if a page would conflict with the index file (usually
#          caused by setting slug to `index`), the PAGE_INDEX
#          will not be generated for that directory.
# Enable comments on pages (i.e. not posts)?
# COMMENTS_IN_PAGES = False
# Enable comments on picture gallery pages?
# COMMENTS_IN_GALLERIES = False

# What file should be used for directory indexes?
# Defaults to index.html
# Common other alternatives: default.html for IIS, index.php
INDEX_FILE = "index.html"

# If a link ends in /index.html,  drop the index.html part.
# http://mysite/foo/bar/index.html => http://mysite/foo/bar/
# (Uses the INDEX_FILE setting, so if that is, say, default.html,
# it will instead /foo/default.html => /foo)
# (Note: This was briefly STRIP_INDEX_HTML in v 5.4.3 and 5.4.4)
STRIP_INDEXES = True

# List of files relative to the server root (!) that will be asked to be excluded
# from indexing and other robotic spidering. * is supported. Will only be effective
# if SITE_URL points to server root. The list is used to exclude resources from
# /robots.txt and /sitemap.xml, and to inform search engines about /sitemapindex.xml.
# ROBOTS_EXCLUSIONS = ["/archive.html", "/category/*.html"]

# Instead of putting files in <slug>.html, put them in <slug>/index.html.
# No web server configuration is required. Also enables STRIP_INDEXES.
# This can be disabled on a per-page/post basis by adding
#    .. pretty_url: False
# to the metadata.
PRETTY_URLS = True

# If True, publish future dated posts right away instead of scheduling them.
# Defaults to False.
# FUTURE_IS_NOW = False

# If True, future dated posts are allowed in deployed output
# Only the individual posts are published/deployed; not in indexes/sitemap
# Generally, you want FUTURE_IS_NOW and DEPLOY_FUTURE to be the same value.
# DEPLOY_FUTURE = False
# If False, draft posts will not be deployed
# DEPLOY_DRAFTS = True

# Allows scheduling of posts using the rule specified here (new_post -s)
# Specify an iCal Recurrence Rule: http://www.kanzaki.com/docs/ical/rrule.html
# SCHEDULE_RULE = ''
# If True, use the scheduling rule to all posts by default
# SCHEDULE_ALL = False

# Do you want a add a Mathjax config file?
# MATHJAX_CONFIG = ""

# If you want support for the $.$ syntax (which may conflict with running
# text!), just use this config:
# MATHJAX_CONFIG = """
# <script type="text/x-mathjax-config">
# MathJax.Hub.Config({
#     tex2jax: {
#         inlineMath: [ ['$','$'], ["\\\(","\\\)"] ],
#         displayMath: [ ['$$','$$'], ["\\\[","\\\]"] ],
#         processEscapes: true
#     },
#     displayAlign: 'center', // Change this to 'left' if you want left-aligned equations.
#     "HTML-CSS": {
#         styles: {'.MathJax_Display': {"margin": 0}}
#     }
# });
# </script>
# """

# Want to use KaTeX instead of MathJax? While KaTeX may not support every
# feature yet, it's faster and the output looks better.
# USE_KATEX = False

# KaTeX auto-render settings. If you want support for the $.$ syntax (wihch may
# conflict with running text!), just use this config:
# KATEX_AUTO_RENDER = """
# delimiters: [
#     {left: "$$", right: "$$", display: true},
#     {left: "\\\[", right: "\\\]", display: true},
#     {left: "$", right: "$", display: false},
#     {left: "\\\(", right: "\\\)", display: false}
# ]
# """

# Do you want to customize the nbconversion of your IPython notebook?
# IPYNB_CONFIG = {}
# With the following example configuration you can use a custom jinja template
# called `toggle.tpl` which has to be located in your site/blog main folder:
# IPYNB_CONFIG = {'Exporter':{'template_file': 'toggle'}}

# What Markdown extensions to enable?
# You will also get gist, nikola and podcast because those are
# done in the code, hope you don't mind ;-)
# Note: most Nikola-specific extensions are done via the Nikola plugin system,
#       with the MarkdownExtension class and should not be added here.
# The default is ['fenced_code', 'codehilite']
MARKDOWN_EXTENSIONS = ['markdown.extensions.fenced_code', 'markdown.extensions.codehilite', 'markdown.extensions.extra']

# Extra options to pass to the pandoc command.
# by default, it's empty, is a list of strings, for example
# ['-F', 'pandoc-citeproc', '--bibliography=/Users/foo/references.bib']
# Pandoc does not demote headers by default.  To enable this, you can use, for example
# ['--base-header-level=2']
# PANDOC_OPTIONS = []

# Social buttons. This is sample code for AddThis (which was the default for a
# long time). Insert anything you want here, or even make it empty (which is
# the default right now)
# (translatable)
# Show link to source for the posts?
# Formerly known as HIDE_SOURCELINK (inverse)
# SHOW_SOURCELINK = True
# Copy the source files for your pages?
# Setting it to False implies SHOW_SOURCELINK = False
COPY_SOURCES = False

# Modify the number of Post per Index Page
# Defaults to 10
# INDEX_DISPLAY_POST_COUNT = 10

# By default, Nikola generates RSS files for the website and for tags, and
# links to it.  Set this to False to disable everything RSS-related.
# GENERATE_RSS = True

# By default, Nikola does not generates Atom files for indexes and links to
# them. Generate Atom for tags by setting TAG_PAGES_ARE_INDEXES to True.
# Atom feeds are built based on INDEX_DISPLAY_POST_COUNT and not FEED_LENGTH
# Switch between plain-text summaries and full HTML content using the
# FEED_TEASER option. FEED_LINKS_APPEND_QUERY is also respected. Atom feeds
# are generated even for old indexes and have pagination link relations
# between each other. Old Atom feeds with no changes are marked as archived.
# GENERATE_ATOM = False

# Only include teasers in Atom and RSS feeds. Disabling include the full
# content. Defaults to True.
# FEED_TEASERS = True

# Strip HTML from Atom and RSS feed summaries and content. Defaults to False.
# FEED_PLAIN = False

# Number of posts in Atom and RSS feeds.
# FEED_LENGTH = 10

# RSS_LINK is a HTML fragment to link the RSS or Atom feeds. If set to None,
# the base.tmpl will use the feed Nikola generates. However, you may want to
# change it for a FeedBurner feed or something else.
# RSS_LINK = None

# A search form to search this site, for the sidebar. You can use a Google
# custom search (https://www.google.com/cse/)
# Or a DuckDuckGo search: https://duckduckgo.com/search_box.html
# Default is no search form.
# (translatable)
# SEARCH_FORM = ""
#
# This search form works for any site and looks good in the "site" theme where
# it appears on the navigation bar:
#
# SEARCH_FORM = """
# <!-- DuckDuckGo custom search -->
# <form method="get" id="search" action="https://duckduckgo.com/"
#  class="navbar-form pull-left">
# <input type="hidden" name="sites" value="%s">
# <input type="hidden" name="k8" value="#444444">
# <input type="hidden" name="k9" value="#D51920">
# <input type="hidden" name="kt" value="h">
# <input type="text" name="q" maxlength="255"
#  placeholder="Search&hellip;" class="span2" style="margin-top: 4px;">
# <input type="submit" value="DuckDuckGo Search" style="visibility: hidden;">
# </form>
# <!-- End of custom search -->
# """ % SITE_URL
#
# If you prefer a Google search form, here's an example that should just work:
# SEARCH_FORM = """
# <!-- Google custom search -->
# <form method="get" action="https://www.google.com/search" class="navbar-form navbar-right" role="search">
# <div class="form-group">
# <input type="text" name="q" class="form-control" placeholder="Search">
# </div>
# <button type="submit" class="btn btn-primary">
# 	<span class="glyphicon glyphicon-search"></span>
# </button>
# <input type="hidden" name="sitesearch" value="%s">
# </form>
# <!-- End of custom search -->
# """ % SITE_URL

# Use content distribution networks for jQuery, twitter-bootstrap css and js,
# and html5shiv (for older versions of Internet Explorer)
# If this is True, jQuery and html5shiv are served from the Google CDN and
# Bootstrap is served from BootstrapCDN (provided by MaxCDN)
# Set this to False if you want to host your site without requiring access to
# external resources.
# USE_CDN = False

# Check for USE_CDN compatibility.
# If you are using custom themes, have configured the CSS properly and are
# receiving warnings about incompatibility but believe they are incorrect, you
# can set this to False.
# USE_CDN_WARNING = True

# Extra things you want in the pages HEAD tag. This will be added right
# before </head>
# (translatable)
# EXTRA_HEAD_DATA = ""
# Google Analytics or whatever else you use. Added to the bottom of <body>
# in the default template (base.tmpl).
# (translatable)
BODY_END = """<script data-goatcounter="https://tbm.goatcounter.com/count" async src="//gc.zgo.at/count.js"></script>
<!-- Global site tag (gtag.js) - Google Analytics -->
<script async src="https://www.googletagmanager.com/gtag/js?id=UA-170088592-1"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());

  gtag('config', 'UA-170088592-1');
</script>
"""

# The possibility to extract metadata from the filename by using a
# regular expression.
# To make it work you need to name parts of your regular expression.
# The following names will be used to extract metadata:
# - title
# - slug
# - date
# - tags
# - link
# - description
#
# An example re is the following:
# '.*\/(?P<date>\d{4}-\d{2}-\d{2})-(?P<slug>.*)-(?P<title>.*)\.rst'
# (Note the '.*\/' in the beginning -- matches source paths relative to conf.py)
# FILE_METADATA_REGEXP = None

# If enabled, extract metadata from docinfo fields in reST documents
# USE_REST_DOCINFO_METADATA = False

# If enabled, hide docinfo fields in reST document output
# HIDE_REST_DOCINFO = False

# Map metadata from other formats to Nikola names.
# Supported formats: yaml, toml, rest_docinfo, markdown_metadata
# METADATA_MAPPING = {}
#
# Example for Pelican compatibility:
# METADATA_MAPPING = {
#     "rest_docinfo": {"summary": "description", "modified": "updated"},
#     "markdown_metadata": {"summary": "description", "modified": "updated"}
# }
# Other examples: https://getnikola.com/handbook.html#mapping-metadata-from-other-formats

# If you hate "Filenames with Capital Letters and Spaces.md", you should
# set this to true.
FILE_METADATA_UNSLUGIFY_TITLES = True

# Additional metadata that is added to a post when creating a new_post
# ADDITIONAL_METADATA = {}

# Nikola supports Twitter Card summaries, but they are disabled by default.
# They make it possible for you to attach media to Tweets that link
# to your content.
#
# IMPORTANT:
# Please note, that you need to opt-in for using Twitter Cards!
# To do this please visit https://cards-dev.twitter.com/validator
#
# Uncomment and modify to following lines to match your accounts.
# Images displayed come from the `previewimage` meta tag.
# You can specify the card type by using the `card` parameter in TWITTER_CARD.
# TWITTER_CARD = {
#     # 'use_twitter_cards': True,  # enable Twitter Cards
#     # 'card': 'summary',          # Card type, you can also use 'summary_large_image',
#                                   # see https://dev.twitter.com/cards/types
#     # 'site': '@website',         # twitter nick for the website
#     # 'creator': '@username',     # Username for the content creator / author.
# }

# If webassets is installed, bundle JS and CSS into single files to make
# site loading faster in a HTTP/1.1 environment but is not recommended for
# HTTP/2.0 when caching is used. Defaults to True.
# USE_BUNDLES = True

# Plugins you don't want to use. Be careful :-)
# DISABLED_PLUGINS = ["render_galleries"]

# Special settings to disable only parts of the indexes plugin (to allow RSS
# but no blog indexes, or to allow blog indexes and Atom but no site-wide RSS).
# Use with care.
# DISABLE_INDEXES_PLUGIN_INDEX_AND_ATOM_FEED = False
# DISABLE_INDEXES_PLUGIN_RSS_FEED = False

# Add the absolute paths to directories containing plugins to use them.
# For example, the `plugins` directory of your clone of the Nikola plugins
# repository.
EXTRA_PLUGINS_DIRS = ["plugins"]

PRETTY_BREADCRUMBS_TAG = "nav"

# Add the absolute paths to directories containing themes to use them.
# For example, the `v7` directory of your clone of the Nikola themes
# repository.
# EXTRA_THEMES_DIRS = []

# List of regular expressions, links matching them will always be considered
# valid by "nikola check -l"
# LINK_CHECK_WHITELIST = []

# If set to True, enable optional hyphenation in your posts (requires pyphen)
# Enabling hyphenation has been shown to break math support in some cases,
# use with caution.
# HYPHENATE = False

# The <hN> tags in HTML generated by certain compilers (reST/Markdown)
# will be demoted by that much (1 → h1 will become h2 and so on)
# This was a hidden feature of the Markdown and reST compilers in the
# past.  Useful especially if your post titles are in <h1> tags too, for
# example.
# (defaults to 1.)
DEMOTE_HEADERS = 0

# Docutils, by default, will perform a transform in your documents
# extracting unique titles at the top of your document and turning
# them into metadata. This surprises a lot of people, and setting
# this option to True will prevent it.
# NO_DOCUTILS_TITLE_TRANSFORM = False

# If you don’t like slugified file names ([a-z0-9] and a literal dash),
# and would prefer to use all the characters your file system allows.
# USE WITH CARE!  This is also not guaranteed to be perfect, and may
# sometimes crash Nikola, your web server, or eat your cat.
# USE_SLUGIFY = True

# Templates will use those filters, along with the defaults.
# Consult your engine's documentation on filters if you need help defining
# those.
# TEMPLATE_FILTERS = {}

# Put in global_context things you want available on all your templates.
# It can be anything, data, functions, modules, etc.
GLOBAL_CONTEXT = {}

# Add functions here and they will be called with template
# GLOBAL_CONTEXT as parameter when the template is about to be
# rendered
GLOBAL_CONTEXT_FILLER = []
