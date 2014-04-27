"""
``ANALYTICS_PROVIDER``
    The fully-qualified module and class name of the analytics provider to use to track events
    (defaults to 'bambu_analytics.providers.google.UniversalAnalyticsProvider')

``ANALYTICS_SETTINGS``
    A dictionary mapping the provider class name (ie: 'UniversalAnalyticsProvider') to a number of
    settings, defined by each provider individually. For example, the Google providers both require
    a setting called ``ID``
"""

from django.conf import settings as s

PROVIDER = getattr(s, 'ANALYTICS_PROVIDER',
    'bambu_analytics.providers.google.UniversalAnalyticsProvider'
)

def get(klass):
    return getattr(s,
        'ANALYTICS_SETTINGS', {
            klass: {}
        }
    ).get(klass, {})
