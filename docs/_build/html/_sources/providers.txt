Providers
=========

Changing analytics provider
---------------------------

Bambu Analytics supports the legacy (ua.js) and new (analytics.js)
scripts as provided by Google. ecommerce is setup to work with the old
style (ua.js), so if you need to track ecommerce events, you should
change the provider via your Django settings file:

::

    ANALYTICS_PROVIDER = 'bambu_analytics.providers.google.GoogleAnalyticsProvider'

Writing your own provider
-------------------------

It's pretty easy to write your own provider. Start by taking a look at
the two classes in ``bambu_analytics.providers.google`` to see how
they're hooked up.

Essentially the job of a provider is to take Python objects that refer
to events and turn them into JavaScript objects and function calls that
your analytics library can understand.

Each provider needs to render a string. For client-side analytics tools
this should contain HTML with a ``<script>`` tag. The first thing inside
that tag should be:

::

    {% include 'analytics/bambu.inc.js' %}

This exposes the ``bambu.analytics`` namespace. After all the code
needed to hook up the analytics tool and track basic events, your
provider should bind to the ``track`` event within ``bambu.analytics``
like this:

::

    bambu.analytics.on('track',
        function(e) {
            // e.event contains the name of the event, which you can compare
            // against the constants in the bambu.analytics namespace (they're)
            // the same as the ones within the Python package.

            // e.args contains a dictionary of arguments that you can use to map
            // the Python-defined keyword args (like 'category' or 'option_value')
            // to arguments that your specific analytics library understands. See
            // the templates/analytics/universal.inc.html file for an idea of
            // how this works.
        }
    );

This way you can write an analytics provider that works on all sites
that use Bambu Analytics. Both of them!

Writing a server-side provider
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

If you want to track your own events or you have a server-side analytics
tool that you want to hook into, you'll write a provider that focuses on
teh back- rather than front-end. You'll still need to render something,
but this can be an empty string, or some sort of tracking pixel if
that's the route you want to go down.