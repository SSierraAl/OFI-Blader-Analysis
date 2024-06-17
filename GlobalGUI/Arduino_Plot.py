###########################################################################################################################
################################################# Libraries #############3###############################################
###########################################################################################################################

from random import randint
import numpy as np
import pyqtgraph as pg

from PySide6.QtCore import QTimer

import csv
import scipy.io

from scipy.signal import butter,filtfilt,welch, get_window
from scipy.fft import rfft, rfftfreq
from numpy import trapz

import Thread_Arduino as ta
import Thread_DAQ as td
import threadweight as tw
import plot

############################################################################################################################
######################################## FUNCTIONS #########################################################################
############################################################################################################################
#Function to plug the DAQ and the Arduino
def init_ports(self): 
    #Here we take the data of the GUI to change the ports
    def Take_info_ports(): 
        try:
            self.ui.load_pages.LayoutColor.removeWidget(self.colorGraph)
        except:
            pass
        self.DAQ_Device = (self.ui.load_pages.textEdit_DAQ_Device.toPlainText())
        self.channel=(self.ui.load_pages.comboBox_3.currentText())
        self.DAQ_Device2=(self.ui.load_pages.textEdit_DAQ_Device_2.toPlainText())

        # Put the info of the GUI in our variables
        self.intensity=(self.ui.load_pages.intensity_spin_box.value())
        self.number_of_samples = int(self.ui.load_pages.textEdit.toPlainText())
        self.LaserFrequency = float(self.ui.load_pages.textEdit_SampleFrequency.toPlainText())
        self.Number_to_mean = float(self.ui.load_pages.textEdit_mean.toPlainText())
        self.lowFrequency = float(self.ui.load_pages.textEdit_lowfreq.toPlainText())
        self.highFrequency = float(self.ui.load_pages.textEdit_highfreq.toPlainText())
        self.directory = self.ui.load_pages.textEdit_numberSamples_3.toPlainText()
        self.nameFile = self.ui.load_pages.textEdit_numberSamples_2.toPlainText()
        self.Format = self.ui.load_pages.comboBox.currentText()
        self.fileSave= int(self.ui.load_pages.textEdit_Bauds.toPlainText())
        # Rezise the arrays
        # Rezise the arrays
        self.vectors = [np.zeros(int(self.number_of_samples)) for _ in range(int(self.Number_to_mean))]
        self.vectors2 = [np.zeros(int(self.number_of_samples)) for _ in range(int(self.fileSave))]
        self.vectorsDiode = [np.zeros(int(self.number_of_samples)) for _ in range(self.fileSave)]
        # New window to the Possible PSD
        Init_Arduino(self)
    #Connect the button "Confirm ports" to this function
    self.ui.load_pages.portsButton.clicked.connect(Take_info_ports)
    
#__Init__ of all the variables
def Init_Arduino(self):
    #Cration of thread to catch the data of arduino with 1 as intensity and the channel "comX"
    self.threadArduino=ta.ArduinoData(1,self.channel)
    #Plug the data catch on the thread to this variable
    self.data_Arduino=self.threadArduino.data_Arduino
    #self.data_Arduino=list(range(8))
    self.clickreference=1
    
    ############### Arduino Parameters ######################

    self.CounterRMS=0
    #Bauds of the serial communication between Arduino and PC
    self.bauds=115200
    #Intensity of the led in the AS7341
    self.intensity=1
    #Number of colors to cath
    self.size_colors=8
    ######## WEIGHT ANALYSIS#######
    
    # Array to save all the data to write, Arduino data adquisition
    self.vectors3 = [np.zeros(self.data_Arduino) for _ in range(self.fileSave)]
    # Array to save all the data to write, Arduino weight adquisition
    # Only to have the size to later calcul the average of FFT
    self.FreqData=np.sqrt(np.mean(np.square(self.vectors), axis=0))
    # Creation of the thread of the DAQ, here we send the two ports to catch all the data
    self.threadDAQ = td.DAQData(self.Number_to_mean, self.LaserFrequency, self.number_of_samples, self.DAQ_Device, self.lowFrequency, self.highFrequency,self.fileSave,self.DAQ_Device2)
    # Link the variables here to the thread variables
    self.DAQ_Data=self.threadDAQ.DAQ_Data
    self.DAQ_Diode=self.threadDAQ.DAQ_Data
    self.data_Diode_plot=self.DAQ_Diode.copy()
    # Creation of the arrays to use in the graphs
    self.Volx= np.array(list(range(self.number_of_samples)))*(1/(self.LaserFrequency))
    self.Voly = np.zeros(self.number_of_samples)

    self.dataFFTX=np.zeros(self.number_of_samples)
    self.dataFFTY=np.zeros(self.number_of_samples)
    # Flag of inserts to don't insert more than once
    self.inserts=0
    #Go to next function
    insert_Arduino_graph2(self)
    

    
    ############## Function when we click "Confirm" ############################
    def Take_Info():
        #Delete the graphs that we have to change the size
        deleteGraphs(self)

    
    #####################  New function to save all the data, from the click to x time ##################################
    def vector_stock():
        #print("llenando")
        if(self.countFile_Save < self.fileSave):
            self.countFile_Save +=1
            self.vectors2.pop(0)
            self.vectors3.pop(0)
            self.vectorsDiode.pop(0)
            aux_DAQ=self.threadDAQ.DAQ_Data.copy()
            aux_color=self.threadArduino.data_Arduino.copy()
            aux_Diode=self.threadDAQ.DAQ_Diode.copy()
            self.vectors2.append(aux_DAQ)
            self.vectors3.append(aux_color)
            self.vectorsDiode.append(aux_Diode)
        else:
            self.countFile_Save = 0
            Save_data_2(self)
            
    self.timerSave = QTimer()
    self.timerSave.setInterval(300) #Setting time
    self.timerSave.timeout.connect(vector_stock) 
    self.countFile_Save=0  
        
    def Save_data_future():
        #print("click_save")
        self.timerPLOT.stop()
        self.timerFFT.stop()
        self.timerDQ.stop()
        self.timerSave.start()
 
    ##################### Function to save data ##############################
    def Save_data_2(self):
        # Copy the data to have every time the data of the moment
        data_to_save=(self.vectors2.copy())
        #data_to_save_Arduino=self.vectors3.copy()
        data_to_save_Diode=self.vectorsDiode.copy()
        # Calculate time axis
        dataX=np.array(self.Volx)
        #weightanalysis
        # Format TXT
        
        
        if(self.Format == ".txt"):
            
            for j in range (int(self.fileSave)):
                # Open different file to save the same position of the array
                with open(str(self.directory+self.nameFile+str(j)+self.Format), "w") as file:
                    for i in range (int(self.number_of_samples)):
                        # Copy the data arduino every time it change the file to have the live data
                        data_to_save_Arduino=self.threadArduino.data_Arduino.copy()
                        
                        # Write the file with the format time, laser data, diode data, arduino data
                        file.write(str(dataX[i])+" "+str(data_to_save[j][i])+"  "+str(data_to_save_Diode[j][i]) +" "+ str(data_to_save_Arduino) +'\n')
        
        # Format CSV            
        elif(self.Format == ".csv"):
            for j in range (int(self.fileSave)):
                #Save the data like a list
                datos1=list(dataX)
                datos2=list(data_to_save[j])
                datos3=list(data_to_save_Diode[j])
                data_to_save_Arduino=self.threadArduino.data_Arduino.copy()
                #put the list vertical side to side and add the arduino data at right
                datos=[list(pair)+(data_to_save_Arduino) for pair in zip(datos1, datos2,datos3)]
                # Open different file to save the same position of the list
                with open(str(self.directory+self.nameFile+str(j)+self.Format), "w") as file:
                    # creation of the writer of csv of the file
                    writer = csv.writer(file)
                    for fila in datos:
                        # Write every row of the final data to save
                        writer.writerow(fila)
         
        # Format MAT    
        else:
            for j in range (int(self.fileSave)):
                data_to_save_Arduino=self.threadArduino.data_Arduino.copy()
                #Save the data like a list
                datos1 = list(dataX)
                datos2 = list(data_to_save[j])
                datos3=list(data_to_save_Diode[j])
                data_to_save_Arduino=self.threadArduino.data_Arduino.copy()
                #put the list vertical side to side and add the arduino data at right
                datos=[list(pair)+(data_to_save_Arduino) for pair in zip(datos1, datos2, datos3)]
                #put the name of the file as name of the matrix in matlab
                data_dict = {self.nameFile+str(j): datos}
                # Write the file
                scipy.io.savemat(str(self.directory+self.nameFile+str(j)+self.Format),data_dict, format="5", appendmat=False)
        # relaunch of the FFT and plot process
        self.timerPLOT.start()
        self.timerFFT.start()
        self.timerDQ.start()
        self.timerSave.stop()

    
    ############################################## Reference#####################################################
    def Put_reference():
        if self.clickreference==1:
            pen_reference = pg.mkPen(color=(0, 0, 0))
            referenceX=self.FreqX.copy()
            referenceY=self.FreqY.copy()
            # Creation of the line to put in the Voltage Laser Graph
            self.data_line_Freq_reference =  self.freqGraph.plot(referenceX, referenceY, pen=pen_reference)
            self.clickreference=0
            self.ui.load_pages.label_reference.setText("Reference ON")
        else:
            self.ui.load_pages.label_reference.setText("Please delete")

    def Clear_reference():
        if self.clickreference==0:
            self.freqGraph.removeItem(self.data_line_Freq_reference)
            self.clickreference=1
            self.ui.load_pages.label_reference.setText("Reference OFF")
        else:
            self.ui.load_pages.label_reference.setText("Please put a reference")
        
    # Connect the buttons to save and to take the GUI info
    self.ui.load_pages.Ok_Button.clicked.connect(Take_Info)
    #self.ui.load_pages.Save_Data.clicked.connect(Save_data)
    self.ui.load_pages.Save_Data.clicked.connect(Save_data_future)
    self.ui.load_pages.pushButton_Reference.clicked.connect(Put_reference)
    self.ui.load_pages.pushButton_Clear.clicked.connect(Clear_reference)

#################################################################################################################################################

########## Filter Butterworth ################
def butter_highpass_filter(data, cutoff, fs, order, text2):
        nyq = 0.5 * fs
        normal_cutoff = cutoff / nyq
        b, a = butter(order, normal_cutoff, btype=text2, analog=False)
        y = filtfilt(b, a, data)
        return y
    
#################################################################################################################################################

########## Insert of the graphs ##################
def insert_Arduino_graph2(self):
    # Actualisation of the Arduino intensity
    self.threadArduino.instensity=(self.intensity)
    # Creation of the Color bar Graph
    self.colorGraph = pg.PlotWidget()
    # Title of the Graph
    self.colorGraph.setTitle("Color Intensity")
    # Label of the bottom
    self.colorGraph.setLabel('bottom', "Freq Colors")
    # left label    
    self.colorGraph.setLabel('left', "Percentage of concentration %")
    # Name of the colors we catch
    x_eje=["Violet", "Dark Blue","Blue","Cyan","Green","Yellow","Orange","Red"]
    # Values to put in the bottom label
    x_values=range(len(x_eje))
    # Create every bar with their values and colors
    self.y1gr=pg.BarGraphItem(x=x_values[0],height=self.data_Arduino[0],width=0.9,brush = 'purple')
    self.y2gr=pg.BarGraphItem(x=x_values[1],height=self.data_Arduino[1],width=0.9,brush = 'dark Blue')
    self.y3gr=pg.BarGraphItem(x=x_values[2],height=self.data_Arduino[2],width=0.9,brush = 'b')
    self.y4gr=pg.BarGraphItem(x=x_values[3],height=self.data_Arduino[3],width=0.9,brush = 'cyan')
    self.y5gr=pg.BarGraphItem(x=x_values[4],height=self.data_Arduino[4],width=0.9,brush = 'g')
    self.y6gr=pg.BarGraphItem(x=x_values[5],height=self.data_Arduino[5],width=0.9,brush = 'yellow')
    self.y7gr=pg.BarGraphItem(x=x_values[6],height=self.data_Arduino[6],width=0.9,brush = 'orange')
    self.y8gr=pg.BarGraphItem(x=x_values[7],height=self.data_Arduino[7],width=0.9,brush = 'red')
    # Add every bar to the graph
    self.colorGraph.addItem(self.y1gr)
    self.colorGraph.addItem(self.y2gr)
    self.colorGraph.addItem(self.y3gr)
    self.colorGraph.addItem(self.y4gr)
    self.colorGraph.addItem(self.y5gr)
    self.colorGraph.addItem(self.y6gr)
    self.colorGraph.addItem(self.y7gr)
    self.colorGraph.addItem(self.y8gr)
    # Set the color of the background
    self.colorGraph.setBackground('w')
    
    ############################################################################################################
    #Charge de Graphs to the layouts
    
    self.ui.load_pages.LayoutColor.addWidget(self.colorGraph)
    
    #############################################################################################################
    #Widget Creation
    # Creation of the Voltage Laser Graph
    self.voltageGraph = pg.PlotWidget()
    # Title of the Graph
    self.voltageGraph.setTitle("Laser Signal")
    # Label of the bottom
    self.voltageGraph.setLabel('bottom', "Time(ms)")   
    # left label     
    self.voltageGraph.setLabel('left', "Voltage (V)")
    # Set the color of the background
    self.voltageGraph.setBackground('w')
    # Set the color of the line (Blue)
    pen = pg.mkPen(color=(0, 0, 255))
    # Creation of the line to put in the Voltage Laser Graph
    self.data_line_Vol =  self.voltageGraph.plot(self.Volx, self.Voly, pen=pen)
    
    #Widget Creation
    # Creation of the FFT Laser Graph
    self.freqGraph = pg.PlotWidget()
    # Title of the Graph
    self.freqGraph.setTitle("Frequency Signal")
    # Label of the bottom
    self.freqGraph.setLabel('bottom', "Freq (Hz)")  
    # left label    
    self.freqGraph.setLabel('left', "Amplitude")
    # Put the y axis in Loagarithmic mode
    self.freqGraph.setLogMode(y=True)
    # Creation of the x axis 
    self.Freqx = list(range(self.number_of_samples))  
    # Creation of the y axis 
    self.Freqy = np.zeros(self.number_of_samples)  
    # Set the color of the background
    self.freqGraph.setBackground('w')
    # Set the color of the line (Red)
    pen2 = pg.mkPen(color=(255, 0, 0))
    # Creation of the line to put in the FFT Laser Graph
    self.data_line_Freq =  self.freqGraph.plot(self.Freqx, self.Freqy, pen=pen2)
    
    #Widget Creation Diode
    # Creation of the Voltage Diode Graph
    self.DiodeGraph = pg.PlotWidget()
    # Title of the Graph
    self.DiodeGraph.setTitle("PhotoDiode Signal")
    # Label of the bottom
    self.DiodeGraph.setLabel('bottom', "Time(ms)")    
    # left label 
    self.DiodeGraph.setLabel('left', "Voltage (V)")
    # Set the color of the background
    self.DiodeGraph.setBackground('w')
    # Set the color of the line (Green)
    pen3 = pg.mkPen(color=(0, 255, 0))
    # Creation of the line to put in the Voltage Diode Graph
    self.data_line_Vol_Diode =  self.DiodeGraph.plot(self.Volx, self.Voly, pen=pen3)
    
    
    #Insert Graphs
    self.ui.load_pages.LayoutLaser.addWidget(self.voltageGraph)
    self.ui.load_pages.LayoutLaser.addWidget(self.freqGraph)
    self.ui.load_pages.LayoutLaser.addWidget(self.DiodeGraph)
    # Put the flag on
    self.inserts=1
    
    #PWELCH algotihm process
    self.Window = get_window('hamming', int(self.number_of_samples))
    window_size = 10
    self.conWindow = np.ones(window_size) / window_size
    
    #################################################################################################################
    # FFT Function

    #Filtro butter bandpass  ############################################################
    def butter_bandpass_filter(data, lowcut, highcut, order,fs):
        nyquist = 0.5 * fs
        lowcut = lowcut / nyquist
        highcut = highcut / nyquist
        b, a = butter(order, [lowcut, highcut], btype='band', analog=False)
        y = filtfilt(b, a, data)
        return y

    #FFT ###############################################################################
    def FFT_calc(datos, samplefreq):
        n = len(datos)
        fft_result = np.fft.rfft(datos)
        freq_fft = np.fft.rfftfreq(len(datos), 1 / samplefreq)
        amplitude = np.abs(fft_result)
        phase = np.angle(fft_result)
        return amplitude, freq_fft, phase

    def FreqSpectrum():
        
        # link the data of the first channel adquisition with the variable
        self.DAQ_Data=self.threadDAQ.DAQ_Data
        self.data_DAQ2=butter_bandpass_filter(self.DAQ_Data, self.lowFrequency, self.highFrequency,3, self.LaserFrequency)
        self.dataFFTY, self.dataFFTX, _=FFT_calc(self.DAQ_Data, self.LaserFrequency)
        # Save this data
        self.vectors[self.CounterRMS] = self.dataFFTY
        self.CounterRMS=self.CounterRMS+1
        # When it's the size we wanted in
        if self.CounterRMS==self.Number_to_mean:
            # Clear the counter
            self.CounterRMS=0
            #RMS average
            self.FreqData=np.sqrt(np.mean(np.square(self.vectors), axis=0))
        

    
    #########################################################################################################################################
       
    def update_daq_vector():
        self.data_Diode_plot=np.roll(self.data_Diode_plot,-1)
        aux_Diode=self.threadDAQ.DAQ_Diode.copy()
        aux_diode_plot=np.array(aux_Diode).mean()
        self.data_Diode_plot[-1]=(float(aux_diode_plot))
        
    #################################################################################################################
    # Update plots
     
    def update_plots():        
        # save the data of the Arduino thread in a variable to use easier
        self.data_Arduino=self.threadArduino.data_Arduino
        #print(self.data_Arduino)
        # send the number of samples to the thread
        self.threadDAQ.number_of_samples=self.number_of_samples
        # save the purple data
        aux_purple=self.data_Arduino[0]
        # save the red data
        aux_rouge=self.data_Arduino[7]
        # calculate the pruple ratio
        self.purple_ratio=aux_purple/aux_rouge
        # calculate de HGB ratio (hemoglobine ratio)
        self.hgbratio=7.90445*(0.37612**self.purple_ratio)
        # Names of the Color X axis
        x_eje=["Violet", "Dark Blue","Blue","Cyan","Green","Yellow","Orange","Red"]
        # Number of bars
        x_values=range(len(x_eje))
        # Sum of the values of arduino data
        addition=np.array(self.data_Arduino).sum()
        # Actualisation of bars and calculate the percentage 
        self.data_Arduino2=list(np.array(self.data_Arduino)*100/addition)
        self.y1gr.setOpts(x=x_values[0],height=self.data_Arduino2[0],width=0.9,brush = 'purple')
        self.y2gr.setOpts(x=x_values[1],height=self.data_Arduino2[1],width=0.9,brush = 'dark Blue')
        self.y3gr.setOpts(x=x_values[2],height=self.data_Arduino2[2],width=0.9,brush = 'b')
        self.y4gr.setOpts(x=x_values[3],height=self.data_Arduino2[3],width=0.9,brush = 'cyan')
        self.y5gr.setOpts(x=x_values[4],height=self.data_Arduino2[4],width=0.9,brush = 'g')
        self.y6gr.setOpts(x=x_values[5],height=self.data_Arduino2[5],width=0.9,brush = 'yellow')
        self.y7gr.setOpts(x=x_values[6],height=self.data_Arduino2[6],width=0.9,brush = 'orange')
        self.y8gr.setOpts(x=x_values[7],height=self.data_Arduino2[7],width=0.9,brush = 'red')
        
        # Fix the Y axis range
        self.colorGraph.setYRange(0, 35)
        # Actualisation of HGB in the GUI
        self.ui.load_pages.label_14.setText("HGB ratio : "+str(self.hgbratio))
        self.colorGraph.update()
        
        ######### Update Laser data FFT and Voltage
        # Put the data in our variable
        self.DAQ_X_Axis=self.threadDAQ.DAQ_X_Axis
        # calculate the time
        self.DAQ_X_Axis=np.array(self.DAQ_X_Axis)*1000/(self.LaserFrequency)
        # Put the data in our variable
        self.DAQ_Data=self.threadDAQ.DAQ_Data

        # Update the voltage data
        self.DAQ_Diode=self.threadDAQ.DAQ_Diode
        # Update lines of the graphs
        self.data_line_Vol.setData(self.DAQ_X_Axis, self.DAQ_Data)
        self.data_line_Freq.setData(self.dataFFTX, self.FreqData) 
        self.data_line_Vol_Diode.setData(self.DAQ_X_Axis,np.array(self.data_Diode_plot))
            
    # Creation of timer to calculate FFT
    self.timerFFT = QTimer()
    self.timerFFT.setInterval(51) # Setting time
    self.timerFFT.timeout.connect(FreqSpectrum)   
    # Creation of timer to uplooad the graphs
    self.timerPLOT = QTimer()
    self.timerPLOT.setInterval(1/2000) #Setting time
    self.timerPLOT.timeout.connect(update_plots)   
    #The interval of refresh data in the vector to save
    self.timerDQ = QTimer()
    self.timerDQ.setInterval(51) #Setting time
    self.timerDQ.timeout.connect(update_daq_vector) 
    # Launch the timers
    self.timerFFT.start()
    self.timerPLOT.start()
    self.timerDQ.start()
    
######################################################################################################

#Function to delete the graphs and the Daq Thread

def deleteGraphs(self):
    # Stop the plotting
    self.timerPLOT.stop()
    self.timerPLOT.stop()
    self.timerFFT.stop()
    self.timerDQ.stop()
    self.timerSave.stop()
    # delete the thread
    self.threadDAQ.delete()
    self.threadArduino.delete()
    #Remove the graphs to create new-ones
    #self.ui.load_pages.LayoutColor.removeWidget(self.colorGraph)
    self.ui.load_pages.LayoutLaser.removeWidget(self.voltageGraph)
    self.ui.load_pages.LayoutLaser.removeWidget(self.freqGraph)
    self.ui.load_pages.LayoutLaser.removeWidget(self.DiodeGraph)


