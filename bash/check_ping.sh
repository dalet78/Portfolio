#!/bin/bash

# Verify if is passed ip
if [ -z "$1" ]; then
    echo "Usage: $0 <IP_ADDRESS>"
    exit 1
fi


TARGET=$1

# number of packet
PING_COUNT=1


ping -c $PING_COUNT $TARGET > /dev/null 2>&1

#Verify result and wite it
if [ $? -eq 0 ]; then
    echo 0  
else
    echo 1  
fi

#example ./check_ping.sh 8.8.8.8