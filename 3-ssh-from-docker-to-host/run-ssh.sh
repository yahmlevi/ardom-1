#!/bin/bash
set -e

# 
# HOST_USERNAME, HOST_OSTYPE and SCRIPT_PATH are received from the docker run command (see run.sh)
# 

case "$HOST_OSTYPE" in
        darwin*)  
            echo "Remote OS type: OSX" 
            HOST_IP="host.docker.internal"

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
            ;; 
        linux*)   
            echo "Remote OS type: LINUX" 
            HOST_IP="host.docker.internal"

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
            ;;
        msys*)    
            echo "Remote OS type: WINDOWS" 
            
            # start "openssh" in "Services" and switch to automatic
            # ip address of Wirleless LAN adapter wifi 
            # HOST="192.168.68.111"
            # HOST_IP="192.168.99.255"

            SCRIPT="dir && d: && cd $SCRIPT_PATH && dir && regedit.bat"
            ;;

        *)        
            echo "unknown: $OSTYPE" 
            ;;
    esac

echo ""
echo "Environment variables:"

echo "HOST_IP       : $HOST_IP"
echo "HOST_USERNAME : $HOST_USERNAME"
echo "HOST_OSTYPE   : $HOST_OSTYPE"
echo "SCRIPT_PATH   : $SCRIPT_PATH"
echo ""

# -q 
# Quiet mode.  Causes all warning and diagnostic messages to besuppressed.

# -o StrictHostKeyChecking=no 
# https://unix.stackexchange.com/questions/33271/how-to-avoid-ssh-asking-permission



# 

echo "SCRIPT: $SCRIPT"
echo ""
echo "Executing ssh to '$HOST_USERNAME@$HOST_IP'"
echo ""

# ssh -i /root/.ssh/id_rsa -o StrictHostKeyChecking=no "$HOST_USERNAME@$HOST" "$SCRIPT"
# cd $SCRIPT_PATH

# If we need to ssh into docker host (the in VirtualBox) (when using Docker Toolbox)
# We get the host ip by executing docker-machine ip 
# The password is 'tcuser'
# ---------------------------------------------
# HOST_IP="192.168.99.100"
# HOST_USERNAME="docker@"

ssh -i /root/.ssh/id_rsa -o StrictHostKeyChecking=no "$HOST_USERNAME@$HOST_IP" "$SCRIPT"

# sshpass -p '211367909' ssh -o StrictHostKeyChecking=no  "$HOST_USERNAME@$HOST_IP" "$SCRIPT"





