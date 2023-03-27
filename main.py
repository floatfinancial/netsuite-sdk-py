import os

from netsuitesdk import NetSuiteConnection


def connect_tba():
    return NetSuiteConnection(
        account=os.getenv('NS_ACCOUNT'),
        consumer_key=os.getenv('NS_CONSUMER_KEY'),
        consumer_secret=os.getenv('NS_CONSUMER_SECRET'),
        token_key=os.getenv('NS_TOKEN_KEY'),
        token_secret=os.getenv('NS_TOKEN_SECRET'),
        # Setting this to `False` populates subLists.
        # https://docs.oracle.com/en/cloud/saas/netsuite/ns-online-help/section_4170181850.html
        # search_body_fields_only=False
    )


def main():
    """
    GarfCool.png (externalId 1000) is in Float Receipts Folder (externalId="9999").
    """
    nc = connect_tba()

    # Attaching files to journal entries via the API is not supported.
    # attachTo = {"internalId": "4607", "type": "journalEntry"},

    attach_basic_ref = nc.client.AttachBasicReference(
        attachTo=nc.client.RecordRef(**{"internalId": "5312", "type": "vendorBill"},),
        attachedRecord=nc.client.RecordRef(**{"externalId": "1000", "type": "file", "name": "GarfCool.png"})
    )

    response = nc.client.request("attach", attach_basic_ref)
    print(response)

    stop = 2


if __name__ == "__main__":
    main()
