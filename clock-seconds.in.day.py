# -*- coding: utf-8 -*-
import serial
from time import sleep, mktime
from datetime import datetime, date
import sys
import getopt

def usage ( error=None ):
	if None != error:
		print error
		print
	print "Usage:", sys.argv[0], "[OPTIONS]"
	print
	print "DESCRIPTION"
	print "Shows a the total elapsed seconds in the day."
	print
	print "OPTIONS"
	print "-p, --port       The port USB7 is on. Default: /dev/ttyACM0"
	print "-h, --help       Show this message."
	exit()

port = '/dev/ttyACM0'

try:
	options, remainder = getopt.getopt( sys.argv[1:], 'hp:', [ 'help', 'port=' ] )
except:
	usage( "Invalid option." )

for opt, arg in options:
	if opt in ( '-h', '--help' ):
		usage()
	elif opt in ( '-p', '--port' ):
		port = arg

ser = serial.Serial( port, 9600, timeout=0 )
try:
	while True:
		now = datetime.now().timetuple()
		now_t = mktime( now )
		then_t = mktime( date.today().timetuple() )
		diff = int( now_t - then_t )
		ser.write( "%d\n" % diff )
		sleep( 1 )
except:
	ser.close()