#!/bin/sh

ifconfig wwan0 down
echo Y > /sys/class/net/wwan0/qmi/raw_ip
ifconfig wwan0 up
qmi-network /dev/cdc-wdm0 start
udhcpc -i wwan0
