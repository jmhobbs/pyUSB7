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
from xml.dom.minidom import parseString
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
	print "Displays the current temperature from the Google weather API."
	print
	print "OPTIONS"
	print "-z, --zipcode    The zipcode to check. Default: 68028"
	print "-c, --celsius    Show value in Celsius, rather than Farenheight."
	print "-i, --interval   The refresh interval in seconds. Set high. Default: 1800"
	print "-p, --port       The port USB7 is on. Default: /dev/ttyACM0"
	print "-h, --help       Show this message."
	exit()

sleep_interval = 1800
system = "f"
zipcode = "68028"
port = '/dev/ttyACM0'

try:
	options, remainder = getopt.getopt( sys.argv[1:], 'hz:i:cp:', [ 'help', 'zipcode=', "interval=", "celsius", 'port=' ] )
except:
	usage( "Invalid option." )

for opt, arg in options:
	if opt in ( '-h', '--help' ):
		usage()
	elif opt in ( '-i', '--interval' ):
		try:
			sleep_interval = float( arg )
		except:
			usage( opt + " must be a number." )
	elif opt in ( '-c', '--celsius' ):
		system = 'c'
	elif opt in ( '-z', '--zipcode' ):
		zipcode = arg
	elif opt in ( '-p', '--port' ):
		port = arg

ser = serial.Serial( port, 9600, timeout=0 )
try:
	while True:
		f = urllib2.urlopen( 'http://www.google.com/ig/api?weather=' + str( zipcode ) )
		x = f.read()
		dom = parseString( x )
		temp = dom.getElementsByTagName( "temp_" + system )[0].getAttribute( 'data' )
		dom.unlink()
		ser.write( temp + "\n" )
		sleep( sleep_interval )
finally:
	ser.close()