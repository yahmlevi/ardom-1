#!/bin/bash 
set -e
# source - https://stackoverflow.com/questions/58419219/is-display-set-properly-running-a-wxpython-phoenix-gui-in-a-docker-container


# HOST_IP=$(ipconfig | grep inet | head -1 | awk '{print $2}')
HOST_IP="192.168.65.0"
echo host_ip: $HOST_IP
DISPLAY=$HOST_IP:0.0
echo $DISPLAY

IMAGE="simple-gui:latest"
# IMAGE="test1"
docker run -e DISPLAY=$DISPLAY $IMAGE



# ip=$(docker run --rm alpine sh -c 'getent hosts docker.for.win.localhost | awk ''{ print $1 }'' ')

# echo $ip