from django.test import TestCase, RequestFactory
from bambu_analytics import track_event, events

class AnalyticsTrackingTestCase(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
    
    def test_track_page(self):
        request = self.factory.get('/')
        track_event(request, events.PAGE)
    
    def test_track_event(self):
        request = self.factory.get('/')
        track_event(request, events.EVENT,
            category = 'test',
            action = 'event'
        )
    
    def test_track_transaction(self):
        request = self.factory.get('/')
        track_event(request, events.TRANSACTION,
            transaction_id = 1,
            store = 'test',
            amount = 1.0,
            tax = 0,
            postage = 0,
            city = 'Birmingham',
            state = 'West Midlands',
            country = 'United Kingdom'
        )

    def test_track_transaction_item(self):
        request = self.factory.get('/')
        track_event(request, events.TRANSACTION_ITEM,
            transaction_id = 1,
            sku = '12345',
            product = 'Test Product',
            category = u'test',
            amount = 1.0,
            quantity = 1
        )