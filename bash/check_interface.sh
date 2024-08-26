#!/bin/bash


if [ -z "$1" ]; then
    echo "Usage: $0 <INTERFACE>"
    exit 1
fi

INTERFACE=$1


if ip link show "$INTERFACE" | grep -q "state UP"; then
    echo 0  
else
    echo 1  
fi

#examle ./check_interface.sh eth0