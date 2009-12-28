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

print "Incomplete"
exit()

ser = serial.Serial('/dev/ttyACM0', 9600, timeout=0)
try:
	#f = urllib2.urlopen('http://www.random.org/integers/?num=1&min=-99999&max=999999&col=6&base=10&format=plain&rnd=new')
	#x = f.read()
	#print x
	ser.write( " \n" )
	ser.write( "8024 \n" )
	sleep(0.05)
	ser.close()
finally:
	ser.close()