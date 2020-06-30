#!/bin/bash
set -e

# HOST_USERNAME and SCRIPT_PATH are received from the docker run command (see run.sh)
HOST="host.docker.internal"

# -q 
# Quiet mode.  Causes all warning and diagnostic messages to besuppressed.

# -o StrictHostKeyChecking=no 
# https://unix.stackexchange.com/questions/33271/how-to-avoid-ssh-asking-permission

SCRIPT="""
    ls -l; 
    cd $SCRIPT_PATH; 
    echo ""; 
    echo 'Testing 1-2-3'; 
    echo '';
    echo OK
"""

ssh -i ~/.ssh/id_rsa -o StrictHostKeyChecking=no -q "$HOST_USERNAME@$HOST" "$SCRIPT"
