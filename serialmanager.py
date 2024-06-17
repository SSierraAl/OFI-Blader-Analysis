import serial

ser = None

def open(port, baudrate):
    global ser
    ser = serial.Serial(port,baudrate)
    
def close():
    global ser
    if ser is not None and ser.is_open:
        ser.close()
    else:
        pass
    