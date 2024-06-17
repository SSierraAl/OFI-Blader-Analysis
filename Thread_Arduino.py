###########################################################################################################################
################################################# Libraries ###############################################################
###########################################################################################################################

from PyQt6.QtCore import QThread, QObject, pyqtSignal as Signal, pyqtSlot as Slot
from PyQt6.QtCore import QTimer

import serial
from PyQt6.QtCore import QThread, QObject, pyqtSignal as Signal, pyqtSlot as Slot
import serial

from PySide6.QtCore import QTimer

############################################################################################################################
######################################## Thread DAQ ########################################################################
############################################################################################################################

#Class Worker, it's who gonna do the process of adquisition in the background
class WorkerArduino(QObject):
    # signal of finish process
    completed = Signal(int)
    # Initialisation of important values, Bauds, size of the array and the data
    bauds=115200
    size_colors=8
    data= list(range(8))
    
    # Function of initilisation of the class worker
    def __init__(self,intensity,channel):
        #Important to self-beggining the worker
        super().__init__()
        # Definition of all variables needed to take the data and do the coms with Arduino and the intensity to send
        self.intensity=intensity
        self.channel = channel
        # Open the serial port to coms
        self.ArduinoComs=serial.Serial(self.channel,self.bauds)
    
    # Function of adquisition
    
    @Slot(int)
    def data_adq(self):
        # Transform de value of intensity like string to send on the serial port
        intensitycmd=str(self.intensity)+'\r' 
        # Send the intensity encode
        self.ArduinoComs.write(intensitycmd.encode())
        # create a new auxiliar variable
        data= list()
        # Process to read the value from the Arduino
        for j in range (self.size_colors):
            # Receive the Arduino data one by one
            datoArduino=str(self.ArduinoComs.readline(),'utf-8').strip('\r\n')
            # Check if the channel is empty, don't crash
            if(datoArduino!=""):
                data.append(float(datoArduino))
            else:
                data.append(0.0)
        # Send complete
        self.data=data
        self.completed.emit(j)
        

class ArduinoData(QObject):
    # Creation of the requested thread of the worker
    workArduino_requested = Signal(int)
    # Function of initilisation of the class ArduinoData
    def __init__(self,intensity,channel):
        #Important to self-beggining the ArduinoData
        super().__init__()
        # Intensity
        self.intensity=intensity
        #Channel
        self.channel=channel
        # Creation of the list with 8 values
        self.data_Arduino= list(range(8))
        # Creation of timer to do always the same process, with a delay of 20ms each one
        self.timerArduino=QTimer()
        self.timerArduino.timeout.connect(self.start)
        self.timerArduino.start(20)
        # Creation of the worker linked to this class
        self.workerArduino = WorkerArduino(self.intensity,self.channel)
        # Creation of the thread
        self.worker_thread = QThread()       
        # Connect the worker with our function complete once finish process
        self.workerArduino.completed.connect(self.complete)
        # Connect the signal with the signal in the worker
        self.workArduino_requested.connect(self.workerArduino.data_adq)
        # Copy all the worker to a thread
        self.workerArduino.moveToThread(self.worker_thread)
        # start the thread
        self.worker_thread.start()
    
    #Function to start the thread   
    def start(self):
        
        n=5
        self.workerArduino.intensity=(self.intensity)
        self.workArduino_requested.emit(n)
    
    # Function to copy the data when it's done 
    def complete(self):
        
        self.data_Arduino=(self.workerArduino.data)
        self.workerArduino.intensity=(self.intensity)
    
    #Function to delete the thread.
    def delete(self):
        
        self.timerArduino.stop()
        self.worker_thread.quit()  # Detener el hilo
        self.worker_thread.wait()  # Esperar a que el hilo finalice
        self.worker_thread.deleteLater()
        self.deleteLater()