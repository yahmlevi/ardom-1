#!/bin/bash
set -e

IMAGE_NAME="ubuntu-trusty-ssh:latest"
# -P
docker run --rm -it --privileged --network=host \
    -v ~/.ssh/id_rsa:/root/.ssh/id_rsa:ro \
    -v ~/.ssh/id_rsa.pub:/root/.ssh/id_rsa.pub:ro \
    $IMAGE_NAME sh

# ip addr show eth0
