from huddu import Queue

"""
    PART 2: The consumer

    Setting: A user just signed up for your service. Now you'd like to push an event to a queue which is later read by your email service that sends a verification mail out to new users
"""

queue = Queue(
    client_id="<your_client_id>",
    client_secret="<your_client_secret>",
)  # Check https://huddu.io/docs/Queue-SDK for more information


def send_mail(email: str, login: str):
    # your login
    print(f"sent an email to {login}")


# on the consumer we'll periodically read over all new entries.

for i in queue.pull_all("signups"):
    try:
        send_mail(i["email"], i["login"])

        # acknowledge event(and thus delete it) if the mail was successfully sent.
        queue.acknowledge("signups", i["_id"])
    except Exception as e:
        print("an error occoured: ")
        # retry this mail if something went wrong.
        # IMPORTANT: like this the email would be retried infinitely. Ideally you'd only retry it maybe 5 times (or less/more; up to you)
        # to achieve that simply acknowledge failed events and store them again with the event being modified to reflect that it was already retried x times.
        print(e)
