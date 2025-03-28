#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'The Idris Community'
SITENAME = u'Idris'
SITEURL = 'http://localhost:8000'
SITELOGO = 'images/logo-small.png'
THEME = 'notmyidea-cms'

PATH = 'content'
STATIC_PATHS =['images','releases']

TIMEZONE = 'UTC'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = ()
#('Idris', 'https://idris-lang.github.io/'),
#         ('CS at St Andrews', 'https://www.cs.st-andrews.ac.uk/'),)

# Social widget
SOCIAL = (('Bluesky', 'https://bsky.app/profile/idris-lang.org'),
          ('GitHub', 'https://www.github.com/idris-lang'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
