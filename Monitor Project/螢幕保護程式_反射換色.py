import cv2
import numpy as np
import random
from random import choice

def run(forward,x1,y1,x2,y2,color):
    if forward==1:
        show(x1,y1,x2,y2,color)
        num = a(x1,y1,x2,y2)
        if num==3:
            forward=2
        elif num == 2:
            forward=4
        else:
            x1+=1
            y1+=1
            x2+=1
            y2+=1
    # 右上        
    elif forward==2:
        show(x1,y1,x2,y2,color)
        num = a(x1,y1,x2,y2)
        if num == 1:
            forward=1
        elif num == 2:
            forward=3
        else:
            x1+=1
            y1-=1
            x2+=1
            y2-=1
    # 左上        
    elif forward==3:  
        show(x1,y1,x2,y2,color)
        num = a(x1,y1,x2,y2)
        if num == 0:
            forward=2
        elif num == 1:
            forward=4
        else:
            x1-=1
            y1-=1
            x2-=1
            y2-=1
    #左下       
    elif forward==4:   
        show(x1,y1,x2,y2,color)
        num = a(x1,y1,x2,y2)
        if num == 0:
            forward=1
        elif num == 3:
            forward=3
        else:
            x1-=1
            y1+=1
            x2-=1
            y2+=1
    return forward,x1,y1,x2,y2

def show(x1,y1,x2,y2,color):
    img = np.full((300, 500, 3), 255, np.uint8)    
    cv2.rectangle(img, (x1,y1), (x2,y2), color, -1)
    cv2.imshow("",img)
    
def a(x1,y1,x2,y2):
    if x1<0:
        return 0
    elif y1<0:
        return 1
    elif x2>500:
        return 2
    elif y2>300:
        return 3

# 邊線 0 0 300 500
ppp = random.randint(50,500)
ppy = random.randint(50,300)
(x1,y1),(x2,y2) = (ppp-50,ppy-50),(ppp,ppy)
forward = random.randint(1,4)
r = random.randint(0,255)
b,g,r = (255,0,0)
color=[b,g,r]
i=0

while True:

    
    chance = forward
    forward,x1,y1,x2,y2 = run(forward,x1,y1,x2,y2,color)
    
    if chance!=forward:
        b = [0,1,2]
        ch_co = color.index(255)
        b.remove(ch_co)
        color[choice(b)]=255
        color[ch_co]=0
        
    if cv2.waitKey(1) >0:
        break
        


cv2.destroyAllWindows()
