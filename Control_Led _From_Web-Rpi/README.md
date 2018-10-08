Controlling Raspberry Pi LEDs through Web

In this project, I’ll demonstrate controlling couple of LEDs connected to Raspberry Pi GPIO from Web. LEDs could be replaced with any devices so its a kind of basic IoT project too, so this core design can be extended to any scale and many devices can be controlled simultaneously. Programming is done in Python and for web interface I have used bottle framework and jQuery Mobile.

Complete post is available at http://rizwanansari.net/control-raspberry-pi-leds-from-web-and-mobile/


#Install bootle

For Python 2.7
```
sudo pip install bottle
```
For Python 3
```
sudo pip3 install bottle
```
#Connection
Refer Rpi GPIO Pin Configuration to find the GPIO pin number

-Connect postive of red led in GPIO24 and yellow in GPIO23
-Ground the both negative terminal to ground pin Rpi
