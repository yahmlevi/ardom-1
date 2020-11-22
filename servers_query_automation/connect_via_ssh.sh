#!/bin/bash
set -e

HOST_IP=" 192.168.68.105"
HOST_USERNAME="Yahm"
HOST_PASSWORD='211367909'
SCRIPT = ""

# ssh -i /root/.ssh/id_rsa -o StrictHostKeyChecking=no "$HOST_USERNAME@$HOST_IP" "$SCRIPT"

sshpass -p $HOST_PASSWORD ssh -o StrictHostKeyChecking=no  "$HOST_USERNAME@$HOST_IP" "$SCRIPT"





