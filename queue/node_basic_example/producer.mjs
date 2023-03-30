import { Store } from "huddu-node"
//or import using require: let Store = require("huddu-node").Store




let store = new Store(
    "<your_client_id>",
    "<your_client_secret>"
)


// Create a new store on the dashboard at https://huddu.io/login?next=/app/store
// In this example we will calculate pi; store it + a radius r and then access it again to calculate the area of a circle.



// Let's calculate the area of a cube that's defined by two edges called "a" and "b" on a remote machine

// Store "a" and "b"
// Note: Running this the second time on one store? .put will throw an exception if an element with the same name is already set. use safe=false if you want to get around this behaviour

await store.put(
    "a",
    10
)

await store.put(
    "b",
    20
)


// oops... I got a wrong.. let's update it
await store.update(
    "a",
    30
)


// On a remote machine with internet access
let a = await store.get("a")
let b = await store.get("b")


let area = a * b
console.log("The area of the rectangle is: " + area + " (Entities)")



// let's clean up:
await store.delete("a")
await store.delete("b")


