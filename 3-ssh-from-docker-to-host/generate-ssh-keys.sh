#!/bin/bash
set -e

# Generating SSH keys (run in Git Bash)

# https://docs.joyent.com/public-cloud/getting-started/ssh-keys/generating-an-ssh-key-manually/manually-generating-your-ssh-key-in-windows

cd $HOME
SSH_KEY_NAME
mkdir -p .ssh
cd $HOME/.ssh

# SSH_KEY_NAME=${1:-"id_rsa"}
SSH_KEY_NAME=${1:-"ardom"}

case "$OSTYPE" in
  solaris*) echo "SOLARIS" ;;
  darwin*)  
    echo "OSX" 
    ssh-keygen -f $SSH_KEY_NAME
    ;; 
  linux*)   echo "LINUX" ;;
  bsd*)     echo "BSD" ;;
  msys*)    
    echo "WINDOWS" 
    ssh-keygen.exe -f $SSH_KEY_NAME
    ;;

  *)        echo "unknown: $OSTYPE" ;;
esac

echo "--------------------------------------------------"
ls -l ~/.ssh/``

