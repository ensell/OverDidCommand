#!/bin/python
#########################################################################
# Name: Raspberry Pi Temperature
# Version: 0.1
# Author: Chris Ensell
#########################################################################
# Reads the file created with the temperature of the Pi (in millidegrees)
# makes it more readable and drops it into a variable.
#########################################################################

piTempFile = open("data/sysTemp")
str = piTempFile.read()
piTempFile.close()
t = eval(str)
t2 = t*2
piTemp = (t/1000.00)