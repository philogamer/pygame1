import pygame
import random
import math

pygame.init()
pygame.mixer.init()
screen=pygame.display.set_mode((1500,750))
pygame.display.set_caption('Lost Soul')
stage='map'
clock=pygame.time.Clock()


class Map:
    def __init__(self,xy,type):
        position=xy
        self.y=xy%10*75
        self.x=(xy-xy%10)/10*75
        if type=='W':
            self.img='assets/wall.png'
        elif type=='CL':
            self.img='assets/CL.png'
        elif type=='CR':
            self.img='assets/CR.png'
        elif type=='CRL':
            self.img='assets/CRL.png'
        elif type=='F':
            gacha=random.randint(1,3)
            if gacha==1:
                self.img='assets/F1.png'
            elif gacha==2:
                self.img='assets/F2.png'    
            else:
                self.img='assets/F3.png'
        self.img=pygame.image.load(self.img).convert_alpha()
        self.img=pygame.transform.scale(self.img,(75,75))
    def draw(self,screen):
        screen.blit(self.img,(self.x,self.y))
class Obstacle:
    def __init__(self,xy,type):
        position=xy
        self.y=xy%10*75
        self.x=(xy-xy%10)/10*75
        if type=='V':
            self.img='assets/V.png'
        elif type=='SL':
            self.img='assets/SL.png'
        elif type=='SLR':
            self.img='assets/SLR.png'
        elif type=='SLRT':
            self.img='assets/SLRT.png'
        elif type=='SLT':
            self.img='assets/SLT.png'
        elif type=='SR':
            self.img='assets/SR.png'
        elif type=='ST':
            self.img='assets/ST.png'
        self.img=pygame.image.load(self.img).convert_alpha()
        self.img=pygame.transform.scale(self.img,(75,75))
        self.rect=pygame.rect(self.x,self.y,75,75)
    def draw(self,screen):
        screen.blit(self.img,(self.x,self.y))
class Player:
    def __init__(self,xy):
        position=xy
        self.y=xy%10*75
        self.x=(xy-xy%10)/10*75
        self.img='assets/main'
        self.img=pygame.image.load(self.img).convert_alpha()
        self.img=pygame.transform.scale(self.img,(40,77))
        self.rect=pygame.rect(self.x,self.y-(77-75),40,75)
    def draw(self,screen):
        screen.blit(self.img,(self.x,self.y))
class Creep:
    def __init__(self,xy,type):
        position=xy
        self.y=xy%10*75
        self.x=(xy-xy%10)/10*75
        self.img='assets/main'
        self.h=10
        self.w=10
        self.img=pygame.image.load(self.img).convert_alpha()
        self.img=pygame.transform.scale(self.img,(self.w,self.h))
        self.wallrect=pygame.rect(self.x,self.y-(self.h-75),self.w,75)
        self.rect=pygame.rect(self.x,self.y,self.w,self.h)
    def draw(self,screen):
        screen.blit(self.img,(self.x,self.y))
rendermap=True
firstdoor=[]  #for save the door for next map
f=[]
door=[]
w=[]
sr=[]
sl=[]
v=[]
cl=[]
cr=[]
crl=[]
slr=[]
slrt=[]
slt=[]
st=[]
#Game loop
while True:
    dt=clock.tick(60)/1000
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            quit(0)
        keys=pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            rendermap=True
    #random map logic
    if rendermap:
        locate=list(range(200))
        f.clear()
        door.clear()
        w.clear()
        sr.clear()
        sl.clear()
        v.clear()
        cl.clear()
        cr.clear()
        crl.clear()
        slr.clear()
        slrt.clear()
        slt.clear()
        st.clear()
        if not firstdoor:
            doorlong=random.randint(1,5)
            doorside=random.choice([-1,1,-2,2])
            firstdoor.append(doorside)
            firstdoor.append(doorlong)
            if doorside==(-1):
                firstexactdoor=random.choice(list(range(19,189+1-doorlong*10,10)))
                firstdoor.append(firstexactdoor)                
                for i in range(0,doorlong):   
                    f.append(Map(firstexactdoor+i*10,'F'))
                    locate.remove(firstexactdoor+i*10)
                    door.append(firstexactdoor+i*10)
            elif doorside==(1):
                firstexactdoor=random.choice(list(range(10,180+1-doorlong*10,10))) 
                firstdoor.append(firstexactdoor)
                for i in range(0,doorlong):
                    f.append(Map(firstexactdoor+i*10,'F'))
                    locate.remove(firstexactdoor+i*10)
                    door.append(firstexactdoor+i*10)    
            elif doorside==(2):
                firstexactdoor=random.choice(list(range(1,8+1-doorlong)))
                firstdoor.append(firstexactdoor)
                for i in range(0,doorlong):
                    f.append(Map(firstexactdoor+i,'F'))
                    locate.remove(firstexactdoor+i)
                    door.append(firstexactdoor+i)                
            elif doorside==(-2):
                firstexactdoor=random.choice(list(range(191,198+1-doorlong)))
                firstdoor.append(firstexactdoor)
                for i in range(0,doorlong):
                    f.append(Map(firstexactdoor+i,'F'))
                    locate.remove(firstexactdoor+i)
                    door.append(firstexactdoor+i)
        else:
            doorlong=firstdoor[1]
            doorside=firstdoor[0]*(-1)
            if doorside==(-1):
                firstexactdoor=random.choice(list(range(19,189+1-doorlong*10,10)))   
                for i in range(0,doorlong):   
                    f.append(Map(firstexactdoor+i*10,'F'))
                    locate.remove(firstexactdoor+i*10)
                    door.append(firstexactdoor+i*10)
            elif doorside==(1):
                firstexactdoor=random.choice(list(range(10,180+1-doorlong*10,10)))
                for i in range(0,doorlong):
                    f.append(Map(firstexactdoor+i*10,'F'))
                    locate.remove(firstexactdoor+i*10)
                    door.append(firstexactdoor+i*10)    
            elif doorside==(2):
                firstexactdoor=random.choice(list(range(1,8+1-doorlong)))
                for i in range(0,doorlong):
                    f.append(Map(firstexactdoor+i,'F'))
                    locate.remove(firstexactdoor+i)
                    door.append(firstexactdoor+i)                
            elif doorside==(-2):
                firstexactdoor=random.choice(list(range(191,198+1-doorlong)))
                for i in range(0,doorlong):
                    f.append(Map(firstexactdoor+i,'F'))
                    locate.remove(firstexactdoor+i)
                    door.append(firstexactdoor+i)

        start=random.choice(door)
        doorban=[]
        c=0
        doorban.extend([0,9,190,199])
        if doorside==1:
            start+=1
            doorban.extend(list(range(10,190,10)))
        elif doorside==-1:
            start-=1
            doorban.extend(list(range(19,199,10)))
        elif doorside==2:
            start+=10
            doorban.extend(list(range(1,9)))
        else:
            start-=10
            doorban.extend(list(range(191,199)))
        f.append(Map(start,'F'))    
        locate.remove(start)
        doorban.extend(door)            
        c=0
        doorside=0
        doorlong=0
        startablefloor=[]
        firstdoor=[]
        door=[]
        while True:    
            while True:
                unablemeetagain=False
                if c!=0:
                    a.remove(c)
                else:
                    if doorside==1 and start in list(range(10,190,10)):
                        a=[1,10,-10]
                    elif doorside==-1 and start in list(range(19,199,10)):
                        a=[-1,10,-10]
                    elif doorside==2 and start in list(range(1,9)):
                        a=[1,10,-1]
                    elif doorside==-2 and start in list(range(191,199)):
                        a=[1,-1,-10]
                    else:
                        a=[1,-1,10,-10]
                if len(a)==0:
                    break
                b=random.choice(a)
                if (doorside==1 and not start in list(range(10,190,10))) or (doorside==-1 and not start in list(range(19,199,10))) or (doorside==2 and not start in list(range(1,9))) or (doorside==-2 and not start in list(range(191,199))):
                    unablemeetagain=True
                if (start+b) in locate and not (start+b) in doorban:
                    side=0
                    c=0
                    d=list(range(1,9))+list(range(10,190,10))+list(range(19,199,10))+list(range(191,199))
                    if (start+b) in d:
                        if (start+b) in list(range(1,9)):
                            if doorside==0: 
                                doorside=2
                            elif doorside!=2:                            
                                break
                            elif unablemeetagain:
                                break
                            else:
                                doorlong+=1
                            if doorlong==5:
                                break
                            side=1
                        elif (start+b) in list(range(10,190,10)):
                            if doorside==0: 
                                doorside=1
                            elif doorside!=1:                             
                                break
                            elif unablemeetagain:
                                break
                            else:
                                doorlong+=1
                            if doorlong==5:
                                break
                            side=1
                        elif (start+b) in list(range(19,199,10)):
                            if doorside==0: 
                                doorside=-1
                            elif doorside!=(-1):                          
                                break
                            elif unablemeetagain:
                                break
                            else:
                                doorlong+=1
                            if doorlong==5:
                                break
                            side=1
                        elif (start+b) in list(range(191,199)):
                            if doorside==0: 
                                doorside=-2
                            elif doorside!=(-2):
                                break
                            elif unablemeetagain:
                                break
                            else:
                                doorlong+=1
                            if doorlong==5:
                                break
                            side=1
                    start+=b
                    f.append(Map(start,'F'))
                    locate.remove(start)
                    if side==0: startablefloor.append(start)  
                else:
                    c=b
            c=0
            if doorside!=0:
                if len(locate)<=130:
                    break
                else:
                    doorban.extend(d)
            while True:
                start=random.choice(startablefloor)
                if ((start+1) in locate and not (start+1) in doorban) or ((start-1) in locate and not (start-1) in doorban) or ((start+10) in locate and not (start+10) in doorban) or ((start-10) in locate and not (start-10) in doorban):
                    break
                else:
                    startablefloor.remove(start)
                                        
        
        firstdoor.append(doorside)
        firstdoor.append(doorlong)   
        rendermap=False
            
    #draw on screen
    screen.fill((0,0,0))
    for i in f:
        i.draw(screen)             
            
                
            
    
    
    pygame.display.update()
    