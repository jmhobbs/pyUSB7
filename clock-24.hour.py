# -*- coding: utf-8 -*-
import serial
from time import sleep
from datetime import datetime

ser = serial.Serial('/dev/ttyACM0', 9600, timeout=0)
try:
	while True:
		now = datetime.now().timetuple()
		ser.write( "%02.0d.%02.0d.%02.0d\n" % ( now[3], now[4], now[5] ) )
		sleep( 1 )
except:
	ser.close()