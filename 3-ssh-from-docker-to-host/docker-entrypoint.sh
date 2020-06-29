#!/bin/sh
set -e

TEMP_DIR="tmp"

cp -R /$TEMP_DIR/.ssh /root/.ssh

chmod 700 /root/.ssh
chmod 644 /root/.ssh/id_rsa.pub
chmod 600 /root/.ssh/id_rsa

exec "$@"