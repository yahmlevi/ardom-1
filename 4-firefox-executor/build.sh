#!/bin/bash 
set -e

# TAG="ubuntu-trusty-ssh:latest"
TAG=${1:-"firefox"}
DOCKERFILE=${2:-"firefox"}

# dos2unix docker-entrypoint.sh
# dos2unix run-ssh.sh

docker build -t $TAG -f $DOCKERFILE.dockerfile .
