#!/bin/bash
set -e

echo ""
echo "Environment variables:"

echo ""
echo "HOST_IP       : $HOST_IP"
echo "HOST_USERNAME : $HOST_USERNAME"
echo ""

echo ""
echo "Executing ssh to '$HOST_USERNAME@$HOST_IP'"
echo ""

# If we need to ssh into docker host (the in VirtualBox) (when using Docker Toolbox)
# We get the host ip by executing docker-machine ip 
# The password is 'tcuser'
# ---------------------------------------------
# HOST_IP="192.168.99.100"
# HOST_USERNAME="docker@"
SCRIPT="python3 regedit.py"
ssh -i /root/.ssh/id_rsa -o StrictHostKeyChecking=no "$HOST_USERNAME@$HOST_IP" "$SCRIPT"





