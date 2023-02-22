from huddu import Drive

###
# Create a new store: https://huddu.io/login?next=/integrations/store
# In this example we will calculate pi; store it and then access it again to calculate the area of a circle.
###


drive = Drive(
    "<paste_your_store_token_here>"
)  # Check https://huddu.io/docs/Drive-SDK for more information

# Let's upload the svg
drive.upload("dog.svg", path="./dog.svg")

# But how do we access it again?
dog_svg = drive.read("dog.svg")
# write it to a new file:
with open("./dog_svg_download.svg", "w") as f:
    f.write(dog_svg)
    f.close()

# Delete the file ? no problemo:
drive.delete("dog.svg")
