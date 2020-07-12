

# set-variable -name DISPLAY -value YOUR-IP:0.0
# HOST_IP="192.168.65.0"

# ipconfig -> Ethernet adapter VirtualBox Host-Only Network: -> IPv4 Address
HOST_IP=$(ipconfig | grep -A 4 'Ethernet adapter VirtualBox Host-Only Network:' | grep -A 1 'IPv4' |  cut -d ':' -f 2)
DISPLAY="$HOST_IP:0.0"

IMAGE_NAME="firefox"

# XDG_RUNTIME_DIR
# https://dev.to/darksmile92/run-gui-app-in-linux-docker-container-on-windows-host-4kde

# XDG_RUNTIME_DIR is an environment variable that any program will access to determine the user specific directory to store small temporary files to. 
# Normally it is set automatically when you log in.
#
# example
# export XDG_RUNTIME_DIR=/home/USERNAME/tmp

docker run -it --rm \
    --env DISPLAY=$DISPLAY \
    --env XDG_RUNTIME_DIR="/home/root/tmp" \
    $IMAGE_NAME