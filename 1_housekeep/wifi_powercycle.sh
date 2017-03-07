#!/bin/bash

echo -n 'WiFi/AirPort power cycling..'
networksetup -setairportpower en1 off
sleep 5
networksetup -setairportpower en1 on
sleep 5
echo -e "\rWiFi/Airport power cycle completed." 
