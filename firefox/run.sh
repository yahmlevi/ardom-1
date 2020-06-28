

# set-variable -name DISPLAY -value YOUR-IP:0.0
# HOST_IP="192.168.65.0"

# ipconfig -> Ethernet adapter VirtualBox Host-Only Network: -> IPv4 Address
HOST_IP="192.168.56.1"
DISPLAY="$HOST_IP:0.0"

docker run -it --rm -e DISPLAY=$DISPLAY firefox