# we import the Twilio client from the dependency we just installed
from twilio.rest import Client

# the following line needs your Twilio Account SID and Auth Token
client = Client("ACc0556d292f568a90307797081f21e0fa", "3296b2a07c826c432bb04ca0c1f5ccf3")

# change the "from_" number to your Twilio number and the "to" number
# to the phone number you signed up for Twilio with, or upgrade your
# account to send SMS to any phone number
client.messages.create(to="972526026586",
                       from_="972526026586",
                       body="Hello from Python!")