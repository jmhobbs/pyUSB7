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
from math import floor
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
	print "Displays the total cpu utilization over an interval."
	print
	print "POSIX ONLY!"
	print
	print "OPTIONS"
	print "-f, --file       Path to stat file. Default: /proc/stat"
	print "-i, --interval   The refresh interval, in seconds. Default: 5"
	print "-m, --meter      Display as meter instead of percent."
	print "-p, --port       The port USB7 is on. Default: /dev/ttyACM0"
	print "-h, --help       Show this message."
	exit()

stat_path = '/proc/stat'
port = '/dev/ttyACM0'
sleep_interval = 5
as_meter = False

try:
	options, remainder = getopt.getopt( sys.argv[1:], 'hf:i:p:m', [ 'help', 'file=', 'interval=', 'port=', 'meter' ] )
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
		stat_path = arg
	elif opt in ( '-m', '--meter' ):
		as_meter = True
	elif opt in ( '-p', '--port' ):
		port = arg

r = re.compile( "cpu +([0-9]+) ([0-9]+) ([0-9]+) ([0-9]+)" )

ser = serial.Serial( port, 9600, timeout=0 )
try:
	f = open( stat_path, 'r' )
	t = f.read()
	f.close()

	g = r.match( t )
	u = float( g.group( 1 ) )
	n = float( g.group( 2 ) )
	s = float( g.group( 3 ) )
	i = float( g.group( 4 ) )

	sleep( sleep_interval )

	while True:
		f = open( stat_path, 'r' )
		t = f.read()
		f.close()

		g = r.match( t )
		_u = float( g.group( 1 ) )
		_n = float( g.group( 2 ) )
		_s = float( g.group( 3 ) )
		_i = float( g.group( 4 ) )

		usage = ( ( _u - u ) + ( _n - n ) + ( _s - s ) ) / ( ( _u - u ) + ( _n - n ) + ( _s - s ) + ( _i - i ) ) * 100

		if as_meter:
			count = int( floor( usage / 16.666 ) )
			for i in range( 1, count ):
				ser.write( "-" )
			ser.write( "\n" )
		else:
			ser.write( "%2.0f\n" % usage )

		u = _u
		n = _n
		s = _s
		i = _i

		sleep( sleep_interval )
finally:
	ser.close()