#!/bin/bash
set -e

# set-variable -name DISPLAY -value YOUR-IP:0.0
# HOST_IP="192.168.65.0"

# ipconfig -> Ethernet adapter VirtualBox Host-Only Network: -> IPv4 Address
HOST_IP=$(ipconfig | grep -A 4 'Ethernet adapter VirtualBox Host-Only Network:' | grep -A 1 'IPv4' |  cut -d ':' -f 2)

DISPLAY="$HOST_IP:0.0"

IMAGE_NAME="firefox"
docker run -it --rm -e DISPLAY="$DISPLAY" "$IMAGE_NAME"