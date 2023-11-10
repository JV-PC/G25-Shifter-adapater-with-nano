import serial
import pyautogui

arduino = serial.Serial('COM3', 2400, timeout=.5) # acquiring the data from the serial port (you can serach for the Pyserial library to more info on this)

pyautogui.PAUSE = 0


while True:
    data = arduino.readline() # reading the serial data sent from the arduino to the seral port
    rawdata = str(data.decode("utf-8", "strict")) # decoding the data to utf
    pdata = rawdata.split(',') # splitting the string into a list, so that we can get each individual value
    length=len(pdata) # getting the lenght of the list so that we can be sure when we are getting the values we really want
    if length == 3: 
        # Assigning each key to it's respective gear on the shifter, based on the serial value that it's given by the potentiometer on the shifter.
        if((int(pdata[0])<2450 and int(pdata[0])>2210) and (int(pdata[1])<2300 and int(pdata[1])>1680)): 
            pyautogui.keyDown('q')
        if((int(pdata[0])<2270 and int(pdata[0])>2100) and (int(pdata[1])<4100 and int(pdata[1])>3200)): 
            pyautogui.keyDown('1')
        if((int(pdata[0])<2270 and int(pdata[0])>2100) and (int(pdata[1])<650 and int(pdata[1])>140)): 
            pyautogui.keyDown('2')
        if((int(pdata[0])<2450 and int(pdata[0])>2210) and (int(pdata[1])<4095 and int(pdata[1])>3350)): 
            pyautogui.keyDown('3')
        if((int(pdata[0])<2450 and int(pdata[0])>2210) and (int(pdata[1])<650 and int(pdata[1])>140)): 
            pyautogui.keyDown('4')
        if((int(pdata[0])<2600 and int(pdata[0])>2500) and (int(pdata[1])<4095 and int(pdata[1])>3350)): 
            pyautogui.keyDown('5')
        if((int(pdata[0])<2560 and int(pdata[0])>2510) and (int(pdata[1])<650 and int(pdata[1])>140)): 
            pyautogui.keyDown('6')
            




