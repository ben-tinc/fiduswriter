#!/bin/bash
# 
# Based on the similar script at https://www.conftool.net/ctforum/index.php/topic,281.0.html

URL="https://www.conftool.net/demo/dhdtest_26j/rest.php"
USER="gebhard"
USER_FILE="./user_$USER._new.xml"
PASSWORD="PF3fuZhQu"

NONCE=`date +%s`
PASSHASH=`echo -n "$NONCE$PASSWORD" | sha256sum | awk '{print $1;}'`

param="page=remoteLogin"
param+="&command=request"
param+="&nonce=$NONCE"
param+="&passhash=$PASSHASH"
param+="&user=$USER"

echo "$URL$param"
curl --silent --request POST $URL --data "$param" --output $USER_FILE 
