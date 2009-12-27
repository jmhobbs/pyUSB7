# -*- coding: utf-8 -*-
import serial
from time import sleep, mktime
import sys
import getopt

def usage ( error=None ):
	if None != error:
		print error
		print
	print "Usage:", sys.argv[0], "[OPTIONS]"
	print
	print "OPTIONS"
	print "-i, --interval   Seconds between movements, expressed in a float value. Default: 0.15"
	print "-p, --port       The port USB7 is on. Default: /dev/ttyACM0"
	print "-h, --help       Show this message."
	exit()

sleep_interval = 0.15
port = '/dev/ttyACM0'

try:
	options, remainder = getopt.getopt( sys.argv[1:], 'hi:p:', [ 'help', 'interval=', 'port=' ] )
except:
	usage( "Invalid option." )

for opt, arg in options:
	if opt in ( '-h', '--help' ):
		usage()
	elif opt in ( '-i', '--interval' ):
		try:
			sleep_interval = float( arg )
		except:
			usage( opt + ' must be a floating point number.' )
	elif opt in ( '-p', '--port' ):
		port = arg

ser = serial.Serial( port, 9600, timeout=0 )
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