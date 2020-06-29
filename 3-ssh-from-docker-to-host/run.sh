#!/biun/bash
set -e

IMAGE_NAME="ubuntu:trusty"
docker run --rm -it --network=host $IMAGE_NAME sh

# ip addr show eth0
