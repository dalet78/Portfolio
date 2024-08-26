#!/bin/bash


if [ "$#" -ne 2 ]; then
    echo "Usage: $0 <file.txt> <frase>"
    exit 1
fi

FILE=$1
PHRASE=$2

count=$(grep -oF "$PHRASE" "$FILE" | wc -l)

echo "counting of \"$PHRASE\" compare $count times in file $FILE."