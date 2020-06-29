#!/bin/bash
set -e

IMAGE_NAME="ubuntu-trusty-ssh:latest"
docker run --rm -it --privileged --network=host -P $IMAGE_NAME sh

# ip addr show eth0
