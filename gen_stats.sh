#!/bin/bash
dir='/var/www/html'
cd "$dir"
/usr/bin/cat /var/log/syslog.1 | grep "New block" | awk '{gsub(/,/, "", $13); gsub(/,/, "", $15); gsub("/.*", "", $13); gsub("ms", "", $15); print $13, $15}' | awk '{gsub("txs=", ""); gsub("t=", ""); print}' > "$dir"/data.txt
/usr/bin/python3 "$dir"/main.py

