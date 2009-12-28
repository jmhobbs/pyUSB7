# -*- coding: utf-8 -*-
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