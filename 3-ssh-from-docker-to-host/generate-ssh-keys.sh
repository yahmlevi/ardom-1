#!/bin/bash
set -e

# Generating SSH keys (run in Git Bash)

# https://docs.joyent.com/public-cloud/getting-started/ssh-keys/generating-an-ssh-key-manually/manually-generating-your-ssh-key-in-windows

cd $HOME

mkdir -p .ssh
cd $HOME/.ssh

KEY_NAME=${1:-"id_rsa"}
ssh-keygen.exe -f $KEY_NAME
