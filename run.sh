#!/bin/bash

#run the appropriate 
if [ "$1" == "install" ]; then
    echo "### Running install ###"
    pip install -r requirements.txt

fi

echo "Running Project"
python3 run.py
# echo $1