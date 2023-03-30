from huddu import Queue

"""
    PART 1: The producer
    
    Create a new queue on the dashboard at https://huddu.io/login?next=/app/store Setting: A user just signed up for 
    your service. Now you'd like to push an event to a queue which is later read by your email service that sends a 
    verification mail out to new users
"""

queue = Queue(
    client_id="<your_client_id>",
    client_secret="<your_client_secret>",
)  # Check https://huddu.io/docs/Queue-SDK for more information

event = {
    "type": "signup",
    "login": "testUser",
    "avatar_url": "https://example.com/testUser.png",
    "email": "test.users@mail.com",
    "signup_via": "Oauth2_google",
    "created": "some date in your favourite date format",
}

queue.push(topic="signups", data=event)
