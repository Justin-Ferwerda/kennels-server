EMPLOYEES = [
        {
            "id": 1,
            "name": "Justin Ferwerda",
        },
        {
            "id": 2,
            "name": "Natalie Ferwerda",
        }
    ]

def get_all_employees():
    """get all employees"""
    return EMPLOYEES

def get_single_employee(id):
    """get single employee"""
    requested_employee = None

    for employee in EMPLOYEES:
        if employee['id'] == id:
            requested_employee = employee

    return requested_employee

def create_employee(employee):
    """creates animal from dict repr sent by client"""
    # Get the id value of the last animal in the list
    max_id = EMPLOYEES[-1]["id"]

    # Add 1 to whatever that number is
    new_id = max_id + 1

    # Add an `id` property to the animal dictionary
    employee["id"] = new_id

    # Add the animal dictionary to the list
    EMPLOYEES.append(employee)

    # Return the dictionary with `id` property added
    return employee
