
import PyDAQmx
from PyDAQmx.DAQmxFunctions import *

def list_daq_devices():
    buffer_size = 2048
    data = create_string_buffer(buffer_size)
    
    DAQmxGetSysDevNames(data, buffer_size)
    devices = data.value.decode("utf-8").strip().split(', ')
    
    if devices:
        print("Available NI-DAQ devices:")
        for device in devices:
            print(f"Device: {device}")
    else:
        print("No NI-DAQ devices found.")

if __name__ == "__main__":
    list_daq_devices()