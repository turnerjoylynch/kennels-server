"""Handles Employee Data"""
EMPLOYEES = [
    {
      "id": 1,
      "name": "Tina Turner",
      "locationId": 2
    },
    {
      "id": 2,
      "name": "Megan Thee Stallion",
      "locationId": 1
    },
    {
      "id": 3,
      "name": "Nicholas Cage",
      "locationId": 3
    }
]

def get_all_employees():
    return EMPLOYEES

def get_single_employee(id):
    requested_employee = None

    for employee in EMPLOYEES:
        if employee["id"] == id:
            requested_employee = employee

    return requested_employee

def create_employee(employee):

    max_id = EMPLOYEES[-1]["id"]

    new_id = max_id + 1
    employee["id"] = new_id

    EMPLOYEES.append(employee)

    return employee

