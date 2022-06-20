import serial
if __name__ == '__main__':
    ser = serial.Serial('/dev/ttymxc2', 9600, timeout=1)
    ser.reset_input_buffer()
    l = 0
    while True:
        if ser.in_waiting > 0:
   
            line = ser.readline().decode('utf-8')
            print(line)
