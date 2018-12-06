#!/usr/bin/env python2
from hermes_python.hermes import Hermes
import random

MQTT_IP_ADDR = "localhost"
MQTT_PORT = 1883
MQTT_ADDR = "{}:{}".format(MQTT_IP_ADDR, str(MQTT_PORT))

INTENT_SUGGESTION = "hackathon:suggestion"
INTENT_INCREASE = "hackathon:increase_temperature"
INTENT_DECREASE = "hackathon:decreaese_temperature"

global TEMPERATURE
TEMPERATURE = 20

def main():

    # subscribe to the intents of desire and point to the corresponding callback function
    with Hermes(MQTT_ADDR) as h:
        h.subscribe_intent(INTENT_SUGGESTION, user_suggestion) \
            .subscribe_intent(INTENT_INCREASE, user_increase) \
            .subscribe_intent(INTENT_DECREASE, user_decrease) \
            .start()


suggestions = ["It would be nice if you would turn off the radiator.",
               "Tomorrow will be quite chilly, bring a sweater!",
               "Tomorrow will be sunny, no need to turn on the radiator."]


def user_suggestion(hermes, intent_message):
    session_id = intent_message.session_id
    response = random.choice(suggestions)
    hermes.publish_end_session(session_id, response)


def user_increase(hermes, intent_message):
    global TEMPERATURE
    session_id = intent_message.session_id

    # get temperature increase if available

    if intent_message.slots.degrees:
        degrees = int(intent_message.slots.degrees.first().value)
    else:
        degrees = 1
    TEMPERATURE += degrees
    response = "Alright, I'm increasing the temperature to {} degrees.".format(TEMPERATURE)
    hermes.publish_end_session(session_id, response)


def user_decrease(hermes, intent_message):
    global TEMPERATURE
    session_id = intent_message.session_id
    TEMPERATURE -= 1
    response = "Alright, I'm decreasing the temperature to {} degrees.".format(TEMPERATURE)
    hermes.publish_end_session(session_id, response)


if __name__ == "__main__":
    main()
