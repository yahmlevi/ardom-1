#!/bin/bash
set -e

IMAGE_NAME="ubuntu-trusty-ssh:latest"
# -P
# docker run --rm -it --privileged --network=host \
#     -v ~/.ssh/id_rsa:/root/.ssh/id_rsa:ro \
#     -v ~/.ssh/id_rsa.pub:/root/.ssh/id_rsa.pub:ro \
#     $IMAGE_NAME sh

# ip addr show eth0

KEY_NAME=${1:-"id_rsa"}
TEMP_DIR="tmp"

docker run --rm -it --privileged --network=host \
    -v /$HOME/.ssh/$KEY_NAME:/$TEMP_DIR/.ssh/id_rsa:ro \
    -v /$HOME/.ssh/$KEY_NAME.pub:/$TEMP_DIR/.ssh/id_rsa.pub:ro \
    $IMAGE_NAME sh


# HOST_IP="192.168.56.1"
# HOST_IP="172.17.0.1"
# ssh -i $HOME/.ssh/id_rsa Yahm@172.17.0.1
# ssh -i $HOME/.ssh/id_rsa Yahm@localhost
# ssh -i $HOME/.ssh/id_rsa Yahm@$HOST_IP
