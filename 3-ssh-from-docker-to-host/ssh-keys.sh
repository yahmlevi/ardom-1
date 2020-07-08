#!/bin/bash
set -e

# Generating SSH keys (run in Git Bash)

# https://docs.joyent.com/public-cloud/getting-started/ssh-keys/generating-an-ssh-key-manually/manually-generating-your-ssh-key-in-windows

# SSH_KEY_NAME=${1:-"id_rsa"}
SSH_KEY_NAME=${1:-"ardom"}

function create_keys(){

    cd $HOME

    mkdir -p .ssh
    cd $HOME/.ssh

    case "$OSTYPE" in
        solaris*) 
            echo "SOLARIS" 
            ;;
        darwin*)  
            echo "OSX" 
            ssh-keygen -f $SSH_KEY_NAME
            ;; 
        linux*)   
            echo "LINUX" 
            ;;
        bsd*)     
            echo "BSD" 
            ;;
        msys*)    
            echo "WINDOWS" 
            ssh-keygen.exe -f $SSH_KEY_NAME
            ;;

        *)        
            echo "unknown: $OSTYPE" 
            ;;
    esac
}

function add_key_to_authorized(){
    cat $HOME/.ssh/$SSH_KEY_NAME.pub >> $HOME/.ssh/authorized_keys
    chmod 600 $HOME/.ssh/authorized_keys

    echo "--------------------------------------------------"
    cat $HOME/.ssh/authorized_keys
    

}


# create_keys
add_key_to_authorized

echo "--------------------------------------------------"
ls -l ~/.ssh/``
