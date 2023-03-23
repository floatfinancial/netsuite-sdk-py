from collections import OrderedDict

from .base import ApiBase
import logging

logger = logging.getLogger(__name__)


class Files(ApiBase):
    """
    Please note that `department` and `class` come back in File responses as the `name` value of the
    Department or Class of the File's Folder, if restricted by Department or Class.
    """
    def __init__(self, ns_client):
        ApiBase.__init__(self, ns_client=ns_client, type_name='File')

    def post(self, data) -> OrderedDict:
        """
        There are other items that could/should be added in here:
        Based on: https://system.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2019_1/schema/record/file.html
        """
        assert data['externalId'], 'missing external id'
        file = self.ns_client.File()

        # TODO Validation for extension in `name`
        if 'name' in data:
            file['name'] = data['name']

        if 'folder' in data:
            file['folder'] = self.ns_client.RecordRef(**(data['folder']))

        if 'externalId' in data:
            file['externalId'] = data['externalId']

        if 'content' in data:
            file['content'] = data['content']

        # This field is read-only
        # if 'mediaTypeName' in data:
        #     file['mediaTypeName'] = data['mediaTypeName']

        if 'fileType' in data:
            file['fileType'] = data['fileType']

        if 'encoding' in data:
            file['encoding'] = data['encoding']

        if 'isInactive' in data:
            file['isInactive'] = data['isInactive']

        if 'isPrivate' in data:
            file['isPrivate'] = data['isPrivate']

        if 'isOnline' in data:
            file['isOnline'] = data['isOnline']

        if 'textFileEncoding' in data:
            file['textFileEncoding'] = data['textFileEncoding']

        if 'description' in data:
            file['description'] = data['description']

        logger.debug('able to create file = %s', file)
        res = self.ns_client.upsert(file)
        return self._serialize(res)
