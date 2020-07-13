#!/bin/bash 
set -e

TAG="simple_gui:latest"

# dos2unix ./run.sh
# dos2unix ./simple_gui.py

DOCKERFILE="wxpython.dockerfile"

dos2unix $DOCKERFILE

echo ""
echo "Building docker image"
echo "------------------------------------------"
docker build -t $TAG -f $DOCKERFILE .
