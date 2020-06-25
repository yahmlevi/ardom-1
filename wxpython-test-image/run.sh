#!/bin/bash 
set -e
# source - https://stackoverflow.com/questions/58419219/is-display-set-properly-running-a-wxpython-phoenix-gui-in-a-docker-container


# HOST_IP=$(ipconfig | grep inet | head -1 | awk '{print $2}')
# HOST_IP="192.168.65.0"

# https://nickjanetakis.com/blog/docker-tip-65-get-your-docker-hosts-ip-address-from-in-a-container
# HOST_IP="host.docker.internal"

HOST_IP="172.17.0.2"

echo "HOST_IP: $HOST_IP"

DISPLAY="$HOST_IP:0.0"
# DISPLAY=":0.0"

# DISPLAY="127.0.0.1:10.0"
echo $DISPLAY

IMAGE="simple-gui:latest"
# IMAGE="test1"

docker run -it --rm -e DISPLAY=$DISPLAY $IMAGE

# docker run -it --rm -e DISPLAY=$DISPLAY --volume="/tmp/.X11-unix:/tmp/.X11-unix:rw"  $IMAGE



# ip=$(docker run --rm alpine sh -c 'getent hosts docker.for.win.localhost | awk ''{ print $1 }'' ')

# echo $ip