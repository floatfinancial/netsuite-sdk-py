import os

from netsuitesdk import NetSuiteConnection
from datetime import datetime


def connect_tba():
    return NetSuiteConnection(
        account=os.getenv('NS_ACCOUNT'),
        consumer_key=os.getenv('NS_CONSUMER_KEY'),
        consumer_secret=os.getenv('NS_CONSUMER_SECRET'),
        token_key=os.getenv('NS_TOKEN_KEY'),
        token_secret=os.getenv('NS_TOKEN_SECRET'),
        # Setting this to False gets everything back (populates sublists)
        # https://docs.oracle.com/en/cloud/saas/netsuite/ns-online-help/section_4170181850.html
        # search_body_fields_only=False
    )


def main():
    nc = connect_tba()
    # customers = nc.customers.get_all_generator()
    # vendor_bills = nc.vendor_bills.get_all_generator()
    # vendor_payment = nc.vendor_payments.get(internalId="5112")

    # create_vendor_bill(nc)
    # create_vendor_payment(nc)

    stop = 2


def create_vendor_bill(nc):
    # https://system.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2022_1/schema/record/vendorbill.html
    return nc.vendor_bills.post({
        "externalId": "130",
        "currency": {
            'name': 'Canadian Dollar',
            'internalId': '1',
        },
        "subsidiary": {
            'internalId': '1',
        },
        "expenseList": [
            {
                "amount": 452,
                "memo": "hi",
                "account": {
                    "internalId": "216",  # office
                },
                "taxCode": {
                    "internalId": "21",  # 13%
                },
                "customer": {  # customer/project
                    "internalId": "535",
                },
                "class": {  # Float Class
                    "internalId": "1",
                },
                "department": {  # Float Department
                    "internalId": "3",
                },
                "location": {  # Float Location
                    "internalId": "1",
                }
            },
            {
                "amount": 123,
                "memo": "hello",
                "account": {
                    "internalId": "216",  # office
                },
                "taxCode": {
                    "internalId": "21",  # 13%
                },
                "customer": {  # customer/project
                    "internalId": "535",
                },
                "class": {  # Float Class
                    "internalId": "1",
                },
                "department": {  # Float Department
                    "internalId": "3",
                },
                "location": {  # Float Location
                    "internalId": "1",
                }
            }
        ],
        "entity": {
            'name': 'Starbucks',
            'internalId': '4',
        },
        "account": {
            'internalId': '111',  # accounts payable
        },
        "memo": f"{datetime.now()}"
    })


def create_vendor_payment(nc):
    # https://system.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2022_1/schema/record/vendorpayment.html
    vendor_bill_payment = nc.vendor_payments.post({
        "externalId": "48777",
        "currency": {
            'name': 'Canadian Dollar',
            'internalId': '1',
        },
        "subsidiary": {
            'internalId': '1',
        },
        "account": {
            'name': 'Float Clearing Account',
            'internalId': '219',
        },
        "entity": {
            'name': 'Starbucks',
            'internalId': '4',
        },
        "location": {
            "internalId": "1",
        },
        "class": {
            "internalId": "1",
        },
        "department": {
            "internalId": "3",
        },
        "memo": "VendorBillPayment memo",
        "total": 649.75,
        # We require applyList to link the vendorBillPayment to the vendorBill
        # https://system.netsuite.com/help/helpcenter/en_US/srbrowser/Browser2022_1/schema/other/vendorpaymentapplylist.html?mode=package
        "applyList": {
            "apply": [
                {
                    "doc": 4807,  # corresponds to VendorBill id
                    "amount": 3.55,
                    "type": "Bill",
                    "currency": "Canadian Dollar"  # What happens if we don't pass this?
                }
            ]
        }
    })


if __name__ == "__main__":
    main()
