# G27-Shifter-USB-adapter-with-arduino-nano
Project to adapt an G27 shifter to USB using an arduino nano 

So, the title is actually prety self explanatory on the main goal of this project.
The focus of the project is the arduino nano board, and an workaround to make it work as a keyboard, even without it's HID capabilities.
I will describe each part of the process and the requirements to it, on my perspective of what I did to complete it.

## Requirements

The requirements are actually pretty simples:

+ A G27 shifter (of course)
+ A DB9 male connector
+ An Arduino Nano board (which is the focus of this project)
 
Regarding the arduino board, you can choose most of them, it would be a lot easier if you choose one with HID capabilities (there are other repositories explaining in further detail how to make those work), which is not our case.

## Wiring diagram

So, the first step is to connect the db9 connector to the arduino board.
For the G27 shifter I used the following wiring diagram: 
(image of wiring diagram)

I had some problems on this step, but I'm not entirely sure that this is a arduino nano problem or if it is just my board that is faulty, but I will documment this problem, so that if happens with you, you can try to fix it!

### Wiring and Analog reading problem

You can actually read about in more detail here: https://forum.arduino.cc/t/problems-with-analog-pin-on-nano/1184291/38
But I will try to speak a little about it here.

So, my arduino board wasn't really being able to read the A3 pin correctly, it was always returning the maximum value possible, so I started measuring everything with my voltmeter, leading me to discover that my analog port was not connected to this chip on the Nano:
(chip image)

So, I did an direct connection with a wire on the analog port I would use, to the respective pin on the chip. (I found out which one measuring the voltage with the voltmeter on each pin on the chip).
Just to register, I thoght the chip to the A3 pin, was this one:
(imagem da porta circulada)

It turns out that it worked, but for some reason, the arduino was getting the values from the two analog info pins from the db9 on the same analog pin, so I did another direct connection with a wire, but this time, I used the IC pin 17
(imagem do chip com a numeração la)

So the direct connection looks like somethin like this:
(imagem da conexão direta)

That solved the issue with the faulty reading for my board.

## Arduino Sketch and Pyhton script

Both can be found on it's respective folders, you just have to upload the arduino sketch to your nano, and modify the pyhton script with your Arduinos port name (for example /dev/cu.usbmodem1461).
You can modify both of them to fit your porpouse, the code is pretty simple and with comments to guide you on undestanding it.

And that's it, I hope this project can help those who are looking for a real cheap solution to adapt their G27 shifter to usb!
Good luck!







