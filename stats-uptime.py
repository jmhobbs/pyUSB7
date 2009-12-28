# -*- coding: utf-8 -*-

# Copyright (c) 2009 John Hobbs

# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:

# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.

# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.

import serial
from time import sleep
import os
import sys
import getopt

def usage ( error=None ):
	if None != error:
		print error
		print
	print "Usage:", sys.argv[0], "[OPTIONS]"
	print
	print "DESCRIPTION"
	print "Displays the total uptime of your machine."
	print
	print "OPTIONS"
	print "-f, --file       Path to uptime file. Default: /proc/uptime"
	print "-i, --interval   The refresh interval, in seconds. Default: 60"
	print "-p, --port       The port USB7 is on. Default: /dev/ttyACM0"
	print "-h, --help       Show this message."
	exit()

uptime_path = '/proc/uptime'
port = '/dev/ttyACM0'
sleep_interval = 60

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
		uptime_path = arg
	elif opt in ( '-p', '--port' ):
		port = arg

ser = serial.Serial( port, 9600, timeout=0 )
try:
	while True:
		uptime = uptime()
		if None != uptime:
			ser.write( "%02.0d.%02.0d.%02.0d\n" % ( uptime[3], uptime[4], uptime[5] ) )
		sleep( sleep_interval )
finally:
	ser.close()

# Based on http://thesmithfam.org/blog/2005/11/19/python-uptime-script/
def uptime():
	try:
		f = open( uptime_path )
		contents = f.read().split()
		f.close()
	except:
		print "Can't sync with uptime file:", uptime_path
		return None

	total_seconds = float( contents[0] )
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