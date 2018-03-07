#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Test'
SITENAME = 'Focus on ML & DM'
SITEURL = 'https://1007530194.github.io/pelican-blog'
#  GITHUB_URL = 'https://github.com/liuchengxu'
GOOGLE_ANALYTICS_UNIVERSAL = 'UA-73260325-2'
GOOGLE_ANALYTICS_UNIVERSAL_PROPERTY = 'auto'
#  DISQUS_SITENAME = 'xuliuchengxlc'

TIMEZONE = 'Asia/Shanghai'

PATH = 'content'

STATIC_PATHS = ['images', 'notebooks']
NOTEBOOK_DIR = 'notebooks'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Homepage', 'https://1007530194.github.io/'),)

# Social widget
SOCIAL = (('GitHub', 'https://github.com/liuchengxu'),
          ('Pelican Blog', 'https://github.com/liuchengxu/pelican-blog'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

MARKUP = ('md', 'ipynb')

PLUGIN_PATHS = ['./plugins']  # 如果像原文直接PLUGIN_PATH = `./plugins`而不使用列表会报warning
PLUGINS = ['ipynb.markup']

THEME = "theme/bootstrap3"
