import cv2
import numpy as np
import random


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

# ?? 0 0 300 500

ppp = random.randint(0,250)
(x1,y1),(x2,y2) = (ppp,ppp+50),(ppp+50,ppp+100)
forward = random.randint(1,4)
r = random.randint(0,255)
color = (x1/300*200,x2/300*255,r)
while True:
    color = (255,0,0)
#     color = ((x2/300+y2/500)/2*255,255)
    # ??
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
    # ??        
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
    # ??        
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
    #??       
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
        
        

    if cv2.waitKey(1) >0:
        break
        


cv2.destroyAllWindows()
