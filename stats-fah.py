# -*- coding: utf-8 -*-
import serial
from time import sleep
import re
import sys
import getopt

def usage ( error=None ):
	if None != error:
		print error
		print
	print "Usage:", sys.argv[0], "[OPTIONS]"
	print
	print "DESCRIPTION"
	print "Displays the current completion status of your F@h work unit. In percent."
	print
	print "OPTIONS"
	print "-f, --file       Path to unitinfo.txt. Default: /var/cache/fah/unitinfo.txt"
	print "-i, --interval   The refresh interval, in seconds. Default: 3600"
	print "-p, --port       The port USB7 is on. Default: /dev/ttyACM0"
	print "-h, --help       Show this message."
	exit()

unitinfo_path = '/var/cache/fah/unitinfo.txt'
port = '/dev/ttyACM0'
sleep_interval = 3600

try:
	options, remainder = getopt.getopt( sys.argv[1:], 'hf:i:p:', [ 'help', 'file=', 'interval=', 'port=' ] )
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
	elif opt in ( '-f', '--file' ):
		unitinfo_path = arg
	elif opt in ( '-p', '--port' ):
		port = arg

r = re.compile( "Progress: +([0-9]+)%" )
ser = serial.Serial( port, 9600, timeout=0 )
try:
	while True:
		f = open( unitinfo_path, 'r' )
		t = f.read()
		f.close()
		g = r.search( t )
		x = g.group( 1 )
		ser.write( "%s\n" % x )
		sleep( sleep_interval )
finally:
	ser.close()