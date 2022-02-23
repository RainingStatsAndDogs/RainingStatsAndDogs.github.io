AUTHOR = 'PB'
SITENAME = "It's Raining Stats and Dogs"
SITEURL = ''

PATH = 'content'

TIMEZONE = 'US/Pacific'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'https://getpelican.com/'),
         ('Python.org', 'https://www.python.org/'),
         ('R', 'https://www.cran.org/'),
         ('Julia', 'https://julialang.org/'),
         ('Jinja2', 'https://palletsprojects.com/p/jinja/'),
         ('scikit-learn', 'https://scikit-learn.org/stable/'),
         ('statsmodels', 'https://www.statsmodels.org/stable/index.html'),
         ('pymc', 'https://docs.pymc.io/en/v3/'),
         ('numpyro', 'https://num.pyro.ai/en/latest/index.html#'),
         ('Stan', 'https://mc-stan.org/'),
         ('tidyverse', 'https://www.tidyverse.org/'),)

# Social widget
SOCIAL = (('Github', 'https://github.com/RainingStatsAndDogs'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

MARKUP = ("md", "ipynb")

from pelican_jupyter import markup as nb_markup
PLUGINS = [nb_markup]

IGNORE_FILES = [".ipynb_checkpoints"]