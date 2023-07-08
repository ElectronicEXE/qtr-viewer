# qtr-viewer
Python program to read data from pololu qtr and qtrx sensors and display the read values by colors.

This program is very useful when building a line follower robot or testing different sensors.

By default, the program is configured to read from the QTR-MD-8A at 115200 baud rate on COM21 but this can be changed in the code.

The program works with up to 32 sensors.

To change the baud rate, serial port, and sensor count edit lines 8, 10, and 12
![249743479-0d131d03-4ca8-4419-9738-162bec91f5d2](https://github.com/ElectronicEXE/qtr-viewer/assets/114730703/d59ab4d5-27a0-44bd-96fe-39eefb36ad01)


Required Python libraries:
- pygame
- serial

Required Arduino libraries:
- QTRSensors

To use the program you need to connect the array of sensors to an Arduino board and upload the Arduino code on it.
Then open QTR-viewer and the calibration will start immediately. Once the sensors are calibrated you can start viewing the sensor data.


![249824250-449063ba-32df-4090-8e3c-339d7c318e9f](https://github.com/ElectronicEXE/qtr-viewer/assets/114730703/235f82dc-13c1-4115-a144-e0da6941e09f)


![249825555-e9f68d98-a088-480c-b552-74379aa19970](https://github.com/ElectronicEXE/qtr-viewer/assets/114730703/335cc2c1-8f51-4ff9-a10b-8ec841eebc8e)


![249449169-611b3443-d27f-44df-9795-c8147be4529e](https://github.com/ElectronicEXE/qtr-viewer/assets/114730703/2d499a38-5baf-4ef6-a713-d7d9590be3f8)


![249745344-c806fc74-77b0-4f19-a156-8aa5caa83507](https://github.com/ElectronicEXE/qtr-viewer/assets/114730703/187d79c6-f325-4cff-af28-8f700f94046f)
