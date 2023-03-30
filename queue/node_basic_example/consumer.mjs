import { Queue } from "huddu-node";
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

function send_mail(email, login) {
    // your login
    console.log(`sent an email to ${login}`);
}

// on the consumer we'll periodically read over all new entries.

let generator = await queue.pullAll("signups");



let nextElement = await generator.next()

while (!nextElement.done) {
    console.log(nextElement);
    try {
        send_mail(nextElement.value.email, nextElement.value.login);

        // acknowledge event(and thus delete it) if the mail was successfully sent.
        //queue.acknowledge("signups", nextElement.value._id);
    } catch (error) {
        console.log("an error occoured: ");
        // retry this mail if something went wrong.
        // IMPORTANT: like this the email would be retried infinitely.Ideally you'd only retry it maybe 5 times (or less/more; up to you)
        // to achieve that simply acknowledge failed events and store them again with the event being modified to reflect that it was already retried x times.
        console.log(error);
    }

    nextElement = await generator.next()
}
