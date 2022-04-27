"""Handles Customer Data"""
import sqlite3
import json
from models import Customer

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
    """ get all """
    # Open a connection to the database
    with sqlite3.connect("./kennel.sqlite3") as conn:

        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT
            a.id,
            a.name,
            a.address,
            a.email
        FROM customer a
        """)

        customers = []
        dataset = db_cursor.fetchall()

        for row in dataset:
            customer = Customer(row['id'], row['name'], row['address'],
                            row['email'])

            customers.append(customer.__dict__)

    return json.dumps(customers)

def get_single_customer(id):
    """ get single """
    with sqlite3.connect("./kennel.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT
            a.id,
            a.name,
            a.address,
            a.email,
        FROM customer a
        WHERE a.id = ?
        """, ( id, ))

        data = db_cursor.fetchone()

        customer = Customer(data['id'], data['name'], data['address'],
                            data['email'])

        return json.dumps(customer.__dict__)

def create_customer(customer):
    """ create """
    max_id = CUSTOMERS[-1]["id"]

    new_id = max_id + 1
    customer["id"] = new_id

    CUSTOMERS.append(customer)

    return customer

def delete_customer(id):
    with sqlite3.connect("./kennel.sqlite3") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        DELETE FROM customer
        WHERE id = ?
        """, (id, ))


def update_customer(id, new_customer):
    """ update """
    for index, customer in enumerate(CUSTOMERS):
        if customer["id"] == id:
            CUSTOMERS[index] = new_customer
            break

def get_customers_by_email(email):
    """ get by """
    with sqlite3.connect("./kennel.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Write the SQL query to get the information you want
        db_cursor.execute("""
        select
            c.id,
            c.name,
            c.address,
            c.email,
            c.password
        from Customer c
        WHERE c.email = ?
        """, ( email, ))

        customers = []
        dataset = db_cursor.fetchall()

        for row in dataset:
            customer = Customer(row['id'], row['name'], row['address'], row['email'],
                                row['password'])
            customers.append(customer.__dict__)

    return json.dumps(customers)
