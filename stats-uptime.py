# -*- coding: utf-8 -*-
import serial
from time import sleep
import os

ser = serial.Serial('/dev/ttyACM0', 9600, timeout=0)
try:
	while True:
		uptime = uptime()
		ser.write( "%02.0d.%02.0d.%02.0d\n" % ( now[3], now[4], now[5] ) )
		sleep( 60 )
except:
	ser.close()

# Based on http://thesmithfam.org/blog/2005/11/19/python-uptime-script/
def uptime():
	try:
		f = open( "/proc/uptime" )
		contents = f.read().split()
		f.close()
	except:
		print "Can't sync with uptime file: /proc/uptime"
		return None

	total_seconds = float(contents[0])
	MINUTE  = 60
	HOUR = MINUTE * 60
	DAY = HOUR * 24
	# Get the days, hours, etc:
	uptime = {}
	uptime['days'] = int( total_seconds / DAY )
	uptime['hours']   = int( ( total_seconds % DAY ) / HOUR )
	uptime['minutes'] = int( ( total_seconds % HOUR ) / MINUTE )
	uptime['seconds'] = int( total_seconds % MINUTE )

	return uptime