import serial

port_name = "/dev/ttymxc5"
ser = serial.Serial(
      port = port_name,
      baudrate = 115200,
      parity = serial.PARITY_NONE,
      bytesize = serial.EIGHTBITS,
      stopbits = serial.STOPBITS_ONE,
      xonxoff = 0,
      rtscts = 0,
      timeout = 1
)
#ser.write("+++".encode())
Flag = True
i=0
while Flag:
    k = input("Enter the valve name")
    ser.write(bytes(k,'iso-8859-1'))
   
ser.close()
