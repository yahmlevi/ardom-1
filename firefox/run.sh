

# set-variable -name DISPLAY -value YOUR-IP:0.0
HOST_IP="192.168.65.0"
DISPLAY="$HOST_IP:0.0"

IMAGE_NAME="firefox"
docker run -it --rm -e DISPLAY=$DISPLAY $IMAGE_NAME