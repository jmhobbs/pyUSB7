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
from datetime import datetime
import sys
import getopt

def usage ( error=None ):
	if None != error:
		print error
		print
	print "Usage:", sys.argv[0], "[OPTIONS]"
	print
	print "DESCRIPTION"
	print "Displays a clock, formatted as HH.MM.SS"
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
		ser.write( "%02.0d.%02.0d.%02.0d\n" % ( now[3], now[4], now[5] ) )
		sleep( 1 )
finally:
	ser.close()