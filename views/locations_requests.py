"""Handles Locations Data"""
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
    },
        {
      "id": 3,
      "name": "Weho",
      "address": "West Hollywood Ct"
    },
    {
      "id": 4,
      "name": "Echo Park",
      "address": "Swan Lake Park Ct"
    }
]

def get_all_locations():
    return LOCATIONS

def get_single_location(id):
    requested_location = None

    for location in LOCATIONS:
        if location["id"] == id:
            requested_location = location

    return requested_location
        