# -*- coding: utf-8 -*-
import serial
from time import sleep
import re

r = re.compile( "/([0-9]+)" )
ser = serial.Serial('/dev/ttyACM0', 9600, timeout=0)
try:
	while True:
		# Get total processes.
		f = open( '/proc/loadavg', 'r' )
		t = f.read()
		f.close()
		g = r.search( t )
		x = g.group(1)
		ser.write( "%s\n" % x )
		sleep( 5 )
except:
	ser.close()