#!/bin/bash


if [ "$#" -ne 3 ]; then
    echo "Usage: $0 <command> <sleep_time> <repeat_count>"
    exit 1
fi

COMMAND=$1
SLEEP_TIME=$2
REPEAT_COUNT=$3

for ((i=1; i<=REPEAT_COUNT; i++))
do
    echo "Esecuzione $i: $COMMAND"
    eval $COMMAND  # Esegue il comando
    sleep $SLEEP_TIME  # Attende il tempo specificato
done


#example ./repeat_command.sh "echo Hello" 2 5