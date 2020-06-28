#!/bin/bash 
set -e

# ./build.sh "nano-server-1903"

TAG="$1"
DOCKERFILE_NAME=${2:-"$TAG"}

docker build -t $TAG -f "$DOCKERFILE_NAME.dockerfile" . 