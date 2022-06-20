import time
import serial
import pycrc

import paho.mqtt.client as mqtt
import time

def on_connect(client, userdata, flags, rc):
    print("__Squid Game__")

def send_data_mqtt(data):
    channelID = "1515156"  #Enter your Channel ID here
    apiKey = "Y1TMQ1OX1SXY50IM"  #Enter your WriteAPI key here
    topic = "channels/" + channelID + "/publish/" + apiKey
    
    client = mqtt.Client()
    client.on_connect = on_connect
    client.connect("mqtt.thingspeak.com", 1883, 80)
    tPayload = "field1=" + str(data)
    client.publish(topic, payload=tPayload, qos=0, retain=False)
    #print(f"send {data} to IoT/topic")
    #time.sleep(1)
    return


number_of_remote_valves=5
remote_valves_offset=900
number_of_air_valves = 6
air_valves_offset = 200
number_of_water_valves = 2
water_valves_offset = 300
number_of_water_pumps = 5
water_pumps_offset = 400
number_of_air_compressor = 5
air_compressor_offset = 500

valves = []
address = []
for i in range(int(remote_valves_offset),int(remote_valves_offset)+int(number_of_remote_valves)):
    valves.append('V'+str(i+1))
    address.append(i+1)
for i in range(int(air_valves_offset),int(air_valves_offset)+int(number_of_air_valves)):
    valves.append('AV'+str(i+1))
    address.append(i+1)
for i in range(int(water_valves_offset),int(water_valves_offset)+int(number_of_water_valves)):
    valves.append('WV'+str(i+1))
    address.append(i+1)
for i in range(int(water_pumps_offset),int(water_pumps_offset)+int(number_of_water_pumps)):
    valves.append('WP'+str(i+1))
    address.append(i+1)
for i in range(int(air_compressor_offset),int(air_compressor_offset)+int(number_of_air_compressor )):
    valves.append('AC'+str(i+1))
    address.append(i+1)

lookup_table = dict( zip(valves,address ))



def modbus_status(status):
    ser = serial.Serial(
      port = "/dev/ttymxc5",
      baudrate = 9600,
      parity = serial.PARITY_NONE,
      bytesize = serial.EIGHTBITS,
      stopbits = serial.STOPBITS_ONE,
      xonxoff = 0,
      rtscts = 0,
      timeout = 1
      )
    #s = serial.Serial("/dev/ttymxc5",9600)
    cmd = [0, 0, 0, 0, 0, 0, 0, 0]
    cmd[0] = 0x01  #Device address
    cmd[1] = 0x05  #command   
    #print("two digits: 0 to 7 (8 channels) and [0 (OFF) or 1 [ON]]")
    #k = input("enter the signal ")
    k=status
    if k[-1] == '1':
        i = str(int(k[-2])-1)
        cmd[2] = 0
        cmd[3] = int(i)
        cmd[4] = 0xFF
        cmd[5] = 0
        crc = pycrc.ModbusCRC(cmd[0:6])
        cmd[6] = crc & 0xFF
        cmd[7] = crc >> 8
        #print(cmd)
        ser.write(cmd)
        time.sleep(0.2)
    elif k[-1] == '0':
        j = str(int(k[-2])-1)
        cmd[2] = 0
        cmd[3] = int(j)
        cmd[4] = 0
        cmd[5] = 0
        crc = pycrc.ModbusCRC(cmd[0:6])
        cmd[6] = crc & 0xFF
        cmd[7] = crc >> 8
        #print(cmd)
        ser.write(cmd)
        time.sleep(0.2)
    return


def send_signal(signal):
    port_name = "/dev/ttymxc0"
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
    print(signal)
    ser.write(signal.encode())
    wait(1)
    ser.close()
    return

def ch_status_valves(valve_name,status):
    #valve name = V1,V2... WP3, AC1 etc
    #status = ON or OFF S_D['ON'] S_D['OFF']
    S_D ={'ON':1, 'OFF':0}
    k = (str(lookup_table[valve_name])+str(S_D[status]))
    #k = input("enter valve code ")
    if valve_name[0]=='V':
        send_signal(k)
        print(k)
        send_data_mqtt(k) 
    elif valve_name[0:2] =='AV':
        status = k[2:]
        modbus_status(status)
        print(status)
        send_data_mqtt(status)
    
def wait(wait_duration):
    #time is in sec
    time.sleep(int(wait_duration))
