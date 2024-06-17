
from random import randint
import threading
import numpy as np
import pyqtgraph as pg
import serial
import datetime as dt
import pandas as pd
import time

from PySide6.QtCore import QTimer

def init_weight(self):
    #self.channel=(self.ui.load_pages..currentText())
    self.ser = serial.Serial('COM5', 115200)
    self.reference = dt.datetime.now()
    self.weightx = []
    self.Weighty = []
    self.rate = []
    self.arr = []
    self.dat = []
    self.windowsize = 30
    self.record = {}
    self.previousvalue = None
    self.rateofchange = None
    self.nowvalue = None
    self.curremt = None
    self.basevalue = 0
    self.rounded_rateofchange = 0

    # Variables with x and y information
    self.Weightxs = np.array(self.weightx)[-50:]
    self.Weightys= np.array(self.Weighty)[-50:]

    #####################################################################
    # Insert Graphic

    self.weight_graph = pg.PlotWidget()
    # Title of the Graph
    self.weight_graph.setTitle("Real-Time Weight Monitoring")
    # Label of the bottom
    self.weight_graph.setLabel('bottom', "Time (s)")    
    # left label 
    self.weight_graph.setLabel('left', "milliLitre (ml)")
    # Set the color of the background
    self.weight_graph.setBackground('w')
    # Set the color of the line (Green)
    pen3 = pg.mkPen(color=(0, 255, 0), width=2)
    # Creation of the line to put in the weight Graph
    self.line_weight_graph =  self.weight_graph.plot(self.Weightys-self.basevalue, self.Weightxs, pen=pen3)



    #insert graphic in layout
    self.ui.load_pages.Weigh_Layout.addWidget(self.weight_graph)


    # Function to update the graphic
    def update_weight_plot():
        #print('timer working')
        while self.ser.in_waiting > 0:
            bytes = self.ser.readline()
            decoded = bytes.decode('utf-8').strip('\r\n')
            try:
                self.flt = float(decoded)
                current = dt.datetime.now()
                tim = dt.datetime.now().strftime('%H:%M:%S')
                self.passed = (current - self.reference).total_seconds()
                self.weightx.append(self.passed)
                self.Weighty.append(self.flt)
                self.data1 = self.Weighty[-1]
                self.data2 = self.Weighty[-11] if len(self.Weighty )>= 11 else 0

            except ValueError:
                pass
        
        self.flowrate = self.data1 - self.data2 
        self.rounded_rateofchange = round(self.flowrate, 2)  
        self.Weightys = np.array(self.Weighty)[-50:]
        self.Weightxs = np.array(self.weightx)[-50:]

        self.currentvalue = self.Weighty[-1] if self.Weighty else 0
       
        #self.curve.setData(self.Weightxs,  self.Weightys-self.basevalue)
        self.data3 = (self.currentvalue  - self.basevalue)
        self.rate.append(self.data3)

        self.flowrate = self.data1 - self.data2
        self.rounded_rateofchange = round(self.flowrate, 2)
        self.rounded_data = round( self.data3, 2)
        
        self.arr.append(self.rounded_rateofchange)

        i=0

        while i < len(self.arr) - self.windowsize + 1:
            window = self.arr[i: i + self.windowsize]
            self.average = round(sum(window)/self.windowsize, 2)
            i +=1 
         
        self.dat.append(self.average)
        self.tad = self.dat[-1]
          
        #Functions to write the labels (str)
        self.ui.load_pages.label_grams.setText((str(self.rounded_data)))
        self.ui.load_pages.label_flowrate.setText((str(self.tad )))

        self.line_weight_graph.setData(self.Weightxs, self.Weightys-self.basevalue )

    # Timer to be used
    self.weight_timer= QTimer()
    self.weight_timer.timeout.connect(update_weight_plot)
    self.weight_timer.setInterval(10)
        
    def Start_weight_timer():
        self.weight_timer.start()

    def Stop_weight_timer():
        self.weight_timer.stop()
        
    def reset_weight_zero():
        self.basevalue = self.currentvalue

        

    #####################################################################
    # Button connections
    self.ui.load_pages.but_start_weight.clicked.connect(Start_weight_timer)
    self.ui.load_pages.but_stop_weight.clicked.connect(Stop_weight_timer)
    self.ui.load_pages.Reset_zero_but.clicked.connect(reset_weight_zero)
    