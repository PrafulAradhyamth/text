import ntplib
import datetime, time
print('Make sure you have an internet connection.')

try:
    client = ntplib.NTPClient()
    response = client.request('pool.ntp.org')
    Internet_date_and_time = datetime.datetime.fromtimestamp(response.tx_time) 
    x=str(Internet_date_and_time)
    #print(x)    #print(x[5:7])#month    #print(x[8:10])#date    #print(x[11:13])#hour
    #print(x[14:16])#min    #print(x[0:4])#year    #print(x[17:19])#sec
    t = x[5:7]+x[8:10]+x[11:13]+x[14:16]+x[0:4]+'.'+x[17:19]
    #print(t)    #date 061111462022.59 monthdatehourminyear.sec

    f = open("time_update.sh", "w")
    f.write("date "+t+'\n')
    f.write("hwclock -w -f /dev/rtc0\n")
    f.write("hwclock -r -f /dev/rtc0\n")
    f.write("dmesg | grep rtc0\n")
    #f.write("reboot\n")
    f.write("date\n")
    f.close()

except OSError:
    print('\n')
    print('Internet date and time could not be reported by server.')
    print('There is not internet connection.')