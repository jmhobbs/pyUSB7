# -*- coding: utf-8 -*-
import serial
from random import randint
from time import sleep

ser = serial.Serial('/dev/ttyACM0', 9600, timeout=0)
try:
	out = "101010"
	while True:
		i = randint(0,1)
		out = out[-5:] + str( i )
		ser.write( out + "\n" )
		sleep( 0.15 )
except:
	ser.close()