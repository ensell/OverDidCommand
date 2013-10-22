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
#from Adafruit_I2C import Adafruit_I2C
from time import sleep
# import RPi.GPIO as GPIO

Incomming = 'mysqlstart'
Command = True

# Bring in all the modules
#execfile('lcd.py')
execfile('fan-control.py')
execfile('pi-temp.py')

if Command: execfile('exec.py')

if piTemp > 160: print "Pi running hot"