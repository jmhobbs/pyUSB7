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
import urllib2
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
	print "Displays a REAL random number from random.org!"
	print
	print "OPTIONS"
	print "-u, --upper-bound     The upper bound to pull from. Default: 999999"
	print "-l, --lower-bound     The lower bound to pull from. Default: -99999"
	print "-p, --port            The port USB7 is on. Default: /dev/ttyACM0"
	print "-h, --help            Show this message."
	exit()

upper_bound = 999999
lower_bound = -99999
port = '/dev/ttyACM0'

try:
	options, remainder = getopt.getopt( sys.argv[1:], 'hu:l:p:', [ 'help', 'upper-bound=', 'lower-bound=', 'port=' ] )
except:
	usage( "Invalid option." )

for opt, arg in options:
	if opt in ( '-h', '--help' ):
		usage()
	elif opt in ( '-u', '--upper-bound' ):
		try:
			upper_bound = int( arg )
		except:
			usage( opt + ' must be an integer.' )
	elif opt in ( '-l', '--lower-bound' ):
		try:
			lower_bound = int( arg )
		except:
			usage( opt + ' must be an integer.' )
	elif opt in ( '-p', '--port' ):
		port = arg

if lower_bound >= upper_bound:
	usage( "The lower bound must be larger than the upper bound." )

if lower_bound < -99999:
	usage( "Lower bound too low. -99999 is the limit." )

if upper_bound > 999999:
	usage( "Upper bound too high. 999999 is the limit." )

ser = serial.Serial( port, 9600, timeout=0 )
try:
	f = urllib2.urlopen( 'http://www.random.org/integers/?num=1&min=%d&max=%d&col=6&base=10&format=plain&rnd=new' % ( lower_bound, upper_bound ) )
	x = f.read()
	y = int( x )
	ser.write( "%d\n" % y )
	sleep( 0.15 ) # Prevents us from closing before it's finished
finally:
	ser.close()