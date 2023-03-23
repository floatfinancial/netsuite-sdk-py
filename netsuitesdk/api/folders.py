from collections import OrderedDict

from .base import ApiBase
import logging

logger = logging.getLogger(__name__)


class Folders(ApiBase):
    def __init__(self, ns_client):
        ApiBase.__init__(self, ns_client=ns_client, type_name='Folder')

    def post(self, data) -> OrderedDict:
        # Please see: https://system.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2019_1/schema/record/folder.html
        assert data['externalId'], 'missing external id'
        folder = self.ns_client.Folder()

        if 'name' in data:
            folder['name'] = data['name']

        if 'externalId' in data:
            folder['externalId'] = data['externalId']

        if 'description' in data:
            folder['description'] = data['description']

        if 'isInactive' in data:
            folder['isInactive'] = data['isInactive']

        if 'isPrivate' in data:
            folder['isPrivate'] = data['isPrivate']

        if 'isOnline' in data:
            folder['isOnline'] = data['isOnline']

        if 'parent' in data:
            folder['parent'] = self.ns_client.RecordRef(**(data['parent']))

        if 'subsidiary' in data:
            folder['subsidiary'] = self.ns_client.RecordRef(**(data['subsidiary']))

        if 'group' in data:
            folder['group'] = self.ns_client.RecordRef(**(data['group']))

        if 'department' in data:
            folder['department'] = self.ns_client.RecordRef(**(data['department']))

        if 'class' in data:
            folder['class'] = self.ns_client.RecordRef(**(data['class']))

        if 'location' in data:
            folder['location'] = self.ns_client.RecordRef(**(data['location']))

        logger.debug('able to create folder = %s', folder)
        res = self.ns_client.upsert(folder)
        return self._serialize(res)
