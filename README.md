# systemd-blender-netrender
A collection of scripts and [systemd](https://wiki.debian.org/systemd) units to manage a Blender netrender "farm" in an active Linux computer lab.

The goal of this repo is to allow a computer lab's currently unused computers to be added as rendering slaves for Blender's netrender. For example, I teach in a high school computer lab with 30 student workstations, where several of them may be unused in any particular class, and only a few are used outside of scheduled classes.  The goal is to utilize these unused computers automagically as netrender slaves for students working with Blender.  When a user logs in to one of the workstations, that specific slave needs to stop, then start slaving  again when the user logs out.  If the master crashes or reboots, the slaves should stop, then restart when the master is running again.

Here's the general process, if you imagine booting up a classroom computer lab in the morning:
1. The Blender netrender master starts as a systemd service on whatever single server/workstation you want to be master.
1. All other workstations run a service (netrender-watchdog) that watches for a locally logged in user, and for the availability of the master on the local network (via the Master Monitor page), 
1. If no one is logged in to the workstation, and the Master Monitor is detected, the slave starts up.
1. If a user logs in or the master goes down, the slave service stops.
1. When the user logs out of the workstation the slave will start again, if the master is up.

## Installation of Slaves

1. Download the watchdog python script and make it executable:

````
sudo wget https://raw.githubusercontent.com/timberline-secondary/systemd-blender-netrender/master/netrender-watchdog.py -N /usr/local/bin/
sudo chmod +x /usr/local/bin/netrender-watchdog.py
````

2. Create a Blnder netrender slave, and save it to: `/usr/local/share/netrender/slave.blend` or download the one form this repo (for Blender 2.76, migth not work with newer versions of blender...)

````
sudo mkdir /usr/local/share/netrender
sudo wget https://github.com/timberline-secondary/systemd-blender-netrender/blob/master/slave2.76.blend -N /usr/local/share/netrender/slave.blend
````

3. Install the services:

3.1 Download watchdog service

````
sudo wget https://github.com/timberline-secondary/systemd-blender-netrender/blob/master/netrender-watchdog.service -N /etc/systemd/system/
````

3.2. Open the file and on this line, change the host to match your master:

````
ExecStart= /usr/bin/env python3 /usr/local/bin/netrender-watchdog.py --host IP_OR_HOSTNAME:PORT
````

3.3 Download the slave service

````
sudo wget https://github.com/timberline-secondary/systemd-blender-netrender/blob/master/netrender-slave.service -N /etc/systemd/system/
````

3.4 Enable the watchdog service to start on boot, and start it

````
sudo systemctl enable netrender-watchdog.service
sudo systemctl start netrender-watchdog.service
````

