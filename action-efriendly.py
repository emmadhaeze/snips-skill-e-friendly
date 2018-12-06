#!/usr/bin/env python2
from hermes_python.hermes import Hermes
import random

MQTT_IP_ADDR = "localhost"
MQTT_PORT = 1883
MQTT_ADDR = "{}:{}".format(MQTT_IP_ADDR, str(MQTT_PORT))

INTENT_SUGGESTION = "hackathon:suggestion"
INTENT_INCREASE = "hackathon:increase_temperature"
INTENT_DECREASE = "hackathon:decreaese_temperature"

def main():

    # subscribe to the intents of desire and point to the corresponding callback function
    with Hermes(MQTT_ADDR) as h:
        h.subscribe_intent(INTENT_SUGGESTION, user_suggestion) \
            .subscribe_intent(INTENT_INCREASE, user_increase) \
            .subscribe_intent(INTENT_DECREASE, user_decrease) \
            .start()


def user_suggestion(hermes, intent_message):
    session_id = intent_message.session_id
    response = "User asked for suggestion."
    hermes.publish_end_session(session_id, response)


def user_increase(hermes, intent_message):
    session_id = intent_message.session_id
    response = "User asked to increase temperature."
    hermes.publish_end_session(session_id, response)


def user_decrease(hermes, intent_message):
    session_id = intent_message.session_id
    response = "User asked to decrease temperature."
    hermes.publish_end_session(session_id, response)


if __name__ == "__main__":
    main()
