# -*- coding: utf-8 -*-
import serial
from random import randint
from time import sleep
import sys
import getopt

def usage ( error=None ):
	if None != error:
		print error
		print
	print "Usage:", sys.argv[0], "[OPTIONS]"
	print
	print "DESCRIPTION"
	print "Displays a (pseudo)random stream of 1's and 0's."
	print
	print "OPTIONS"
	print "-i, --interval   Seconds between digit generation, expressed in a float value. Default: 0.15"
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

ser = serial.Serial( port, 9600, timeout=0)
try:
	out = "101010"
	while True:
		i = randint( 0, 1 )
		out = out[-5:] + str( i )
		ser.write( out + "\n" )
		sleep( sleep_interval )
finally:
	ser.close()