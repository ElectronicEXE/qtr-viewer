import pygame, sys
from pygame.locals import *
import serial

# VERSION = 1.7

#################################################
Sensor_Count = 8

serial_port = 'COM21'

baud_rate = 115200
#################################################


ser = serial.Serial(serial_port, baud_rate, timeout=1)

ready = False

clist =[100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100]
cLlist =[100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100,100]

pos = 0


x = Sensor_Count * 71
if x < 300:
    x = 500
y = 150

def main():
    pygame_init(x,y)
 
    while True:

        serGet(ser)
        draw_text(DISPLAY, ready,cLlist, pos,x,Sensor_Count)
        draw_box(DISPLAY,clist, Sensor_Count)

        for event in pygame.event.get():
            if event.type==QUIT:
                pygame.quit()
                sys.exit()
        

def serGet(ser):
    data = ser.readline().decode('utf-8').strip()
    splitData = data.split(",")
    global cLlist,pos,ready,Sensor_Count
    try:
        ii = 0
        for i in range(Sensor_Count):
            cLlist[ii] = splitData[ii]
            ii = ii + 1
        pos = splitData[Sensor_Count]
        if len(splitData) != Sensor_Count+1:
            print(f"WARNING: SENSOR COUNT MISSMATCHING. programmed sensor count: {Sensor_Count} received sensor count: {len(splitData)-1}")
        setcolor()            
        ready = True
    except:
        print("not ready")
        print("calibration is still in progress .....................")
        ready = False

def translate(value, leftMin, leftMax, rightMin, rightMax):
    leftSpan = leftMax - leftMin
    rightSpan = rightMax - rightMin
    valueScaled = float(value - leftMin) / float(leftSpan)
    return rightMin + (valueScaled * rightSpan)

def setcolor():
    global clist,cLlist
    iii = 0
    for i in range(Sensor_Count):
        clist[iii] = int(translate(int(cLlist[iii]), 1000, 0, 0, 255))
        iii = iii +1


def draw_box(DISPLAY, clist, S_no):
        i = 0
        w = 10
        for i in range(S_no):
            rgb = clist[i], clist[i], clist[i]
            pygame.draw.rect(DISPLAY,rgb,(w,10,60,80))
            w = w+70

        pygame.display.update()   


def draw_text(DISPLAY, ready, cLlist, pos,x,S_no):
        white = 255,255,255
        BLACK=(30,30,50)
        font = pygame.font.SysFont("Arial", 30)
        font2 = pygame.font.SysFont("Arial", 15)
        if ready ==True:
            text = font.render("                   position:  " + str(pos) + "                    ", True, white,BLACK)
        else:
            text = font.render("calibration is still in progress ...", True, white,BLACK)

        textRect = text.get_rect()
        textRect.center = (x/2 , 130 )
        i = 0
        w = 40
        for i in range (S_no):
            
            text1 = font2.render("  " + str(cLlist[i]) + "  ", True, white,BLACK)
            textRect1 = text1.get_rect()
            textRect1.center = (w ,100 )
            DISPLAY.blit(text1,textRect1)
            w = w + 70
        

       
        DISPLAY.blit(text,textRect)



def pygame_init(x,y):
    pygame.init()
    global DISPLAY
    DISPLAY=pygame.display.set_mode((x,y),0,32)
    BLACK=(30,30,50)
    DISPLAY.fill(BLACK)
    pygame.display.set_caption('QTR-viewer')

if __name__ == '__main__':
    main()
