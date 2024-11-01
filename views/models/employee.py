class Employee:
    """employee class"""
    def __init__(self, id, name, address,  location_id):
        self.id = id
        self.name = name
        self.address = address
        self.location_id = location_id
        self.location = None

    def serialized(self):
        return {
            "id": self.id,
            "name": self.name,
            "address": self.address
        }
