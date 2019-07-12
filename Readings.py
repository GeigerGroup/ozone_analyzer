# -*- coding: utf-8 -*-
"""
Created on Tue Jul  2 16:35:00 2019

@author: Geiger
"""

import time
import threading
import csv

class Readings():
    
    def __init__(self,name,instrument):
        self.name = name
        self.instr = instrument
        self.timer = InfiniteTimer(1, self.getData)
        self.fileID = open(self.name,'a+')
        self.fileID.write('ppm,temp,pressure,flowrate,voltage,day,time\r')
        #append = csv.writer(self.fileID)
        #append.writerow(['ppm','temp','pressure','flowrate','voltage','day','time'])
        
        

              
    def start(self):
        self.timer.start()
    
    def stop(self):
        self.timer.cancel()
        self.fileID.close()
        
    def getData(self):
        data = self.instr.read()
        if data != None:
            append = csv.writer(self.fileID,lineterminator = '\r')
            append.writerow(data)
            print(data)
        
class InfiniteTimer():
    """A Timer class that does not stop, unless you want it to."""

    def __init__(self, seconds, target):
        self._should_continue = False
        self.is_running = False
        self.seconds = seconds
        self.target = target
        self.thread = None

    def _handle_target(self):
        self.is_running = True
        self.target()
        self.is_running = False
        self._start_timer()

    def _start_timer(self):
        if self._should_continue: # Code could have been running when cancel was called.
            self.thread = threading.Timer(self.seconds, self._handle_target)
            self.thread.start()

    def start(self):
        if not self._should_continue and not self.is_running:
            self._should_continue = True
            self._start_timer()
        else:
            print("Timer already started or running, please wait if you're restarting.")

    def cancel(self):
        if self.thread is not None:
            self._should_continue = False # Just in case thread is running and cancel fails.
            self.thread.cancel()
        else:
            print("Timer never started or failed to initialize.")


        
        