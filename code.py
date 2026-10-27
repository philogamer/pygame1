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
        elif type=='V':
            self.img='assets/V.png'
        elif type=='CL':
            self.img='assets/CL.png'
        elif type=='CR':
            self.img='assets/CR.png'
        elif type=='CRL':
            self.img='assets/CRL.png'
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

rendermap=True
firstdoor=[]  #for save the door for next map
#Game loop
while True:
    dt=clock.tick(60)/1000
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            quit(0)
    #random map logic
    if rendermap:
        locate=list(range(200))
        door=[]
        f=[]
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
                firstexactdoor=firstdoor[2]+9       
                for i in range(0,doorlong):   
                    f.append(Map(firstexactdoor+i*10,'F'))
                    locate.remove(firstexactdoor+i*10)
                    door.append(firstexactdoor+i*10)
            elif doorside==(1):
                firstexactdoor=firstdoor[2]-9
                for i in range(0,doorlong):
                    f.append(Map(firstexactdoor+i*10,'F'))
                    locate.remove(firstexactdoor+i*10)
                    door.append(firstexactdoor+i*10)    
            elif doorside==(2):
                firstexactdoor=firstdoor[2]-90
                for i in range(0,doorlong):
                    f.append(Map(firstexactdoor+i,'F'))
                    locate.remove(firstexactdoor+i)
                    door.append(firstexactdoor+i)                
            elif doorside==(-2):
                firstexactdoor=firstdoor[2]+90
                for i in range(0,doorlong):
                    f.append(Map(firstexactdoor+i,'F'))
                    locate.remove(firstexactdoor+i)
                    door.append(firstexactdoor+i)

        start=random.choice(door)
        c=0
        while start in door:
            if doorside==1 or doorside==-1:
                a=[10,-10]
            else:
                a=[1,-1]
            if c!=0: 
                if len(a)==0:
                    break
                elif len(a)==1:
                    c=0
                else:
                    a.remove(c)
            b=random.choice(a)
            if (start+b) in locate and not (start+b) in [0,9,199,190]:
                start+=b
                f.append(Map(start,'F'))
                locate.remove(start)
            else:
                c=b
        
        c=0
        doorside=0
        doorlong=0
        while True:
            a=[1,-1,10,-10]
            if c!=0: 
                if len(a)==0:
                    break
                elif len(a)==1:
                    c=0
                else:
                    a.remove(c)
            b=random.choice(a)
            if (start+b) in locate and not (start+b) in [0,9,199,190] and not (start+b) in door:
                d=list(range(1,9))+list(range(10,190,10))+list(range(19,199,10))+list(range(191,199))
                if (start+b) in d:
                    if (start+b) in list(range(1,9)):
                        if doorside==0: 
                            doorside=2
                        elif doorside!=2:
                            break
                        else:
                            doorlong+=1
                        if doorlong==6:
                            break
                    elif (start+b) in list(range(10,190)):
                        if doorside==0: 
                            doorside=1
                        elif doorside!=1:
                            break
                        else:
                            doorlong+=1
                        if doorlong==6:
                            break
                    elif (start+b) in list(range(19,199)):
                        if doorside==0: 
                            doorside=-1
                        elif doorside!=(-1):
                            break
                        else:
                            doorlong+=1
                        if doorlong==6:
                            break
                    elif (start+b) in list(range(191,199)):
                        if doorside==0: 
                            doorside=-2
                        elif doorside!=(-2):
                            break
                        else:
                            doorlong+=1
                        if doorlong==6:
                            break
                start+=b
                f.append(Map(start,'F'))
                locate.remove(start)  
            else:
                c=b
            if len(locate)==5:
                break
        rendermap=False
            
    #draw on screen
    for i in f:
        i.draw(screen)             
            
                
            
    
    
    pygame.display.update()
    