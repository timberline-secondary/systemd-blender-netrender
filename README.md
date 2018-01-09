# blender-netrender-slave-service
A [systemd](https://wiki.debian.org/systemd) unit to start a Blender netrender slave


## How to use
#### Create slave.blend
1. Create a netrender slave named `slave.blend` with the settings you want (use the [Blender Netrender Additions](https://github.com/WARP-LAB/Blender-Network-Render-Additions) fork to render with GPU on slaves)
1. Save the file to `/opt/netrender-startup` or another location of your choice.  If you change the location, you'll need to edit `WorkingDirectory` in the the unit file `netrender-slave.service`

#### Install the Systemd Unit
1. Move to install dir:`cd /etc/systemd/system/`
1. Download: `sudo wget https://raw.githubusercontent.com/timberline-secondary/blender-netrender-slave-service/master/netrender-slave.service`
1. Ensure it has correct permissions: `sudo chmod 664 /etc/systemd/system/netrender-slave.service`
1. Inform systemd of the new service: `sudo systemctl daemon-reload`
1. To start the service when the computer boots: `sudo systemctl enable netrender-slave`
1. To start the service manually: `sudo systemctl start netrender-slave`
1. To check the status or restart or stop the service, replace `start` with `status`, `restart`, or `stop` `
