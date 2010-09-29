# -*- coding: utf-8 -*-

# Copyright (c) 2010 John Hobbs

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
import sys
import getopt

import feedparser

def usage ( error=None ):
	if None != error:
		print error
		print
	print "Usage:", sys.argv[0], "[OPTIONS] <gmail-config.py>"
	print
	print "DESCRIPTION"
	print "Displays the last trade price of a stock symbol."
	print
	print "OPTIONS"
	print "-i, --interval   The refresh interval, in seconds. Default: 600"
	print "-p, --port       The port USB7 is on. Default: /dev/ttyACM0"
	print "-h, --help       Show this message."
	exit()

port = '/dev/ttyACM0'
sleep_interval = 150

try:
	options, remainder = getopt.getopt( sys.argv[1:], 'hs:i:p:', [ 'help', 'symbol=', 'interval=', 'port=' ] )
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

if 1 != len( remainder ):
	usage( 'you must pass a configuration file' )

config = None
try:
	config = __import__( remainder[0][:-3], None, None, [''] )
except ImportError, e:
	usage( 'Couldn\'t load configuration: ' + str( e ) )

ser = serial.Serial( port, 9600, timeout=0 )
try:
	while True:
		total = 0
		for account in config.accounts:
			feed = feedparser.parse( account )
			total += len( feed['entries'] )
		ser.write( total + "\n" )
		sleep( sleep_interval )
finally:
	ser.close()
