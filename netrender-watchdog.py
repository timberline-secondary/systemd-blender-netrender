#!/usr/bin/env python3
import argparse
import time
import subprocess
from urllib import request
from urllib.error import URLError


def master_is_running(host="suzanne:8001", use_ssl=False):
    """
    Determines whether a Blender netrender master is running on the local network.
    Currently, it does this by looking to see if the Master Monitor webpage is being
    served by the master.
    :param host: where to find the master.  IP or hostname plus port.
    :param use_ssl: if the master is using ssl
    :return: True if the Blender netrender master is running
    """
    protocol = "https" if use_ssl else "http"
    master_monitor_url = "{protocol}://{host}".format(**locals())
    try:
        response = request.urlopen(master_monitor_url)
    except URLError:
        print("Blender netrender master not found at: {master_monitor_url}".format(**locals()))
        return False
    else:
        if response.code != 200:
            print("Blender netrender master error. HTTP response: {}".format(response))
            return False
    print(master_monitor_url)
    return True


def user_is_logged_in():
    """
    Checks if a user is logged on locally.
    Currently this is done by checking the results of the `who` command and
    Searching for a native terminal device (tty).  SSH connections (pts) won't count.
    Probably not a very robust way of doing this, but works for me!
    :return: True if a user is logged in locally.
    """
    who = subprocess.run(['who'], stdout=subprocess.PIPE, universal_newlines=True)
    if who.stdout.find("tty") == -1:
        return False
    else:
        print("A user is logged in locally: {}".format(who.stdout))
        return True
        

if __name__ == "__main__":  # if this script is run form the command line
    parser = argparse.ArgumentParser()
    parser.add_argument("--host", help="The master's ip or hostname and port")
    parser.add_argument("--ssl", help="The master is using ssl", action="store_true")
    args = parser.parse_args()

    kwargs = {}
    if args.host:
        kwargs['host'] = args.host
    if args.ssl:
        kwargs['use_ssl'] = True

    while not user_is_logged_in() and master_is_running(**kwargs):
        time.sleep(5)
