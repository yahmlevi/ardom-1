#!/bin/bash 
set -e

TAG="ssh_from_docker:latest"

docker build -t $TAG -f test.dockerfile .
