#!/bin/sh

while true
do
  # Check if a user is logged on locally (via tty),  Will ignore ssh connections.
  # Might need to change for other distros. 
  if who | grep tty  > /dev/null 2>&1; then
    echo "User has logged in locally. I'm outta here!"
    exit 0
  fi
  sleep 1
done

