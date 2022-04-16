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

def create_customer(customer):
   
    max_id = CUSTOMERS[-1]["id"]

    new_id = max_id + 1
    customer["id"] = new_id

    CUSTOMERS.append(customer)

    return customer

