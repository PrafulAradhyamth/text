from a_v import *
from datetime import datetime
Flag = True

while Flag == True:
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    #print("Current Time =", current_time)
    if current_time !='17:00:00':
        i = input("Enter the mode ") 
        a=Switcher()
        a.numbers_to_modes(int(i))
        Flag = True
    elif current_time == '19:16:00':
        a=Switcher()
        a.numbers_to_modes(int(1))
        Flag = True
    #elif i == '0':
    #    Flag = False

