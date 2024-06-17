from random import randint
import serial
import datetime as dt
from PySide6.QtCore import QTimer
from PyQt6.QtCore import QThread, QObject, pyqtSignal as Signal, pyqtSlot as Slot


class WorkerWeight(QObject):
    # signal of finish process
    completedweight = Signal(int)
    bauds=115200
    weightx =list()
    Weighty = list()
    flow =  list()
    
    
    def __init__(self, channels):
        #Important to self-beggining the worker
        super().__init__()
        #channels='COM3'
        self.channels =  channels
        # Open the serial port to coms
        self.ser= serial.Serial(channels, 115200)
        self.reference = dt.datetime.now()
    
    @Slot(int)
    
    
    def takedata(self):
        weightx = list()
        Weighty = list()
        flow = list ()
        j = 1
        # acquiring the arduino data from the serial port chosen
        while self.ser.in_waiting > 0:
            bytes = self.ser.readline()
            decoded = bytes.decode('utf-8').strip('\r\n')
            try:
                self.flt = float(decoded)
                current = dt.datetime.now()
                tim = dt.datetime.now().strftime('%H:%M:%S')
                self.passed = (current - self.reference).total_seconds()
                #function of time 0 to infinity as the data is being processed. 
                Weighty.append(self.flt)
                weightx.append(self.passed)
                flow.append(self.flt)
                
                                  
            except ValueError:
                pass
            
            self.weightx = weightx
            self.Weighty = Weighty
            self.flow = flow
            self.completedweight.emit(j)
           
        
class WeightData(QObject):
    weightArduino_requested =Signal(int)
    
    def __init__(self, channels):
        super().__init__()
        self.channels =  channels
        
        self.weightxarduino = list()
        self.weightyarduino = list()
        self.flowarduino =  list()
        
        self.weight_timer= QTimer()
        self.weight_timer.timeout.connect(self.startweight)
        self.weight_timer.start(20)
        
        self.WorkerWeight = WorkerWeight(self.channels)
         # Creation of the thread
        self.workerthread = QThread()       
        # Connect the worker with our function complete once finish process
        self.WorkerWeight.completedweight.connect(self.completeweight)
        # Connect the signal with the signal in the worker
        self.weightArduino_requested.connect(self.WorkerWeight.takedata)
        # Copy all the worker to a thread
        self.WorkerWeight.moveToThread(self.workerthread)
        # start the thread
        self.workerthread.start()
    
    #Function to start the thread   
    def startweight(self):
        
        n=5
        self.weightArduino_requested.emit(n)
        
    # Function to copy the data when it's done 
    def completeweight(self):
        
        self.weightxarduino=(self.WorkerWeight.weightx)
        self.weightyarduino=(self.WorkerWeight.Weighty)
        self.flowarduino = (self.WorkerWeight.flow)

    #Function to delete the thread.
    def delete(self):
        
        self.weight_timer.stop()
        self.workerthread.quit()  
        self.workerthread.wait()  
        self.workerthread.deleteLater()
        self.deleteLater()