import numpy as np
import pyqtgraph as pg
from PySide6.QtCore import QTimer
from PySide6.QtCore import QTimer
from PyQt6.QtCore import QThread, QObject, pyqtSignal as Signal, pyqtSlot as Slot
import threadweight as tw
import scipy.io
import datetime as dt
import pandas as pd
import csv

#MAIN FUNCTION USED IN PLOTTING AND WEIGHT ANALYSIS

def init_plot(self):
    #set to take the COM port info and assign it to channels
    def info_port():
        self.channels=(self.ui.load_pages.comboBox_weight_port.currentText())
        try:
            ini_plot(self)
        except:
            print('error') 
    self.ui.load_pages.but_confirm_weight.clicked.connect(info_port)
    
def ini_plot(self):
    self.bauds=115200
    self.base_weight= []
    self.rate = []
    self.dat = []
    self.longy = []
    self.longx = []
    self.flow = []

    self.windowsize = 3
    self.previousvalue = None
    self.rateofchange = None
    self.nowvalue = None
    self.curremt = None
    self.basevalue = 0
    self.flowrate = 0
    #data from the arduino , threadweight 
    self.weight = tw.WeightData(self.channels)
    self.weightxarduino= self.weight.weightxarduino
    self.weightyarduino= self.weight.weightyarduino 
    self.flowarduino  = self.weight.flowarduino
    
    #display and plot the data every 50 values 
    self.weightxs = np.array(self.weightxarduino)[-50:]
    self.weightys = np.array(self.weightyarduino)[-50:]
    
    self.weight_graph = pg.PlotWidget()
    # Title of the Graph
    self.weight_graph.setTitle("Real-Time Weight Monitoring")
        
    # Label of the bottom
    self.weight_graph.setLabel('bottom', "Time (s)")    
    # left label 
    self.weight_graph.setLabel('left', "grams (g)")
    # Set the color of the background
    self.weight_graph.setBackground('w')
    # Set the color of the line (Green)
    pen3 = pg.mkPen(color=(0, 255, 0), width=2)
    # Creation of the line to put in the weight Graph
    self.line_weight_graph =  self.weight_graph.plot(self.weightys-self.basevalue, self.weightxs, pen=pen3)

    self.ui.load_pages.comboBox_weight_port.currentText()

    #insert graphic in layout
    self.ui.load_pages.Weigh_Layout.addWidget(self.weight_graph)
    

    
    def update_plot():
        #self.weight = tw.WeightData(self.channels)
        #self.channels = 'COM3's
        #self.weightx=self.weight.weightxarduino
        #self.Weighty=self.weight.weightyarduino
        #store in lists so as to save and access the data for calculations
        #x represents the time while y represents the grams
        self.weightxarduino= self.weight.weightxarduino
        self.weightyarduino= self.weight.weightyarduino
        self.longy.extend(self.weightyarduino)
        self.longx.extend(self.weightxarduino)
        self.flowarduino  = self.weight.flowarduino 
        self.flow.extend(self.flowarduino)
        # calculation of the rate of change by taking the current value and the value at the end of the second
        # every Second has 11 values 
        self.data1 = self.flow[-1] if len(self.flow )>= 1 else 0
        self.data2 = self.flow[-11] if len(self.flow )>= 11 else 0

        self.flowrate = self.data1 - self.data2 
        self.rate.append(self.flowrate)
        
        self.weightxs = np.array(self.longx)[-50:]
        self.weightys = np.array(self.longy)[-50:]
        
        self.currentvalue = self.weightys [-1] if len(self.weightys )>= 1 else 0
        
        #self.rounded_rateofchange = round(self.flowarduino  , 2)
       
        #self.curve.setData(self.Weightxs,  self.Weightys-self.basevalue)

        #displaying the new weight after the reset function is called
        self.data3 = (self.currentvalue  - self.basevalue)
        self.base_weight.append(self.data3)
        #round off to the nearest two decimal places 
        self.rounded_data = round(self.data3,  2)
        self.rounded_flow = round(self.flowrate,  2)
        

        #Functions to write the labels (str)
        self.ui.load_pages.label_grams.setText((str(self.rounded_data )))
        self.ui.load_pages.label_flowrate.setText((str(self.rounded_flow )))

        self.line_weight_graph.setData(self.weightxs, self.weightys-self.basevalue)

    # Timer to be used
    self.weight_timer= QTimer()
    self.weight_timer.timeout.connect(update_plot)
    self.weight_timer.setInterval(100)
       
    def saving_data():
        self.directory_weight = self.ui.load_pages.lineEdit_weight_directory.text()
        self.nameFile_weight = self.ui.load_pages.lineEdit_weight_FileName.text()
        self.Format_weght = self.ui.load_pages.comboBox_weight_Format.currentText()
        #self.vectorW.pop(0)
        #self.vectorF.pop(0)
        #data_W = self.base_weight.copy()
        #data_F = self.rate.copy()
        #self.vectorW.append(data_W)
        #self.vectorF.append(data_F)

        # for .mat files
        if(self.Format_weght == ".mat"):
            data_weight = self.base_weight.copy()
            data_flow = self.rate.copy()
            save1 = list(data_weight)
            save2 = list(data_flow)
            df = pd.DataFrame({'weight ':save1, 'rate of change ' :save2})

            scipy.io.savemat(str(self.directory_weight+self.nameFile_weight+self.Format_weght), {'data':df.values}, do_compression=True)
            
        else:
            data_weight = self.base_weight.copy()
            data_flow = self.rate.copy()
            #put the list vertical side to side and add the arduino data at right
            datos=[list(pair) for pair in zip(data_weight, data_flow)]
        #for .csv files 
            with open(str(self.directory_weight+self.nameFile_weight+self.Format_weght), 'a') as f:
                writer = csv.writer(f)
                for file in datos:
                    # Write every row of the final data to save
                    writer.writerow(file)
                #writer.writerow([datos])
                
        #clear the list to start new values every time start is pressed        
        self.base_weight.clear()
        self.rate.clear() 
          
        self.timerSaving.stop()

         
    self.timerSaving = QTimer()
    self.timerSaving.setInterval(300) 
    self.timerSaving.timeout.connect(saving_data)
        
    def start_weight_timer():
        self.weight_timer.start()     
    
    def Stop_weight_timer():
        self.weight_timer.stop()
        self.timerSaving.start()
            
    def reset_weight_zero():
        self.basevalue = self.currentvalue
        #base value is the current y value at that time 
        

    #####################################################################
    # Button connections
    self.ui.load_pages.but_start_weight.clicked.connect(start_weight_timer)
    self.ui.load_pages.but_stop_weight.clicked.connect(Stop_weight_timer)
    self.ui.load_pages.Reset_zero_but.clicked.connect(reset_weight_zero)         

