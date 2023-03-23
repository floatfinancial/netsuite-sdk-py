import os

from netsuitesdk import NetSuiteConnection

from records import TextFileEncoding, MediaType


def connect_tba():
    return NetSuiteConnection(
        account=os.getenv('NS_ACCOUNT'),
        consumer_key=os.getenv('NS_CONSUMER_KEY'),
        consumer_secret=os.getenv('NS_CONSUMER_SECRET'),
        token_key=os.getenv('NS_TOKEN_KEY'),
        token_secret=os.getenv('NS_TOKEN_SECRET'),
        # Setting this to False populuates sublists
        # https://docs.oracle.com/en/cloud/saas/netsuite/ns-online-help/section_4170181850.html
        # search_body_fields_only=False
    )


def main():
    nc = connect_tba()

    # files = nc.files.get_all()
    # file = nc.files.get(internalId="111")

    # folders = nc.folders.get_all()
    # folder = nc.folders.get(externalId="9999")

    def on_connection():
        """
        For implementation, we could do something like the below on NetSuite connection.
        On connection, check if there is a "Float Receipts" folder, if there isn't, create it.
        """
        search = nc.folders.search(attribute="name", value="Float Receipts", operator="is")
        if search is None:
            post_folder(nc)

    # _ = post_folder(nc)
    # _ = post_file(nc)

    stop = 2


def post_file(nc):
    filename = "garfcool.png"

    with open(filename, "rb") as f:
        encoded_string = f.read()

    return nc.files.post({
        # Name must include extension
        "name": filename,
        "description": 'Man, that cat is cool!',
        # It isn't possible to create a new NS FC Folder from within a File POST
        "folder": {
            "externalId": "9999",  # 9999 - Float Receipts FC Folder
            # "internalId": "-4",  # Negative internalIds represent default File Cabinet Folders
        },
        "externalId": "1000",
        "content": encoded_string,
        "fileType": MediaType.PNG.value,
        "textFileEncoding": TextFileEncoding.UTF8.value,
        "isPrivate": True,
        "isOnline": False,  # This defaults to True is not provided - Bonkers
        "isInactive": False,
    })


def post_folder(nc):
    return nc.folders.post({
        "name": "Float Receipts",
        "externalId": "9999",
        "description": "NetSweet File Cabinet Folder to house many images of Garfield.",
        "isPrivate": True,
        "isOnline": False,
        "isInactive": False,
    })


if __name__ == "__main__":
    main()
