#!/bin/bash 
set -e

TAG="simple-gui:latest"

docker build -t $TAG -f test.dockerfile .
