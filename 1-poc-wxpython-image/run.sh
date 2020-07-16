#!/bin/bash 
set -e


# source - https://stackoverflow.com/questions/58419219/is-display-set-properly-running-a-wxpython-phoenix-gui-in-a-docker-container


# HOST_IP=$(ipconfig | grep inet | head -1 | awk '{print $2}')
# HOST_IP="192.168.65.0"

# https://nickjanetakis.com/blog/docker-tip-65-get-your-docker-hosts-ip-address-from-in-a-container
# HOST_IP="host.docker.internal"

# HOST_IP="ipconfig"
HOST_IP="192.168.56.1"
# HOST_IP="host.docker.internal"
DISPLAY="$HOST_IP:0.0"

echo "HOST_IP   : $HOST_IP"
echo "DISPLAY   : $DISPLAY"

IMAGE="simple_gui:latest"

# -----original------ 
# docker run -it --rm -e DISPLAY=$DISPLAY $IMAGE bash
# -v /tmp/.X11-unix:/tmp/.X11-unix:rw
docker run -it  -e DISPLAY=$DISPLAY --device /dev/dri --privileged $IMAGE bash

# docker run -it --rm -e DISPLAY=$DISPLAY --volume="/tmp/.X11-unix:/tmp/.X11-unix:rw"  $IMAGE



# ip=$(docker run --rm alpine sh -c 'getent hosts docker.for.win.localhost | awk ''{ print $1 }'' ')

# echo $ip

# https://askubuntu.com/questions/541343/problems-with-libgl-fbconfigs-swrast-through-each-update
# https://command-not-found.com/glxgears
# apt install mesa-utils