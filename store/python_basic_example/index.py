from math import acos

from huddu import Store

"""
    Create a new store on the dashboard at https://huddu.io/login?next=/app/store
    In this example we will calculate pi; store it + a radius r and then access it again to calculate the area of a circle.
"""

store = Store(
    client_id="<your_client_id>",
    client_secret="<your_client_secret>"
)  # Check https://huddu.io/docs/Store-SDK for more information


def calc_pi(decimal_places):
    return round(2 * acos(0.0), decimal_places)


# Store pi and r in a store
store.put("pi", calc_pi(3))
store.put("r", 100)

# update key "pi"
store.update("pi", calc_pi(5))


# on a different device with internet access...
def calc_circle(pi, r):
    return pi * r ** 2


# Retrieve our values using the keys we used before
pi = store.get("pi")
r = store.get("r")

print("the area of the circle is:")
print(calc_circle(pi, r))

# Removing the key/value pairs using the respective keys
store.delete("pi")
store.delete("r")
