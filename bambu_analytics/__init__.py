__version__ = '2.0'

from django.utils.importlib import import_module
from bambu_analytics import settings
from logging import getLogger

LOGGER = getLogger('bambu_analytics')

def _init_tracker(request):
	"""
	Setup tracking on a request
	"""
	if not getattr(request, '_analytics_handler', None):
		module, dot, klass = settings.PROVIDER.rpartition('.')
		module = import_module(module)
		ps = settings.get(klass)

		klass = getattr(module, klass)
		request._analytics_handler = klass(**ps)

def add_events_from_redirect(request):
	"""
	Add trakcing events from a previous request on the same session
	to the current event queue for this request
	"""
	events = request.session.get('bambu_analytics.events', [])

	if any(events):
		_init_tracker(request)
		request._analytics_handler.events.extend(
			[e for e in events]
		)

		del request.session['bambu_analytics.events']
		request.session.modified = True
		return True

	return False

def track_event(request, event, **kwargs):
	"""
    Let's say you have a contact form. In the view that receives the form
    data, you want to track the successful submission of form data and then
    redirect the user to a page thanking them for getting in touch.
    
    >>> from bambu_analytics import track_event, events
    >>> def enquiry_form(request):
    >>>     track_event(request, events.EVENT,
    >>>     category = u'Enquiry',
    >>>     action = u'Submit'
    >>> )
    
    Here, ``events.EVENT`` is a constant meaning 'a standard event'.

    If you're using a client-side analytics library (like Google Analytics),
    you should only track events in this way if you're going to redirect the
    user back to a page that will load and render the ``tracking`` template
    tag. Otherwise the event will be stored in the user's session cookie,
    but won't be tracked by your provider.
	"""
	_init_tracker(request)

	try:
		request._analytics_handler.track(event, **kwargs)
	except Exception, ex:
		LOGGER.error('Error tracking analytics event', exc_info = True,
			extra = {
				'data': {
					'event': event,
					'args': kwargs
				}
			}
		)
