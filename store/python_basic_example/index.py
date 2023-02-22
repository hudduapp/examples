from math import acos

from huddu import Store

###
# Create a new store: https://huddu.io/login?next=/integrations/store
# In this example we will calculate pi; store it and then access it again to calculate the area of a circle.
###


store = Store("<paste_your_store_token_here>")  # Check https://huddu.io/docs/Store-SDK for more information


def calc_pi(decimal_places):
    return round(2 * acos(0.0), decimal_places)


store.put("pi", calc_pi(3))
# let's store more decimal places...
store.update("pi", calc_pi(5))

# let's store an example radius r
store.put("r", 100)


###
# Imagine now accessing this data on a different machine
###

def calc_circle(pi, r):
    return pi * r ** 2


pi = store.get("pi")
r = store.get("r")

print("the area of the circle is:")
print(calc_circle(pi, r))

#   delete the key/value pairs in the store

store.delete("pi")
store.delete("r")
