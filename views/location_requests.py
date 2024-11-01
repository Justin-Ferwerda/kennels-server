import sqlite3
import json
from .models import Location, Employee, Animal



LOCATIONS = [
        {
            "id": 1,
            "name": "Nashville North",
            "address": "8422 Johnson Pike"
        },
        {
            "id": 2,
            "name": "Nashville South",
            "address": "209 Emory Drive"
        }
    ]

def get_all_locations():
    """gets all locations"""
    # Open a connection to the database
    with sqlite3.connect("./kennel.sqlite3") as conn:

        # Just use these. It's a Black Box.
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        # Write the SQL query to get the information you want
        db_cursor.execute("""
        SELECT
            a.id,
            a.name,
            a.address
        FROM location a
        """)

        # Initialize an empty list to hold all animal representations
        locations = []

        # Convert rows of data into a Python list
        dataset = db_cursor.fetchall()

        # Iterate list of data returned from database
        for row in dataset:

            # Create an animal instance from the current row.
            # Note that the database fields are specified in
            # exact order of the parameters defined in the
            # Animal class above.
            location = Location(row['id'], row['name'], row['address'])

            locations.append(location.__dict__)

    # Use `json` package to properly serialize list as JSON
    return json.dumps(locations)

def get_single_location(id):
    """get single location"""
    with sqlite3.connect("./kennel.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT
        l.id AS location_id,
        l.name AS location_name,
        l.address AS location_address,
        e.id AS employee_id, e.name AS employee_name, e.address AS employee_address,
        a.id AS animal_id, a.name AS animal_name, a.breed, a.status, a.customer_id
        FROM 
            location l
        JOIN 
            employee e ON l.id = e.location_id
        JOIN 
            animal a ON l.id = a.location_id
        WHERE 
            l.id = ?
        """, ( id, ))

    results = db_cursor.fetchall()
    location = Location(results[0]["location_id"], results[0]["location_name"], results[0]["location_address"])
    data = {
        'employees': [],
        'animals': []
    }
    animal_ids = set()
    employee_ids = set()
    for row in results:
        if row["employee_id"] not in employee_ids:
            employee = Employee(row["employee_id"], row["employee_name"], row["employee_address"], id)
            data["employees"].append(employee.serialized())
            employee_ids.add(row["employee_id"])

        if row["animal_id"] not in animal_ids:
            animal = Animal(row["animal_id"], row["animal_name"], row["breed"], row["status"], id, row["customer_id"])
            data["animals"].append(animal.serialized())
            animal_ids.add(row["animal_id"])

    response = location.__dict__ | data

    return response

def create_location(location):
    """creates animal from dict repr sent by client"""
    # Get the id value of the last animal in the list
    max_id = LOCATIONS[-1]["id"]

    # Add 1 to whatever that number is
    new_id = max_id + 1

    # Add an `id` property to the animal dictionary
    location["id"] = new_id

    # Add the animal dictionary to the list
    LOCATIONS.append(location)

    # Return the dictionary with `id` property added
    return location

def delete_location(id):
    """delete location"""
    with sqlite3.connect("./kennel.sqlite3") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        DELETE FROM location
        WHERE id = ?
        """, (id, ))

def update_location(id, new_location):
    """updates animal"""
    # Iterate the ANIMALS list, but use enumerate() so that
    # you can access the index value of each item.
    for index, location in enumerate(LOCATIONS):
        if location["id"] == id:
            # Found the animal. Update the value.
            LOCATIONS[index] = new_location
            break
