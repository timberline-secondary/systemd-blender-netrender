#!/bin/sh
# credits: https://stackoverflow.com/a/12748070/2700631

check_master()
{
  URL=$1
  http_status=`curl -sL -w "%{http_code}\\n" "$URL" -o /dev/null`
  #echo $http_status
  if [ $http_status != "200" ]
  then
    echo "$URL did not return 200.  Is the Master running?"
    exit 1
  fi
}

#main
while :
do
  check_master $1
  sleep 5
done
