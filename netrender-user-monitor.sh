#!/bin/sh

while true
do
  # If Xorg is running, then a user has logged in to the GUI.  `pidof Xorg` Works for Ubuntu's X server. 
  # Might need to change for other distros. A more universal method of checking would be nice.
  if pidof Xorg > /dev/null 2>&1; then
    echo "X window server found.  User has logged in to GUI. I'm outta here!"
    exit 0
  fi
  sleep 1
done
