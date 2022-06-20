modprobe wilc-sdio

wpa_supplicant -B -Dnl80211 -i wlan0 -c /etc/wpa_supplicant.conf

udhcpc -i wlan0
