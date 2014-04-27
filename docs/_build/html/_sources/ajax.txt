AJAX and client-side tracking
=============================

If you want to track events client-side, or you're running a site that
uses a lot of AJAX (like `Poddle.fm <http://poddle.fm/>`_), you'll get
automatic access to the ``bambu.analytics`` namespace within JavaScript,
and you can call ``track()`` to handle client-side events or AJAX page
updates (ie: via ``window.pushstate``).

Here's an example event used on Poddle.fm when a user clicks the Play
button on an episode of a podcast:

::

    <script>
        $('a.btn-play').on('click',
            function() {
                // Play the audio
                ...

                // Track the click event
                bambu.analytics.track(
                    bambu.analytics.EVENT,
                    {
                        category: 'Audio',
                        action: 'play'
                    }
                );
            }
        );
    </script>
