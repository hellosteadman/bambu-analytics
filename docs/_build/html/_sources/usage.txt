Usage
=====

By default, all page views will be tracked once you include the
``tracking`` template tag in your base HTML template, like so:

::

    <!DOCTYPE html>
    <html>
        ...
        <body>
            ...
            {% load analytics %}{% tracking %}
        </body>
    </html>

Tracking events are gathered by the middleware, as it allows trackable
events to be defined server-side. For example, when you submit an
enquiry form, you can add an event that will be tracked once the user is
redirected to the 'thank you' page.
