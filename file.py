#!/usr/bin/python
# -*- coding: utf-8 -*-
import RPi.GPIO as GPIO
import random as rand
import time

GPIO.setmode(GPIO.BCM)

# hate this shit

GPIO.setup(6, GPIO.OUT)
GPIO.SETUP(26, GPIO.IN)
voltstatus = GPIO.input(26)
GPIO.output(6, GPIO.LOW)
p = GPIO.PWM(6, 1)
freq = 1
p.start(freq)
while 0 < 1:
    try:
        if voltstatus == 1:
            freq = rand.randint(1, 6)
        else:

            GPIO.output(6, 0)
            print "python's fucked"
    except KeyboardInterrupt:
        GPIO.cleanup()
