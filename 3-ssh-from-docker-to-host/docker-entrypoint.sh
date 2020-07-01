#!/bin/sh
set -e

# source 
# # https://nickjanetakis.com/blog/docker-tip-56-volume-mounting-ssh-keys-into-a-docker-container

TEMP_DIR="tmp"

cp -R /$TEMP_DIR/.ssh /root/.ssh

chmod 700 /root/.ssh
chmod 644 /root/.ssh/id_rsa.pub
chmod 600 /root/.ssh/id_rsa

# mind the username@host at the end of the key!
# cat /root/.ssh/id_rsa.pub >> /root/.ssh/authorized_keys
# chmod 600 /root/.ssh/authorized_keys

exec "$@"