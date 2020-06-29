#!/bin/bash 
set -e

TAG="ubuntu-trusty-ssh:latest"

docker build -t $TAG -f test.dockerfile .
