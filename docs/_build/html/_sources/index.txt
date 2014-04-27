Bambu Analytics
===============

Provides a simple, pluggable system for analytics

About Bambu Analytics
---------------------

Bambu Analytics provides a simple system for implementing analytics
tools like Google Analytics into your Django projects, so you can track
page views, goals and events.

By default it supports Google's `Universal
Analytics <https://support.google.com/analytics/answer/2790010?hl=en-GB>`_
programme, but you interact with the package within JavaScript via the
``bambu.analytics`` namespace. This way, you can change analytics
providers (or write your own) without changing the code within the rest
of your site.

This is massively a work-in-progress.

About Bambu Tools 2.0
---------------------

This is part of a toolset called Bambu Tools. It's being moved from a
namespace of ``bambu`` to its own 'root-level' package, along with all
the other tools in the set. If you're upgrading from a version prior to
2.0, please make sure to update your code to use ``bambu_analytics``
rather than ``bambu.analytics``.

Contents
--------

.. toctree::
   :maxdepth: 1
   
   installation
   usage
   workflow
   tracking
   providers
   ajax
   settings

Todo
----

-  Implement ecommerce into the Universal Analytics provider

Questions or suggestions?
-------------------------

Find me on Twitter (@iamsteadman) or `visit my blog <http://steadman.io/>`_.

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
