"""Handles Employee Data"""

import sqlite3
import json
from models import Employee

EMPLOYEES = [
    {
        "id": 1,
        "name": "Tina Turner",
        "location_id": 2
    },
    {
        "id": 2,
        "name": "Megan Thee Stallion",
        "location_id": 1
    },
    {
        "id": 3,
        "name": "Nicholas Cage",
        "location_id": 3
    }
]


def get_all_employees():
    """ get all """
    with sqlite3.connect("./kennel.sqlite3") as conn:

        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT
            a.id,
            a.name,
            a.location_id
        FROM employee a
        """)

        employees = []
        dataset = db_cursor.fetchall()

        for row in dataset:
            employee = Employee(row['id'], row['name'], row['location_id'])

            employees.append(employee.__dict__)

    return json.dumps(employees)

def get_single_employee(id):
    """ get single """
    with sqlite3.connect("./kennel.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT
            a.id,
            a.name,
            a.location_id
        FROM employee a
        WHERE a.id = ?
        """, ( id, ))

        data = db_cursor.fetchone()

        employee = Employee(data['id'], data['name'], data['location_id'])

        return json.dumps(employee.__dict__)


def create_employee(employee):
    """ create """
    max_id = EMPLOYEES[-1]["id"]

    new_id = max_id + 1
    employee["id"] = new_id

    EMPLOYEES.append(employee)

    return employee


def delete_employee(id):
    """ delete """
    employee_index = -1

    for index, employee in enumerate(EMPLOYEES):
        if employee["id"] == id:
            employee_index = index

    if employee_index >= 0:
        EMPLOYEES.pop(employee_index)


def update_employee(id, new_employee):
    """ update """
    for index, employee in enumerate(EMPLOYEES):
        if employee["id"] == id:
            EMPLOYEES[index] = new_employee
            break

def get_employees_by_location(location_id):
    """ get by """
    with sqlite3.connect("./kennel.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Write the SQL query to get the information you want
        db_cursor.execute("""
        SELECT
            a.id,
            a.name,
            a.location_id
        WHERE a.location_id = ?
        """, (location_id, ))

        employees = []
        dataset = db_cursor.fetchall()

        for row in dataset:
            employee = Employee(row['id'], row['name'], row['location_id'])
            employees.append(employee.__dict__)

    return json.dumps(employees)
