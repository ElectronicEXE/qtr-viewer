import pygame, sys
from pygame.locals import *
import serial
import threading
import time

serial_port = 'COM21'
baud_rate = 9600
ser = serial.Serial(serial_port, baud_rate, timeout=1)


c1 = 100
c2 = 100
c3 = 100
c4 = 100
c5 = 100
c6 = 100
c7 = 100
c8 = 100

pos = 0

white = 255,255,255

def main():
    pygame.init()
    
    
    DISPLAY=pygame.display.set_mode((570,150),0,32)

    BLACK=(30,30,50)

    DISPLAY.fill(BLACK)

 
    while True:
        font = pygame.font.SysFont("Arial", 30)
        text = font.render("   position:  " + str(pos) + "    ", True, white,BLACK)
        textRect = text.get_rect()
        textRect.center = (285 , 130 )
        serGet()
        pygame.display.update()
        c1rgb = c1,c1,c1
        c2rgb = c2,c2,c2
        c3rgb = c3,c3,c3
        c4rgb = c4,c4,c4
        c5rgb = c5,c5,c5
        c6rgb = c6,c6,c6
        c7rgb = c7,c7,c7
        c8rgb = c8,c8,c8

        pygame.draw.rect(DISPLAY,c1rgb,(10,10,60,80))
        pygame.draw.rect(DISPLAY,c2rgb,(80,10,60,80))
        pygame.draw.rect(DISPLAY,c3rgb,(150,10,60,80))
        pygame.draw.rect(DISPLAY,c4rgb,(220,10,60,80))
        pygame.draw.rect(DISPLAY,c5rgb,(290,10,60,80))
        pygame.draw.rect(DISPLAY,c6rgb,(360,10,60,80))
        pygame.draw.rect(DISPLAY,c7rgb,(430,10,60,80))
        pygame.draw.rect(DISPLAY,c8rgb,(500,10,60,80))
        DISPLAY.blit(text,textRect)

        for event in pygame.event.get():
            if event.type==QUIT:
                pygame.quit()
                sys.exit()
        

def serGet():
    data = ser.readline().decode('utf-8').strip()
    splitData = data.split(",")
    global c1l,c2l,c3l,c4l,c5l,c6l,c7l,c8l,pos
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
    except:
        print("not ready")
        print("calibratione is still in progress .....................")


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

if __name__ == '__main__':
    main()