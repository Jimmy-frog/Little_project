import cv2
import numpy as np
import random


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
    
    
    while color[(i+1)%3]<255:
        color[(i+1)%3]+=1
        forward,x1,y1,x2,y2 = run(forward,x1,y1,x2,y2,color)
        if cv2.waitKey(1) >0:
            break

    while color[i%3]>0:
        color[i%3]-=1
        forward,x1,y1,x2,y2 = run(forward,x1,y1,x2,y2,color)
        if cv2.waitKey(1) >0:
            break

#     forward,x1,y1,x2,y2 = run(forward,x1,y1,x2,y2)
    i+=1
    if cv2.waitKey(1) >0:
        break 


cv2.destroyAllWindows()