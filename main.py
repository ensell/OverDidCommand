#!/usr/bin/python
# coding: UTF-8
#########################################################################
# Name: OverDid Command
# Version: 0.1
# Author: Chris Ensell
#########################################################################
# Main file
#########################################################################
# Bring in all the libraries
import os
import time
import urllib
from time import sleep

# LIBRARIES NEEDED!
# https://github.com/maliubiao/python-inotify
# import pyinotify
# import RPi.GPIO as GPIO
#from Adafruit_I2C import Adafruit_I2C

# Check for incomming command, run exec if there is one
Incomming = ''
if Incomming: execfile('exec.py')

# Bring in all the modules
# LCD commands
#execfile('lcd.py')
# Check temperature
execfile('pi-temp.py')


