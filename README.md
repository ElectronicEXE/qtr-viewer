# qtr-viewer
Python program to read data from pololu qtr and qtrx sensors and display the read values by colors.

This program is very useful when building a line follower robot or testing different sensors.

By default, the program is configured to read from the QTR-MD-8A at 115200 baud rate on COM21 but this can be changed in the code.

The program works with up to 32 sensors.

To change the baud rate, serial port, and sensor count edit lines 8, 10, and 12
![image](https://github.com/ElectronicEXE/qtr-viewer/assets/114730703/0d131d03-4ca8-4419-9738-162bec91f5d2)


Required Python libraries:
- pygame
- serial

Required Arduino libraries:
- QTRSensors

To use the program you need to connect the array of sensors to an Arduino board and upload the Arduino code on it.
Then open QTR-viewer and the calibration will start immediately. Once the sensors are calibrated you can start viewing the sensor data.
![image](https://github.com/ElectronicEXE/qtr-viewer/assets/114730703/53681632-d6fb-4c05-aefc-bf8fb5227e28)


![image](https://github.com/ElectronicEXE/qtr-viewer/assets/114730703/611b3443-d27f-44df-9795-c8147be4529e)


![image](https://github.com/ElectronicEXE/qtr-viewer/assets/114730703/c806fc74-77b0-4f19-a156-8aa5caa83507)



