#!/bin/bash 
set -e

TAG=$1

docker build -t $TAG -f windows.dockerfile . 