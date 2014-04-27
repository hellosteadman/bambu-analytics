"""
There are four types of trackable event within Bambu Analytics, but not
all of them are setup to work with Google's Universal Analytics just
yet.

The last two haven't been properly hooked up to Google's new system, but
you can use the legacy provider (see below).
"""

PAGE = 'page'
"""A page view (this is handled automatically by middleware)"""

EVENT = 'event'
"""Something of note happening on the site, that you want to measure"""

TRANSACTION = 'transaction'
"""A monetary transaction"""

TRANSACTION_ITEM = 'transaction_item'
"""Part of an order (an item in someone's shopping cart)"""