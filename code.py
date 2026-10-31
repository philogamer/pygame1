import pygame
import random
import math

pygame.init()
pygame.mixer.init()
screen=pygame.display.set_mode((1500,800))
pygame.display.set_caption('Lost Soul')
stage='map'
clock=pygame.time.Clock()


class Map:
    def __init__(self,xy,type):
        self.position=xy
        self.y=xy%10*70
        self.x=(xy-xy%10)/10*70
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
        self.img=pygame.transform.scale(self.img,(70,70))
    def draw(self,screen):
        screen.blit(self.img,(self.x,self.y))
class Goable:
    def __init__(self,xy):
        self.position=xy
        self.y=xy%10*70
        self.x=(xy-xy%10)/10*70
        self.rect=pygame.Rect(self.x,self.y,70,70)
    def update(self):
        self.rect=pygame.Rect(self.x,self.y,70,70)
class Obstacle:
    def __init__(self,xy,type):
        self.position=xy
        self.y=xy%10*70
        self.x=(xy-xy%10)/10*70
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
        self.img=pygame.transform.scale(self.img,(70,70))
        self.rect=pygame.Rect(self.x,self.y,70,70)
    def draw(self,screen):
        screen.blit(self.img,(self.x,self.y))
class Player:
    def __init__(self,xy):
        self.position=xy
        self.y=xy%10*70
        self.x=(xy-xy%10)/10*70
        self.targetx=self.x
        self.targety=self.y
        self.direction='right'
        self.speed=200
        self.hp=500
        self.maxhp=500
        self.img='assets/main.png'
        self.img=pygame.image.load(self.img).convert_alpha()
        self.img=pygame.transform.scale(self.img,(61,107))
        self.rect=pygame.Rect(self.x,self.y-(107-70),61,107)
        self.wallrect=pygame.Rect(self.x,self.y+(107-73)-(107-70),61,71)
    def draw(self,screen):
        screen.blit(self.img,(self.x,self.y-(107-70)))
    def move(self,dt):
        dx=self.targetx-self.x
        self.direction='right' if dx>0 else 'left'
        dy=self.targety-self.y
        distance=math.hypot(dx,dy)
        if self.speed*dt>=distance:
            self.x=self.targetx
            self.y=self.targety
        else:
            self.x+=dx/distance*self.speed*dt
            self.y+=dy/distance*self.speed*dt
        if self.x<0:
            self.x=0
        if self.x>(1400-61):
            self.x=(1400-61)
        if self.y<-((107-70)-(107-70)):
            self.y=-((107-70)-(107-70))  
        if self.y>((700-107)+(107-70)):
            self.y=700-107+(107-70)
    def update(self):
        self.rect=pygame.Rect(self.x,self.y-(107-70),61,107)
    def checkwall(self):
        self.wallrect=pygame.Rect(self.targetx,self.targety+(107-73)-(107-70),61,71)
class Creep:
    def __init__(self,xy,type):
        self.position=xy
        self.y=xy%10*70
        self.x=(xy-xy%10)/10*70
        self.targetx=self.x
        self.targety=self.y
        self.direction='right'
        self.speed=50
        self.touchwall=True
        self.touchwallx=False
        self.touchwally=False
        self.type=type
        self.randomx=0
        self.randomy=0
        self.shoot=0
        if self.type=='normal':
            self.img='assets/ghost.png'
            self.h=30*2
            self.w=24*2
            self.hp=100
            self.maxhp=100
            self.range=200
            self.view=300
            self.dmg=10
        elif self.type=='elite':
            self.img='assets/ghost1.png'
            self.h=30*2
            self.w=24*2
            self.hp=200
            self.maxhp=200
            self.range=200
            self.view=300
            self.dmg=15
        elif self.type=='slime':
            self.img='assets/slime.png'
            self.h=14*2
            self.w=19*2
            self.hp=70
            self.maxhp=70
            self.range=100
            self.view=200
            self.dmg=3
        
        self.img=pygame.image.load(self.img).convert_alpha()
        self.img=pygame.transform.scale(self.img,(self.w,self.h))
        self.wallrect=pygame.Rect(self.targetx,self.targety+(self.h-70),self.w,70)
        self.rect=pygame.Rect(self.x,self.y,self.w,self.h)
    def draw(self,screen):
        screen.blit(self.img,(self.x,self.y))
        pygame.draw.rect(screen,(112,112,112),pygame.Rect(self.x,self.y-4,self.w,4))
        pygame.draw.rect(screen,(225,0,0),pygame.Rect(self.x,self.y-4,self.hp*self.w/self.maxhp,4))
    def move(self,dt):
        dx=self.targetx-self.x
        self.direction='right' if dx>0 else 'left'
        dy=self.targety-self.y
        distance=math.hypot(dx,dy)
        if self.speed*dt>=distance:
            self.x=self.targetx
            self.y=self.targety
        else:
            self.x+=dx/distance*self.speed*dt
            self.y+=dy/distance*self.speed*dt
        if self.x<0:
            self.x=0
        if self.x>(1400-self.w):
            self.x=(1400-self.w)
        if self.y<0:
            self.y=0 
        if self.y>700-self.h:
            self.y=700-self.h
    def update(self):
        self.rect=pygame.Rect(self.x,self.y,self.w,self.h)
    def checkwall(self):
        self.wallrect=pygame.Rect(self.targetx,self.targety+(self.h-70),self.w,70)
class Bullet:
    def __init__(self,x,y,targetx,targety):
        self.y=y+18
        self.x=x
        self.targetx=targetx
        self.targety=targety
        self.speed=200
        self.img='assets/bullet.png'
        self.img=pygame.image.load(self.img).convert_alpha()
        self.img=pygame.transform.scale(self.img,(20,20))
        self.rect=pygame.Rect(self.x,self.y,20,20)
        self.wallrect=pygame.Rect(self.x,self.y-18,20,20+18)
        self.dx=(self.targetx-self.x)*2000
        self.dy=(self.targety-self.y)*2000
        self.distance=math.hypot(self.dx,self.dy)
        self.dmg=7
    def draw(self,screen):
        screen.blit(self.img,(self.x,self.y))
    def move(self,dt):
        self.x+=self.dx/self.distance*self.speed*dt
        self.y+=self.dy/self.distance*self.speed*dt
        if self.x<0:
            self.x=0
        if self.x>(1400-20):
            self.x=(1400-20)
        if self.y<0:
            self.y=0  
        if self.y>(700-20):
            self.y=700-20
        
    def update(self):
        self.rect=pygame.Rect(self.x,self.y,20,20)
        self.wallrect=pygame.Rect(self.x,self.y-18,20,20+18)        


rendermap=True
firstdoor=[]  #for save the door for next map
#Game loop
while True:
    dt=clock.tick(60)/1000
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            quit(0)
        keys=pygame.key.get_pressed()
    #random map logic
    if rendermap:
        locate=list(range(200))
        goable=[]
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
        wall=[]
        creeps=[]
        bullets=[]
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
            player=Player(random.choice(door))
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
            player=Player(random.choice(door))

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
        goable=[]
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
                                goable.append(Goable(start+b))
                            elif doorside!=2:                            
                                break
                            elif unablemeetagain:
                                break
                            else:
                                doorlong+=1
                                door.append(start+b)
                                goable.append(Goable(start+b))
                            if doorlong==5:
                                doorlong-=1
                                break
                            side=1
                        elif (start+b) in list(range(10,190,10)):
                            if doorside==0: 
                                doorside=1
                                door.append(start+b)
                                goable.append(Goable(start+b))
                            elif doorside!=1:                             
                                break
                            elif unablemeetagain:
                                break
                            else:
                                doorlong+=1
                                door.append(start+b)
                                goable.append(Goable(start+b))
                            if doorlong==5:
                                doorlong-=1
                                break
                            side=1
                        elif (start+b) in list(range(19,199,10)):
                            if doorside==0: 
                                doorside=-1
                                door.append(start+b)
                                goable.append(Goable(start+b))
                            elif doorside!=(-1):                          
                                break
                            elif unablemeetagain:
                                break
                            else:
                                doorlong+=1
                                door.append(start+b)
                                goable.append(Goable(start+b))
                            if doorlong==5:
                                doorlong-=1
                                break
                            side=1
                        elif (start+b) in list(range(191,199)):
                            if doorside==0: 
                                doorside=-2
                                door.append(start+b)
                                goable.append(Goable(start+b))
                            elif doorside!=(-2):
                                break
                            elif unablemeetagain:
                                break
                            else:
                                doorlong+=1
                                door.append(start+b)
                                goable.append(Goable(start+b))
                            if doorlong==5:
                                doorlong-=1
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
        firstdoor.append(doorlong+1)   
        rendermap=False
        for i in map:
            insidef.append(i.position)
        for i in insidef:
            if not i in list(range(10,190,10)):
                i-=1
                if i in locate:
                    locate.remove(i)
                    if i-1 in locate:
                        wall.append(Map(i,'W'))
                        w.append(i)
                    else:
                        if i in d:
                            wall.append(Map(i,'W'))
                            w.append(i)
                        else:                        
                            map.append(Map(i,'F'))
                            insidef.append(i)
        for i in insidef:
            if not i in list(range(1,9)):
                i-=10
                if i in locate:
                    sr.append(i)
        for i in w:
            if not i in list(range(1,9)):
                i-=10
                if i in locate:
                    sr.append(i)
        for i in insidef:
            if not i in list(range(191,199)):
                i+=10
                if i in locate:
                    if i in sr:
                        slr.append(i)
                        sr.remove(i)
                    else:
                        sl.append(i)
        for i in w:
            if not i in list(range(191,199)):
                i+=10
                if i in locate:
                    if i in sr:
                        slr.append(i)
                        sr.remove(i)
                    else:
                        sl.append(i)
        for i in insidef:
            if not i in list(range(19,199,10)) and not i==0:
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
        
    
    #main character logic
    player.targetx=player.x
    player.targety=player.y
    if keys[pygame.K_a]:
        player.targetx=player.x-1
        player.checkwall()
        for i in obstacle:
            if i.rect.colliderect(player.wallrect):
                player.targetx=player.x
                player.checkwall()
    if keys[pygame.K_d]:
        player.targetx=player.x+1
        player.checkwall()
        for i in obstacle:
            if i.rect.colliderect(player.wallrect):
                player.targetx=player.x
                player.checkwall()
    if keys[pygame.K_w]:
        player.targety=player.y-1
        player.checkwall()
        for i in obstacle:
            if i.rect.colliderect(player.wallrect):
                player.targety=player.y
                player.checkwall()
    if keys[pygame.K_s]:
        player.targety=player.y+1
        player.checkwall()
        for i in obstacle:
            if i.rect.colliderect(player.wallrect):
                player.targety=player.y
                player.checkwall()
                
    player.move(dt)
    player.update()
    
    #creep logic
    creepsquare=random.sample(insidef,int(len(insidef)/5))
    if creeps==[]:
        for i in creepsquare:
            creeps.append(Creep(i,random.choice(['slime','normal','elite'])))
    for creep in creeps:
        if math.hypot(player.x-creep.x,player.y-creep.y)>creep.range:
            if math.hypot(player.x-creep.x,player.y-creep.y)>creep.view:    
                creep.targetx=creep.x
                creep.targety=creep.y
                if creep.touchwall:
                    creep.randomx=random.choice([-1,1])
                    creep.randomy=random.choice([-1,1])
                    creep.touchwall=False
                if creep.randomx!=0:
                    creep.targetx=creep.x+creep.randomx
                    creep.checkwall()
                    for i in obstacle:
                        if i.rect.colliderect(creep.wallrect):
                            creep.targetx=creep.x
                            creep.touchwall=True
                            creep.checkwall()    
                if creep.randomy!=0:
                    creep.targety=creep.y+creep.randomy
                    creep.checkwall()
                    for i in obstacle:
                        if i.rect.colliderect(creep.wallrect):
                            creep.targety=creep.y
                            creep.touchwall=True
                            creep.checkwall()
                if creep.x<=0 or creep.x>=(1400-creep.w) or creep.y<=0 or creep.y>=700-creep.h:
                    creep.touchwall=True
            else:
                if creep.touchwallx:
                    creep.randomx=random.choice([-1,1])
                    creep.touchwallx=False
                else:
                    if player.x-creep.x>0:
                        creep.randomx=1
                    elif player.x-creep.x<0:
                        creep.randomx=-1
                if creep.touchwally:
                    creep.randomy=random.choice([-1,1])
                    creep.touchwally=False
                else:
                    if player.y-creep.y>0:
                        creep.randomy=1
                    elif player.y-creep.y<0:
                        creep.randomy=-1
                creep.targetx=creep.x+creep.randomx
                creep.checkwall()
                for i in obstacle:
                    if i.rect.colliderect(creep.wallrect):
                        creep.targetx=creep.x
                        creep.touchwallx=True
                        creep.checkwall()
                creep.targety=creep.y+creep.randomy
                creep.checkwall()
                for i in obstacle:
                    if i.rect.colliderect(creep.wallrect):
                        creep.targety=creep.y
                        creep.touchwally=True
                        creep.checkwall()
                if creep.x<=0 or creep.x>=(1400-creep.w):
                    creep.touchwallx=True
                if creep.y<=0 or creep.y>=700-creep.h:
                    creep.touchwally=True
                
        
            creep.move(dt)
            creep.update()
        else:
            creep.shoot+=dt
            if creep.shoot>=1:
                bullets.append(Bullet(creep.x,creep.y,player.x,player.y))
                creep.shoot=0
    for bullet in bullets:
        bullet.move(dt)
        bullet.update()
        if bullet.rect.colliderect(player.rect):
            bullets.remove(bullet)
        elif bullet.x>=(1400-20) or bullet.x<=0 or bullet.y<=0 or bullet.y>=(700-20):
            bullets.remove(bullet)
        else:
            for object in obstacle:
                if bullet.wallrect.colliderect(object.rect):
                    bullets.remove(bullet)
                    break            
        
            
            
    for i in goable:
        if i.rect.colliderect(player.rect):
            if player.x<=0 or player.x>=(1400-61) or player.y<=-((107-70)-(107-70)) or player.y>=((700-107)+(107-70)):
                rendermap=True

    
        

        
            
        
                       
                
    #draw on screen
    screen.fill((70,70,70))
    for i in map:
        i.draw(screen)
    for i in obstacle:
        i.draw(screen)
    for i in wall:
        i.draw(screen)
    for i in creeps:
        i.draw(screen)
        pygame.draw.rect(screen,(225,0,0),i.wallrect,1)
    pygame.draw.rect(screen,(225,0,0),player.wallrect,1)
    player.draw(screen)
    for i in bullets:
        i.draw(screen)
        pygame.draw.rect(screen,(225,0,0),i.wallrect,1)
               
            
                
            
    
    
    pygame.display.update()
    