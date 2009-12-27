# -*- coding: utf-8 -*-
import serial
from time import sleep, mktime
import sys

sleep_interval = 0.15

if len( sys.argv ) > 1:
	try:
		sleep_interval = float( sys.argv[1] )
	except:
		print "Usage:", sys.argv[0], "[INTERVAL]"
		print "INTERVAL is seconds expressed in a float value."
		print "It is the time between movements of the scanner."
		exit()

ser = serial.Serial('/dev/ttyACM0', 9600, timeout=0)
try:
	x = 0
	ltr = True
	while True:
		ser.write( "-" )
		for i in range(0,x):
			ser.write( " " )
		ser.write( "\n" )
		x = ( x + 1 ) if ltr else ( x - 1 )
		if x >= 5:
			ltr = False
		elif x <= 0:
			ltr = True
		sleep( sleep_interval )
finally:
	ser.close()