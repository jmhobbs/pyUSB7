# -*- coding: utf-8 -*-
import serial
from time import sleep, mktime
from datetime import datetime, date

ser = serial.Serial('/dev/ttyACM0', 9600, timeout=0)
try:
	while True:
		now = datetime.now().timetuple()
		now_t = mktime( now )
		then_t = mktime(date.today().timetuple() )
		diff = int( now_t - then_t )
		ser.write( "%d\n" % diff )
		sleep( 1 )
except:
	ser.close()