# systemd-blender-netrender
A collection of scripts and [systemd](https://wiki.debian.org/systemd)  units to manage a Blender netrender "farm" in an active Linux computer lab.

The goal of this repo is to allow a computer lab's currently unused computers to be added as rendering slaves for Blender's netrender. For example, I teach in a high school computer lab with 30 student workstations, where several of them may be unused in any particular class, and only a few are used outside of schedule classes.  The goal is to utilize these unused compuiters automagically as netrender slaves for students working with Blender.  When a user logs in to one of the workstations, that specific slave needs to stop, then start slaving  again when the user logs out.  If the master crashes or reboots, the slaves should stop, then restart when the master is running again.

Here's the general process, if you imagine booting up a classroom computer lab in the morning:
1. The Blender netrender master starts as a systemd service on whatever single server/workstation you want to be master.
1. All other workstations run a service (netrender-monitor) that watches for the availability of the Master Monitor page on the local network.
1. When the Master Monitor is detected, the slaves startup.
1. The slave workstations also run a service (netrender-user-monitor) that monitors for users logging in to the workstation via GUI (an ssh connection won't trigger this)
1. If a user logs in, the slave service stops.
1. When the user logs out of the workstation, this will be detected (5 minute polling interval), this will trigger the slave service to start again.
1. If the Mastor Monitor becomes unavailable (master crash, reboot, netowrk issues), this will be detected and trigger the slave to stop.  it will start again once the Master Monitor page is reachable again.

******************** OLD STUFF BELOW ***********************

## How to Setup a Slave Service
#### Create slave.blend
1. Create a netrender slave named `slave.blend` with the settings you want (use the [Blender Netrender Additions](https://github.com/WARP-LAB/Blender-Network-Render-Additions) fork to render with GPU on slaves)
1. Save the file to `/opt/netrender-slave` or another location of your choice.  If you change the location, you'll need to edit `WorkingDirectory` in the the unit file `netrender-slave.service`

#### Install the Systemd Unit
1. Move to install dir:
`cd /etc/systemd/system/`
1. Download: 
`sudo wget https://raw.githubusercontent.com/timberline-secondary/blender-netrender-service/master/netrender-slave.service`
1. Ensure it has correct permissions: 
`sudo chmod 664 /etc/systemd/system/netrender-slave.service`
1. Inform systemd of the new service: 
`sudo systemctl daemon-reload`
1. To start the service when the computer boots: 
`sudo systemctl enable netrender-slave`
1. To start the service manually: 
`sudo systemctl start netrender-slave`
1. To check the status or restart or stop the service, replace `start` with `status`, `restart`, or `stop`


## How to Setup a Master Service

Todo...
