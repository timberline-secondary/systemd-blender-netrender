#!/bin/sh
# credits: https://stackoverflow.com/a/12748070/2700631
# /usr/local/bin/netrender-watchdog

check_master()
{
  URL=$1
  http_status=$(curl -sL -w "%{http_code}\\n" "$URL" -o /dev/null)
  if [ $http_status != "200" ]; then
    echo "$URL did not return 200.  Is the Master running?"
    exit 1
  fi
}

# Check if a user is logged on locally (via tty),  Will ignore ssh connections.
# Might need to change for other distros.
check_user()
{
  if who | grep tty  > /dev/null 2>&1; then
    echo "A user has logged in locally. I'm outta here!"
    exit 1
  fi
}

#main
while :
do
  check_master $1
  check_user
  sleep 5
done

