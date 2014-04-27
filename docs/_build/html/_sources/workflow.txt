The workflow
============

1. The user requests a URL
2. The analytics middleware adds a page-view event to its tracking list
3. The view for that URL is rendered, and the script containing the
   analytics setup code and the tracked event from step 2 is rendered
4. The user submits a form on the page
5. The view for that form calls ``bambu_analytics.track_event``
6. An HTTP redirect is issued
7. The middleware reads the redirect and stores the tracking event in a
   session variable
8. The user's browser is redirected to a 'thank you' page
9. When the 'thank you' page is rendered, the tracking event stored in
   the session variable are read into JavaScript and rendered

All of this sounds complex, but actually means you can track events more
easily and in a pluggable, product-agnostic way. It also provides the
option for server-side analytics events to be tracked.

In Google Analytics, the practical upshot is that it uses events rather
than goals, meaning you don't have to manually define them in your
Analytics property.