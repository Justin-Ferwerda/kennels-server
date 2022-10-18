CUSTOMERS = [
        {
            "id": 1,
            "name": "Justin Ferwerda",
        },
        {
            "id": 2,
            "name": "Natalie Ferwerda",
        }
    ]

def get_all_customers():
    """get all customers"""
    return CUSTOMERS

def get_single_customer(id):
    """get single customer"""
    requested_customer = None

    for customer in CUSTOMERS:
        if customer['id'] == id:
            requested_customer = customer

    return requested_customer

def create_customer(customer):
    """creates animal from dict repr sent by client"""
    # Get the id value of the last animal in the list
    max_id = CUSTOMERS[-1]["id"]

    # Add 1 to whatever that number is
    new_id = max_id + 1

    # Add an `id` property to the animal dictionary
    customer["id"] = new_id

    # Add the animal dictionary to the list
    CUSTOMERS.append(customer)

    # Return the dictionary with `id` property added
    return customer
