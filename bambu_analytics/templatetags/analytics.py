from django.template import Library
from logging import getLogger

register = Library()
LOGGER = getLogger('bambu_analytics')

@register.simple_tag(takes_context = True)
def tracking(context):
	request = context.get('request')
	if not request:
		return u'<script>console.error(\'Current request object not found in Django template context\');</script>'

	if getattr(request, '_analytics_handler', None):
		try:
			return request._analytics_handler.render(request)
		except Exception, ex:
			LOGGER.warn('Error rendering analytics code', exc_info = True)

	return u''
