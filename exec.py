#!/usr/bin/python
#########################################################################
# Name: Command Execution
# Version: 0.1
# Author: Chris Ensell
#########################################################################
# This file SHOULD control all commands sent via button
#
# Should display message on the LCD
#	 Should display confirmation
# 		 Light up green (confirm) and red (cancel) buttons
#
# If confirmed, should execute command
#
# Commands stored in sysCommands
#########################################################################
doThis = False

cmd = open('data/sysCommands')
cmdLines = cmd.readlines()

if Incomming:
	findCommand = [cmdLines.index(i) for i in cmdLines if Incomming in i]

	if findCommand:
		run = cmdLines[findCommand[0]].strip()[len(Incomming)+1:]

		# Confirmation?  I dunno...  Need to get everything put together first.
		print "Are you sure?"

		if doThis:
			if Incomming == "ping":
				os.system(run)
			else:
				os.system(run)
	else:
		print "Command not found: " + Incomming