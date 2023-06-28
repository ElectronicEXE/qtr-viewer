import pygame, sys
from pygame.locals import *
import serial
from draw import *

serial_port = 'COM21'
baud_rate = 9600

ser = serial.Serial(serial_port, baud_rate, timeout=1)

ready = False

c1 = 100
c2 = 100
c3 = 100
c4 = 100
c5 = 100
c6 = 100
c7 = 100
c8 = 100

c1l = 100
c2l = 100
c3l = 100
c4l = 100
c5l = 100
c6l = 100
c7l = 100
c8l = 100

pos = 0

def main():
    pygame_init()
 
    while True:

        serGet(ser)
        draw_text(DISPLAY, ready, c1l, c2l, c3l, c4l, c5l, c6l, c7l, c8l, pos)
        draw_box(DISPLAY, c1, c2, c3, c4, c5, c6, c7, c8)

        for event in pygame.event.get():
            if event.type==QUIT:
                pygame.quit()
                sys.exit()
        

def serGet(ser):
    data = ser.readline().decode('utf-8').strip()
    splitData = data.split(",")
    global c1l,c2l,c3l,c4l,c5l,c6l,c7l,c8l,pos,ready
    try:
        c1l = splitData[0]
        c2l = splitData[1]
        c3l = splitData[2]
        c4l = splitData[3]
        c5l = splitData[4]
        c6l = splitData[5]
        c7l = splitData[6]
        c8l = splitData[7]
        pos = splitData[8]
        setcolor()            
        ready = True
    except:
        print("not ready")
        print("calibratione is still in progress .....................")
        ready = False

def translate(value, leftMin, leftMax, rightMin, rightMax):
    leftSpan = leftMax - leftMin
    rightSpan = rightMax - rightMin
    valueScaled = float(value - leftMin) / float(leftSpan)
    return rightMin + (valueScaled * rightSpan)

def setcolor():
    global c1,c2,c3,c4,c5,c6,c7,c8
    c1 = int(translate(int(c1l), 1000, 0, 0, 255))
    c2 = int(translate(int(c2l), 1000, 0, 0, 255))
    c3 = int(translate(int(c3l), 1000, 0, 0, 255))
    c4 = int(translate(int(c4l), 1000, 0, 0, 255))
    c5 = int(translate(int(c5l), 1000, 0, 0, 255))
    c6 = int(translate(int(c6l), 1000, 0, 0, 255))
    c7 = int(translate(int(c7l), 1000, 0, 0, 255))
    c8 = int(translate(int(c8l), 1000, 0, 0, 255))
    return c1,c2,c3,c4,c5,c6,c7,c8


def pygame_init():
    pygame.init()
    global DISPLAY
    DISPLAY=pygame.display.set_mode((570,150),0,32)
    BLACK=(30,30,50)
    DISPLAY.fill(BLACK)

if __name__ == '__main__':
    main()