import serial
import pycrc
import time

s = serial.Serial("/dev/ttymxc5",9600)    
cmd = [0, 0, 0, 0, 0, 0, 0, 0]

cmd[0] = 0x01  #Device address
cmd[1] = 0x05  #command   
print("two digits: 0 to 7 (8 channels) and [0 (OFF) or 1 [ON]]")
k = input("enter the signal ")

if k[-1] == '1':
    i = k[-2]
    cmd[2] = 0
    cmd[3] = int(i)
    cmd[4] = 0xFF
    cmd[5] = 0
    crc = pycrc.ModbusCRC(cmd[0:6])
    cmd[6] = crc & 0xFF
    cmd[7] = crc >> 8
    print(cmd)
    s.write(cmd)
    time.sleep(0.2)
elif k[-1] == '0':
    j = k[-2]
    cmd[2] = 0
    cmd[3] = int(j)
    cmd[4] = 0
    cmd[5] = 0
    crc = pycrc.ModbusCRC(cmd[0:6])
    cmd[6] = crc & 0xFF
    cmd[7] = crc >> 8
    print(cmd)
    s.write(cmd)
    time.sleep(0.2)
