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
        self.position=xy
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
        self.position=xy
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
        elif type=='SRT':           
            self.img='assets/SRT.png'
        elif type=='S4':
            self.img='assets/S4.png'
        self.img=pygame.image.load(self.img).convert_alpha()
        self.img=pygame.transform.scale(self.img,(75,75))
        self.rect=pygame.Rect(self.x,self.y,75,75)
    def draw(self,screen):
        screen.blit(self.img,(self.x,self.y))
class Player:
    def __init__(self,xy):
        self.position=xy
        self.y=xy%10*75
        self.x=(xy-xy%10)/10*75
        self.targetx=self.x
        self.targety=self.y
        self.direction='right'
        self.speed=50
        self.img='assets/main'
        self.img=pygame.image.load(self.img).convert_alpha()
        self.img=pygame.transform.scale(self.img,(40,77))
        self.rect=pygame.Rect(self.x,self.y-(77-75),40,75)
    def draw(self,screen):
        screen.blit(self.img,(self.x,self.y))
    def move(self,dt):
        dx=self.targetx-self.x
        self.direction='right' if dx>0 else 'left'
        dy=self.targety-self.y
        distance=math.hypot(dx,dy)
        if self.speed*dt>=distance:
            self.x=self.targetx
            self.y
class Creep:
    def __init__(self,xy,type):
        self.position=xy
        self.y=xy%10*75
        self.x=(xy-xy%10)/10*75
        self.img='assets/main'
        self.h=10
        self.w=10
        self.img=pygame.image.load(self.img).convert_alpha()
        self.img=pygame.transform.scale(self.img,(self.w,self.h))
        self.wallrect=pygame.Rect(self.x,self.y-(self.h-75),self.w,75)
        self.rect=pygame.Rect(self.x,self.y,self.w,self.h)
    def draw(self,screen):
        screen.blit(self.img,(self.x,self.y))
rendermap=True
firstdoor=[]  #for save the door for next map
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
        map=[]
        obstacle=[]
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
        srt=[]
        st=[]
        insidef=[]
        if not firstdoor:
            doorlong=random.randint(1,5)
            doorside=random.choice([-1,1,-2,2])
            firstdoor.append(doorside)
            firstdoor.append(doorlong)
            if doorside==(-1):
                firstexactdoor=random.choice(list(range(19,189+1-doorlong*10,10)))
                firstdoor.append(firstexactdoor)                
                for i in range(0,doorlong):   
                    map.append(Map(firstexactdoor+i*10,'F'))
                    locate.remove(firstexactdoor+i*10)
                    door.append(firstexactdoor+i*10)
            elif doorside==(1):
                firstexactdoor=random.choice(list(range(10,180+1-doorlong*10,10))) 
                firstdoor.append(firstexactdoor)
                for i in range(0,doorlong):
                    map.append(Map(firstexactdoor+i*10,'F'))
                    locate.remove(firstexactdoor+i*10)
                    door.append(firstexactdoor+i*10)    
            elif doorside==(2):
                firstexactdoor=random.choice(list(range(1,8+1-doorlong)))
                firstdoor.append(firstexactdoor)
                for i in range(0,doorlong):
                    map.append(Map(firstexactdoor+i,'F'))
                    locate.remove(firstexactdoor+i)
                    door.append(firstexactdoor+i)                
            elif doorside==(-2):
                firstexactdoor=random.choice(list(range(191,198+1-doorlong)))
                firstdoor.append(firstexactdoor)
                for i in range(0,doorlong):
                    map.append(Map(firstexactdoor+i,'F'))
                    locate.remove(firstexactdoor+i)
                    door.append(firstexactdoor+i)
        else:
            doorlong=firstdoor[1]
            doorside=firstdoor[0]*(-1)
            if doorside==(-1):
                firstexactdoor=random.choice(list(range(19,189+1-doorlong*10,10)))   
                for i in range(0,doorlong):   
                    map.append(Map(firstexactdoor+i*10,'F'))
                    locate.remove(firstexactdoor+i*10)
                    door.append(firstexactdoor+i*10)
            elif doorside==(1):
                firstexactdoor=random.choice(list(range(10,180+1-doorlong*10,10)))
                for i in range(0,doorlong):
                    map.append(Map(firstexactdoor+i*10,'F'))
                    locate.remove(firstexactdoor+i*10)
                    door.append(firstexactdoor+i*10)    
            elif doorside==(2):
                firstexactdoor=random.choice(list(range(1,8+1-doorlong)))
                for i in range(0,doorlong):
                    map.append(Map(firstexactdoor+i,'F'))
                    locate.remove(firstexactdoor+i)
                    door.append(firstexactdoor+i)                
            elif doorside==(-2):
                firstexactdoor=random.choice(list(range(191,198+1-doorlong)))
                for i in range(0,doorlong):
                    map.append(Map(firstexactdoor+i,'F'))
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
        map.append(Map(start,'F'))    
        locate.remove(start)
        doorban.extend(door)            
        c=0
        doorside=0
        doorlong=0
        startablefloor=[]
        firstdoor=[]
        
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
                                door.append(start+b)
                            elif doorside!=2:                            
                                break
                            elif unablemeetagain:
                                break
                            else:
                                doorlong+=1
                                door.append(start+b)
                            if doorlong==5:
                                break
                            side=1
                        elif (start+b) in list(range(10,190,10)):
                            if doorside==0: 
                                doorside=1
                                door.append(start+b)
                            elif doorside!=1:                             
                                break
                            elif unablemeetagain:
                                break
                            else:
                                doorlong+=1
                                door.append(start+b)
                            if doorlong==5:
                                break
                            side=1
                        elif (start+b) in list(range(19,199,10)):
                            if doorside==0: 
                                doorside=-1
                                door.append(start+b)
                            elif doorside!=(-1):                          
                                break
                            elif unablemeetagain:
                                break
                            else:
                                doorlong+=1
                                door.append(start+b)
                            if doorlong==5:
                                break
                            side=1
                        elif (start+b) in list(range(191,199)):
                            if doorside==0: 
                                doorside=-2
                                door.append(start+b)
                            elif doorside!=(-2):
                                break
                            elif unablemeetagain:
                                break
                            else:
                                doorlong+=1
                                door.append(start+b)
                            if doorlong==5:
                                break
                            side=1
                    start+=b
                    map.append(Map(start,'F'))
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
        for i in map:
            if not i.position in door:
                insidef.append(i.position)
        for i in insidef:
            i-=1
            if i in locate:
                locate.remove(i)
                if i-1 in locate:
                    map.append(Map(i,'W'))
                    w.append(i)
                else:
                    if i in d:
                        map.append(Map(i,'W'))
                        w.append(i)
                    else:                        
                        map.append(Map(i,'F'))
                        insidef.append(i)
        for i in insidef:
            i-=10
            if i in locate:
                sr.append(i)
        for i in w:
            i-=10
            if i in locate:
                sr.append(i)
        for i in insidef:
            i+=10
            if i in locate:
                if i in sr:
                    slr.append(i)
                    sr.remove(i)
                else:
                    sl.append(i)
        for i in w:
            i+=10
            if i in locate:
                if i in sr:
                    slr.append(i)
                    sr.remove(i)
                else:
                    sl.append(i)
        for i in insidef:
            i+=1
            if i in locate:
                if i in sr:
                    srt.append(i)
                    sr.remove(i)
                elif i in sl:
                    slt.append(i)
                    sl.remove(i)
                elif i in slr:
                    slrt.append(i)
                    slr.remove(i)                            
                else:
                    st.append(i)               
        
        
        #có thể làm góc sau này, có thể làm cạnh cho cửa
        for i in locate:
            v.append(i)
        if v:
            for i in v:
                obstacle.append(Obstacle(i,'V'))
        if sr:
            for i in sr:
                locate.remove(i)
                obstacle.append(Obstacle(i,'SR'))
        if sl:
            for i in sl:
                locate.remove(i)
                obstacle.append(Obstacle(i,'SL'))
        if slr:
            for i in slr:
                locate.remove(i)
                obstacle.append(Obstacle(i,'SLR'))
        if slrt:
            for i in slrt:
                locate.remove(i)
                obstacle.append(Obstacle(i,'SLRT'))
        if slt:
            for i in slt:
                locate.remove(i)
                obstacle.append(Obstacle(i,'SLT'))
        if srt:
            for i in srt:
                locate.remove(i)
                obstacle.append(Obstacle(i,'SRT'))
        if st:
            for i in st:
                locate.remove(i)
                obstacle.append(Obstacle(i,'ST'))
                
                
    #draw on screen
    screen.fill((0,0,0))
    for i in map:
        i.draw(screen)
    for i in obstacle:
        i.draw(screen)             
            
                
            
    
    
    pygame.display.update()
    