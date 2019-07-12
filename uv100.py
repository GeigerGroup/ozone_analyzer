# -*- coding: utf-8 -*-
"""
Created on Tue Jul  2 16:35:29 2019

@author: Geiger
"""

import serial

class UV100():

    def __init__(self):
        
        #initialize serial port
        ser = serial.Serial()
        
        #port on computer
        ser.port = 'COM3'
        
        #serial settings
        ser.bytesize = serial.EIGHTBITS
        ser.stopbits = serial.STOPBITS_ONE
        ser.parity = serial.PARITY_NONE
        ser.xonxoff = False
        ser.baudrate = 9600
        
        #timeout after 1 second so don't wait forever
        ser.timeout = 0.2
        
        #open serial port
        ser.open()
        
        #set serial port property
        self.ser = ser
    
    
    #verifies that topas is there    
    def write(self,text):
        self.ser.write(text)

    def read(self):
        text = self.ser.readline()
        atext = text.decode('ascii').replace('\x00','')
        lst = atext.split(',')
        if len(lst) == 7:
            lst[-1] = lst[-1].replace('\n','')
            lst[0] = lst[0].replace('\r','')
            return lst
        else:
            return None
    
    def close(self):
        self.ser.close()
 