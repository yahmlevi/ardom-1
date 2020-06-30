#!/bin/bash
set -e

# HOST_USERNAME and SCRIPT_PATH are received from the docker run command (see run.sh)
# HOST="host.docker.internal"
# HOST="172.17.0.1"
# HOST="192.168.56.1"  - connect to host 192.168.56.1 port 22: Connection refused 

echo "HOST          : $HOST"
echo "HOST_USERNAME : $HOST_USERNAME"
echo "SCRIPT_PATH   : $SCRIPT_PATH"

# -q 
# Quiet mode.  Causes all warning and diagnostic messages to besuppressed.

# -o StrictHostKeyChecking=no 
# https://unix.stackexchange.com/questions/33271/how-to-avoid-ssh-asking-permission

# SCRIPT="""
#     ls -l; 
#     cd $SCRIPT_PATH; 
#     echo ""; 
#     echo 'Testing 1-2-3'; 
#     echo '';
#     echo OK
# """

SCRIPT="ls -l"

echo "SCRIPT: $SCRIPT"

echo "Executing ssh to '$HOST_USERNAME@$HOST'"
# ssh -i ~/.ssh/id_rsa -o StrictHostKeyChecking=no -q "$HOST_USERNAME@$HOST" "$SCRIPT"
ssh -i ~/.ssh/id_rsa -o StrictHostKeyChecking=no "$HOST_USERNAME@$HOST"

