# Boot IDLE at Start
For some cases, crontab,system md service and other alternatives fails to run your program.
It may require some display environment.

Or for current Rasbian builds:

sudo nano /etc/xdg/lxsession/LXDE-pi/autostart
Add the following line, and then save the file:

@sh /home/pi/launcher.sh
Or if you want a terminal window also, for debugging:

@lxterminal --command='sh /home/pi/launcher.sh'