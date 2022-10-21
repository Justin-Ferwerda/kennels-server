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

def delete_customer(id):
    """deletes animal"""
    # Initial -1 value for animal index, in case one isn't found
    customer_index = -1

    # Iterate the ANIMALS list, but use enumerate() so that you
    # can access the index value of each item
    for index, customer in enumerate(CUSTOMERS):
        if customer["id"] == id:
            # Found the animal. Store the current index.
            customer_index = index

    # If the animal was found, use pop(int) to remove it from list
    if customer_index >= 0:
        CUSTOMERS.pop(customer_index)

def update_customer(id, new_customer):
    """updates animal"""
    # Iterate the ANIMALS list, but use enumerate() so that
    # you can access the index value of each item.
    for index, customer in enumerate(CUSTOMERS):
        if customer["id"] == id:
            # Found the animal. Update the value.
            CUSTOMERS[index] = new_customer
            break
