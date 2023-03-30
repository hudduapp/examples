import { Queue } from "huddu-node"
//or import using require: let Queue = require("huddu-node").Queue




/*
    PART 1: The producer
    
    Create a new queue on the dashboard at https://huddu.io/login?next=/app/store Setting: A user just signed up for 
    your service.Now you'd like to push an event to a queue which is later read by your email service that sends a 
    verification mail out to new users
*/


let queue = new Queue(
    "<your_client_id>",
    "<your_client_secret>"
);

let event = {
    "type": "signup",
    "login": "testUser",
    "avatar_url": "https://example.com/testUser.png",
    "email": "test.users@mail.com",
    "signup_via": "Oauth2_google",
    "created": "some date in your favourite date format",
}

await queue.push("signups", event)
