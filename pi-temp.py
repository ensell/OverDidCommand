#!/bin/python
#########################################################################
# Name: Raspberry Pi Temperature
# Version: 0.1
# Author: Chris Ensell
#########################################################################
# Reads the file created with the temperature of the Pi (in millidegrees)
# makes it more readable and drops it into a variable.
#########################################################################
# SEE pi-information.py FOR REDOING THIS
tempFile = "data/sysTemp"

piTempFile = open(tempFile)
temp = piTempFile.read()
piTempFile.close()
t = eval(temp)
t2 = t*2
piTemp = (t/1000.00)

if piTemp > 50: fanOn = True
else: fanOn = False

if fanOn:
	# TURN ON FAN
	print "Pi fan: On"
else:
	#TURN OFF FAN
	print "Pi fan: Off"

# ADD SOMETHING HERE TO PRINT TEMP TO LCD

# V2, for when added to the Pi
# class ModHandler(pyinotify.ProcessEvent):
#     # evt has useful properties, including pathname
#     def process_IN_CLOSE_WRITE(self, evt):
# 		piTempFile = open(tempFile)
# 		temp = piTempFile.read()
# 		piTempFile.close()
# 		t = eval(temp)
# 		t2 = t*2
# 		piTemp = (t/1000.00)

# handler = ModHandler()
# wm = pyinotify.WatchManager()
# notifier = pyinotify.Notifier(wm, handler)
# wdd = wm.add_watch(tempFile, pyinotify.IN_CLOSE_WRITE)
# notifier.loop()