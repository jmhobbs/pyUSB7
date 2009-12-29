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
from datetime import datetime, timedelta
from time import mktime, sleep
from math import floor
import sys
import getopt

def break_time_down ( seconds ):
	r = { 'days': 0, 'hours': 0, 'minutes': 0, 'seconds': 0 }
	r['days'] = floor( seconds / 86400 )
	seconds = seconds - ( r['days'] * 86400 )
	r['hours'] = floor( seconds / 3600 )
	seconds = seconds - ( r['hours'] * 3600 )
	r['minutes'] = floor( seconds / 60 )
	seconds = seconds - ( r['minutes'] * 60 )
	r['seconds'] = seconds
	return r

def usage ( error=None ):
	if None != error:
		print error
		print
	print "Usage:", sys.argv[0], "[OPTIONS] -c COUNTDOWN"
	print
	print "DESCRIPTION"
	print "Displays a countdown from a given amount of time."
	print "Will show as much of the remaining time as possible."
	print
	print "COUNTDOWN    The time to count down from. The format is: "
	print "             Days:Hours:Minutes:Seconds"
	print
	print "             Examples:"
	print "                    12:15  12 Minutes, 20 Seconds"
	print "                 5:4:0:20  5 Days, 4 Hours, 20 Seconds"
	print
	print "OPTIONS"
	print "-p, --port       The port USB7 is on. Default: /dev/ttyACM0"
	print "-h, --help       Show this message."
	exit()


port = '/dev/ttyACM0'
countdown = None

try:
	options, remainder = getopt.getopt( sys.argv[1:], 'hp:c:', [ 'help', 'port=' ] )
except:
	usage( "Invalid option." )

for opt, arg in options:
	if opt in ( '-h', '--help' ):
		usage()
	elif opt in ( '-p', '--port' ):
		port = arg
	elif opt == '-c':
		countdown = arg

if None == countdown:
	usage( "You must provide a value for COUNTDOWN." )

split_up = countdown.split( ':' )
split_up.reverse()

storage = { 'days': 0, 'hours': 0, 'minutes': 0, 'seconds': 0 }

if len( split_up ) > 4:
	usage( "Invalid value for COUNTDOWN, " + countdown + ", too many sections." )

try:
	if 4 == len( split_up ):
		storage['days'] = int( split_up[3] )
	if 3 <= len( split_up ):
		storage['hours'] = int( split_up[2] )
	if 2 <= len( split_up ):
		storage['minutes'] = int( split_up[1] )
	if 1 <= len( split_up ):
		storage['seconds'] = int( split_up[0] )
except:
	usage( "Invalid value for COUTDOWN, " + countdown + ", integer values only please." )

delta = timedelta(days=storage['days'], hours=storage['hours'], minutes=storage['minutes'], seconds=storage['seconds'] )

then = mktime( ( datetime.now() + delta ).timetuple() )

for i in range( 0, 10 ):
	now = mktime( datetime.now().timetuple() )
	print break_time_down( then - now )
	sleep( 1 )

#ser = serial.Serial( port, 9600, timeout=0 )
#try:
	#then
	#now = mktime( datetime.now().timetuple() )
	#while x >= 0:
		#ser.write( "%d\n" % x )
		#x = x - 1
#finally:
	#ser.close()