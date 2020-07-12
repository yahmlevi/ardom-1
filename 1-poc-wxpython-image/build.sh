#!/bin/bash 
set -e

TAG="simple_gui:latest"

dos2unix ./run.sh
dos2unix ./simple_gui.py

docker build -t $TAG -f wxpython.dockerfile .
