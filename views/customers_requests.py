"""Handles Customer Data"""
CUSTOMERS = [
    {
      "id": 1,
      "name": "Sydney Noh",
      "address": "125 NSS Ln",
      "email": "me@trevorguinn.com"
    },
    {
      "id": 2,
      "name": "Trevor Guinn",
      "address": "123 NSS Ln",
      "email": "me@trevorguinn.com"
    },
    {
      "id": 3,
      "name": "Lynn Samuelson",
      "address": "Best Dairy Queen in the World, Starbuck",
      "email": "lynnsamuelson@ls.com"
    },
    {
      "id": 4,
      "name": "Hayley Williams",
      "address": "123 Misery Business Ln",
      "email": "yelyah@williams.com"
    },
]

def get_all_customers():
    return CUSTOMERS

def get_single_customer(id):
    requested_customer = None

    for customer in CUSTOMERS:
        if customer["id"] == id:
            requested_customer = customer

    return requested_customer