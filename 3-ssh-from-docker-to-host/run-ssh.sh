#!/bin/bash
set -e

# 
# HOST_USERNAME, HOST_OSTYPE and SCRIPT_PATH are received from the docker run command (see run.sh)
# 

case "$HOST_OSTYPE" in
    darwin*)  
        echo "Remote OS type: OSX" 
        HOST="host.docker.internal"
        ;; 
    linux*)   
        echo "Remote OS type: LINUX" 
        HOST="host.docker.internal"
        ;;
    msys*)    
        echo "Remote OS type: WINDOWS" 
        # HOST="172.17.0.1"
        HOST="192.168.56.1"  # - connect to host 192.168.56.1 port 22: Connection refused 
        ;;

    *)        
        echo "unknown: $OSTYPE" 
        ;;
esac

echo ""
echo "Environment variables:"

echo "HOST          : $HOST"
echo "HOST_USERNAME : $HOST_USERNAME"
echo "HOST_OSTYPE   : $HOST_OSTYPE"
echo "SCRIPT_PATH   : $SCRIPT_PATH"
echo ""

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
    cat regedit.bat;
    echo "";
    echo OK
"""

echo "SCRIPT: $SCRIPT"
echo ""
echo "Executing ssh to '$HOST_USERNAME@$HOST'"
echo ""

ssh -i /root/.ssh/id_rsa -o StrictHostKeyChecking=no "$HOST_USERNAME@$HOST" "$SCRIPT"


