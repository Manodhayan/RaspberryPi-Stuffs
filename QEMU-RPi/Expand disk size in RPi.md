# Expand disk size in RPi Image


```
fdisk <imagefile>
```
- Enter P to display all partition
- Note the start sector of the partition you want to expand
- d - delete the partition of your interest
- n - Create new partition
- Enter your preferred partition number and selct primary partition
- Input your deleted start sector to this partiotion
- Press Enter on the end. By default total memory will be allocated for that partition
- Make sure you don't remove the ext4 signature, if it prompts.
- w - to write the changes you made to the image

do this all in any linux platform not on the emulated raspian.

That's it. You are done

