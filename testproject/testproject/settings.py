from os import path

DEBUG = True
TEMPLATE_DEBUG = DEBUG

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'database.db',
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': ''
    }
}

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'bambu_analytics.middleware.AnalyticsMiddleware'
)

TEMPLATE_CONTEXT_PROCESSORS = (
	'django.core.context_processors.debug',
	'django.core.context_processors.request'
)

SITE_ID = 1
INSTALLED_APPS = (
    'django.contrib.sites',
    'bambu_analytics',
    'testproject.myapp'
)

SECRET_KEY = 'sm8apo4(o4ni9n=nsn7-3x8g@fkeuckm(#ixpk5lw3vrzq*ads'
ROOT_URLCONF = 'testproject.urls'

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

SITE_ROOT = path.abspath(path.dirname(__file__) + '/../')
STATIC_ROOT = path.join(SITE_ROOT, 'static')
TEMPLATE_DIRS = (
    path.join(SITE_ROOT, 'templates'),
)

ANALYTICS_SETTINGS = {
    'UniversalAnalyticsProvider': {
        'ID': 'UA-XXXXXXXX-XX'
    }
}