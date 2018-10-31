# Run IDLE at Start
For some cases, crontab,system md service and other alternatives fails to run your program.
It may require some display environment .i.e need to run at python shell. When you run your script at terminal, your program just run in terminal itself.

- My case is
    - I run a python program that has a callback. Callback lives only when the kernal is alive. If you run it on pyhton IDLE, it will open python shell and run it. Kernal stays alive until you close the shell.
    - But if you run a python program in terminal, it will run the program and the kernal shut down after executing the program.This literally means your callback has died. That's bad for me
    - Every alternatives for start your program at bootup run the program on terminal

I 'll explain how I solved this issue.
- I need to run program in idle rather than at terminal and you can do this by,<br><br>

How usually we do
```
python3 myprogram.py
```
Instead
```
idle myprogram.py
```
or 
```
idle3 myprogram.py
```
- Now I need to run this command at bootup. If you directly run this command at bootup. I ended up with same issue because you won't be able run idle when the system is booting up.
- So, it should run IDLE after rasperry pi finishes its bootup process. Just like Chrome launches on Windows machine when we log in (If you preset this operation).

- Before that you should write your command in sh file. Here's how you can write sh file.
Create a file and paste this content save it in .sh format. I saved it as launcher.sh

```
#!/bin/bash
idle3 -r /home/pi/myprogram.py
```
- Final step

For current Rasbian builds:
```
sudo nano ~/.config/lxsession/LXDE-pi/autostart
```
Add the following line, and then save the file:
```
@sh /home/pi/launcher.sh
```
Or if you want a terminal window also, for debugging:
```
@lxterminal --command='sh /home/pi/launcher.sh'
```
Paste both the lines, if you're not sure what you want.