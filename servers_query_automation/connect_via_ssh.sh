#!/bin/bash
set -e

# TODO
# 
# - loop that iterates throgh list of IP Adresses 
# - CRP to known location files: 1. PowerShell script that finds OS version and 
# - 

HOST_IP="192.168.0.72"
HOST_USERNAME="Yahm"
HOST_PASSWORD="211367909"
IP_LIST=("192.168.68.105", "192.168.62.104")

# ssh -i /root/.ssh/id_rsa -o StrictHostKeyChecking=no "$HOST_USERNAME@$HOST_IP" "$SCRIPT"

sshpass -p $HOST_PASSWORD ssh $HOST_USERNAME@$HOST_IP
# -o StrictHostKeyChecking=no 



