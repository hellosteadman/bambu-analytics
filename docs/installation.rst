Installation
============

Install the package via Pip:

::

    pip install bambu-analytics

Add it to your ``INSTALLED_APPS`` list:

::

    INSTALLED_APPS = (
        ...
        'bambu_analytics'
    )

Next, install the tracking middleware:

::

    MIDDLEWARE_CLASSES = (
        ...
        'bambu_analytics.middleware.AnalyticsMiddleware',
        ...
    )

Also, make sure 'django.core.context_processors.request' is listed in your
``TEMPLATE_CONTEXT_PROCESSORS`` settings otherwise Bambu AJAX won't be able to access the current
request object.

Finally, set your Google Analytics ID:

::

    ANALYTICS_SETTINGS = {
        'UniversalAnalyticsProvider': {
            'ID': 'UA-XXXXXXXX-XX'
        }
    }

Or, use the shortcut setting:

::

    GOOGLE_ANALYTICS_IDS = ('UA-XXXXXXXX-XX',)

(This is a legacy setting that will be deprecated in a future release)