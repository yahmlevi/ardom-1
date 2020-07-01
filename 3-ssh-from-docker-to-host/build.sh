#!/bin/bash 
set -e

# TAG="ubuntu-trusty-ssh:latest"
TAG=${1:-"ubuntu-trusty-ssh:latest"}
DOCKERFILE=${2:-"test"}

# dos2unix docker-entrypoint.sh
# dos2unix run-ssh.sh

docker build -t $TAG -f $DOCKERFILE.dockerfile .
