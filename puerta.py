#!/usr/bin/env python
# -*- coding: utf-8 -*-
from data_loader import DataLoader
from logger import get_logger
import paho.mqtt.publish as publish

settings = DataLoader()
logger = get_logger("puerta")
logger.setLevel(0)

def puerta(bot, update, args, job_queue, chat_data):
    log_message(update)
    logger.debug("hostname: " + settings.mqtt_hostname + "\n username: " + settings.mqtt_auth["username"] + "\n password: " + settings.mqtt_["password"])

def abrir():
    logger.debug("hostname: " + settings.mqtt["hostname"] + 
                "\n username: " + settings.mqtt["username"] + 
                "\n password: " + settings.mqtt["password"])
    publish.single("cmnd/PUERTA/POWER", "1", hostname=settings.mqtt_hostname, auth = settings.mqtt_auth)

if __name__ == "__main__":
    print ("Bienvenido, se va a abrir la porta.")
