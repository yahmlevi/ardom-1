#!/bin/bash 
set -e

TAG="$1"
DOCKERFILE_NAME=${2:-"$TAG"}

docker build -t $TAG -f "$DOCKERFILE_NAME.dockerfile" . 