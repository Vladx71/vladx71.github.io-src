#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Vladx71'
SITENAME = u'Vladx71 Github Pages'
SITEURL = ''

PLUGIN_PATHS = ['/home/vlad/git/pelican-plugins']
PLUGINS = ['gravatar' , 'sitemap' , 'always_modified' , 'disqus_static' ,'encrypt-content' , 'gallery' , 'pdf' , 'pelican_youtube' , 'pelican_vimeo' , 'pin_to_top' , 'tag_cloud']

PATH = 'content'

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = yes
CATEGORY_FEED_ATOM = yes
TRANSLATION_FEED_ATOM = yes
AUTHOR_FEED_ATOM = yes
AUTHOR_FEED_RSS = yes

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         )

# Social widget
#SOCIAL = (('You can add links in your config file', '#'),
#          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
