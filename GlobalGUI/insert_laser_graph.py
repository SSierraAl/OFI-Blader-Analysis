from random import randint
import numpy as np
import pyqtgraph as pg
from nidaqmx.stream_readers import AnalogSingleChannelReader
import nidaqmx as ni
from nidaqmx import constants
from nidaqmx import stream_readers
from PySide6.QtCore import QTimer
from scipy.signal import butter,filtfilt,welch, get_window
from scipy.fft import rfft, rfftfreq
from numpy import trapz

def butter_highpass_filter(data, cutoff, fs, order, text2):
        nyq = 0.5 * fs
        normal_cutoff = cutoff / nyq
        b, a = butter(order, normal_cutoff, btype=text2, analog=False)
        y = filtfilt(b, a, data)
        return y

def InsertLaserGraphs(self):
        
    #Widget Creation
    self.voltageGraph = pg.PlotWidget()
    self.voltageGraph.setTitle("Laser Signal")
    self.voltageGraph.setLabel('bottom', "Time(ms)")    
    self.voltageGraph.setLabel('left', "Voltage (V)")
    self.Volx = list(range(10000))  # 100 time points
    self.Voly = [randint(0,100) for _ in range(10000)]  # 100 data points
    self.voltageGraph.setBackground('w')
    pen = pg.mkPen(color=(0, 0, 255))
    self.data_line_Vol =  self.voltageGraph.plot(self.Volx, self.Voly, pen=pen)
    
    #Widget Creation
    self.freqGraph = pg.PlotWidget()
    self.freqGraph.setTitle("Frequency Signal")
    self.freqGraph.setLabel('bottom', "Freq (Hz)")    
    self.freqGraph.setLabel('left', "Amplitude")
    self.Freqx = list(range(1000))  # 100 time points
    self.Freqy = [randint(0,100) for _ in range(1000)]  # 100 data points
    self.freqGraph.setBackground('w')
    pen2 = pg.mkPen(color=(255, 0, 0))
    self.data_line_Freq =  self.freqGraph.plot(self.Freqx, self.Freqy, pen=pen2)
    
    #Insert Graphs
    self.ui.load_pages.LayoutLaser.addWidget(self.voltageGraph)
    self.ui.load_pages.LayoutLaser.addWidget(self.freqGraph)


    #PWELCH algotihm process
    self.Window = get_window('hamming', self.number_of_samples)
    window_size = 10
    self.conWindow = np.ones(window_size) / window_size
        

    def update_plot_data():
        
        self.data_line_Vol.setData(self.DAQ_X_Axis, self.DAQ_Data)
        self.data_line_Freq.setData(self.Freqx, self.Freqy)
        print(self.DAQ_Data.size)
        self.timerDAQ.start()
        self.timerPLOT.start()


    def FreqSpectrum():  
        #self.timerDAQ.stop()
        self.timerPLOT.stop()
        self.data_DAQ2=butter_highpass_filter(self.DAQ_Data, self.lowFrequency, self.Laser_frequency, 3, "high")
        #4000
        self.data_DAQ2=butter_highpass_filter(self.data_DAQ2, self.HighFrequency, self.Laser_frequency, 3, "low")

        self.vectors[self.CounterRMS] = self.DAQ_Data
        self.CounterRMS=self.CounterRMS+1

        if self.CounterRMS==self.Number_to_mean:
            
            self.timerDAQ.stop()
            self.timerPLOT.stop()
            self.CounterRMS=0
        
            #RMS average
            FreqData=np.sqrt(np.mean(np.square(self.vectors), axis=0))

            #Descomentar
            #FFT
            yf = rfft(self.DAQ_Data)
            xf = rfftfreq(self.number_of_samples, 1 / self.Laser_frequency)
            yf=np.abs(yf)
            self.dataFFTX=xf
            self.dataFFTY=yf

            #res = np.mean(FreqData.reshape(-1, ), axis=1)
            #PSD
            self.dataFreq,self.dataFreqY = welch(FreqData, fs=self.Laser_frequency, window = self.Window)
            
            window_size = 5
            window = np.ones(window_size) / window_size
            self.Freqy = np.convolve(self.dataFreqY, window, mode='valid')
            self.Freqx = np.convolve(self.dataFreq, window, mode='valid')
            
            
            frequencies=self.Freqx[:4000]
            psd=self.Freqy[:4000]

            #positionCm=round(float(self.Zaber_Pos)*100/1039370,5)
            #m0 = round(abs(trapz(frequencies,psd)*1000),5)
            #m1 = round(abs(trapz(frequencies,frequencies*psd)),5) #Calculate first moment

            #Processing
            #with open(str(self.directory+"ValuesData.txt"), 'a') as file:
            #   file.write("Pos: "+str(positionCm)+" M0: "+str(m0)+" M1: "+str(m1)+ '\n')

            
            update_plot_data()
            
    
    def wait_time():
            
        self.timerWait.stop()
        self.timerDAQ.start()
        self.timerPLOT.start()

        
    #Timer PLOT
    self.timerPLOT = QTimer()
    self.timerPLOT.setInterval(1/2000)
    self.timerPLOT.timeout.connect(FreqSpectrum)
    
    self.timerWait = QTimer()
    self.timerWait.setInterval(2)
    self.timerWait.timeout.connect(wait_time)