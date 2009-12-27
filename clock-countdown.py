# -*- coding: utf-8 -*-
import serial

ser = serial.Serial('/dev/ttyACM0', 9600, timeout=0)
try:
	x = 999999
	while x >= 0:
		ser.write( "%d\n" % x )
		x = x - 1
except:
	ser.close()