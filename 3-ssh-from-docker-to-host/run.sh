#!/bin/bash
set -e

IMAGE_NAME="ubuntu-trusty-ssh:latest"
# -P
# docker run --rm -it --privileged --network=host \
#     -v ~/.ssh/id_rsa:/root/.ssh/id_rsa:ro \
#     -v ~/.ssh/id_rsa.pub:/root/.ssh/id_rsa.pub:ro \
#     $IMAGE_NAME sh

# ip addr show eth0


# case "$HOST_OSTYPE" in
#     darwin*)  
#         echo "Remote OS type: OSX" 
#         HOST="host.docker.internal"
#         ;; 
#     linux*)   
#         echo "Remote OS type: LINUX" 
#         HOST_IP="host.docker.internal"
#         ;;
#     msys*)    
#         echo "Remote OS type: WINDOWS" 
#         # HOST="172.17.0.1"
        
#         HOST_IP="192.168.56.1"  # - connect to host 192.168.56.1 port 22: Connection refused 
#         ;;

#     *)        
#         echo "unknown: $OSTYPE" 
#         ;;
# esac

SSH_KEY_NAME=${1:-"ardom"}
TEMP_DIR="tmp"

# docker run -p 127.0.0.1:80:8080/tcp ubuntu bash
# echo $PWD
# -v /$PWD/regedit.bat:/regedit.bat \

# 
HOST_IP=$(ipconfig | grep -A 4 'Wireless LAN adapter WiFi' | grep -A 1 'IPv4' |  cut -d ':' -f 2 | xargs)

docker run --rm -it --privileged --network=host \
    -v /$HOME/.ssh/$SSH_KEY_NAME:/$TEMP_DIR/.ssh/id_rsa:ro \
    -v /$HOME/.ssh/$SSH_KEY_NAME.pub:/$TEMP_DIR/.ssh/id_rsa.pub:ro \
    --env HOST_USERNAME=$(whoami) \
    --env HOST_IP=$HOST_IP \
    --env HOST_OSTYPE=$OSTYPE \
    --env SCRIPT_PATH="$PWD" \
    $IMAGE_NAME sh


# HOST_IP="192.168.56.1"
# HOST_IP="172.17.0.1"
# ssh -i $HOME/.ssh/id_rsa Yahm@172.17.0.1
# ssh -i $HOME/.ssh/id_rsa Yahm@localhost
# ssh -i $HOME/.ssh/id_rsa Yahm@$HOST_IP
