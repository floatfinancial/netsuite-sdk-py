from .base import ApiBase
import logging

logger = logging.getLogger(__name__)


class CustomSegments(ApiBase):
    def __init__(self, ns_client):
        ApiBase.__init__(self, ns_client=ns_client, type_name='CustomSegment')

    def get_all(self):
        """
        Get all custom segments using search API (getAll not supported for CustomSegment)
        """
        return self._search_all_generator(page_size=100)

    def get_all_generator(self, page_size=20):
        """
        Returns a generator which is more efficient memory-wise
        Uses search API instead of getAll (which is not supported for CustomSegment)
        """
        return self.create_paginated_search(page_size=page_size)
