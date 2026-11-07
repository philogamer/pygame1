import pygame
import random
import math

pygame.init()
pygame.mixer.init()
pygame.font.init()
screen=pygame.display.set_mode((1500,800))
transparentscreen=pygame.Surface((1500,800), pygame.SRCALPHA)
pygame.display.set_caption('Lost Soul')
clock=pygame.time.Clock()
font=pygame.font.Font('assets/font.ttf',30)
titlefont=pygame.font.Font('assets/endfont.ttf',100)
codefont=pygame.font.Font('assets/endfont.ttf',50)
chatfont=pygame.font.Font('assets/endfont.ttf',30)


def write(text,font,color,x,y):
    screen.blit(font.render(text,True,color),(x,y))

class Map:
    def __init__(self,xy,type):
        self.position=xy
        self.y=xy%10*70
        self.x=(xy-xy%10)/10*70
        if type=='W':
            self.img='assets/wall.png'
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
    def __init__(self):
        self.y=0
        self.x=0
        self.targetx=self.x
        self.targety=self.y
        self.direction='right'
        self.dmg=10
        self.speed=200
        self.maxspeed=200
        self.hp=500
        self.maxhp=500
        self.mana=100
        self.maxmana=100
        self.img='assets/main.png'
        self.img=pygame.image.load(self.img).convert_alpha()
        self.img=pygame.transform.scale(self.img,(61,107))
        self.rect=pygame.Rect(self.x,self.y-(107-70),61,107)
        self.wallrect=pygame.Rect(self.x,self.y+(107-73)-(107-70),61,71)
        self.manaregen=12
        self.attackspeed=0.5
        self.exp=0
        self.level=1
        self.buffstat=0
        self.takedame=True
        self.slashcooldown=0
        self.enemykilled=0
    def put(self,xy):
        self.y=xy%10*70
        self.x=(xy-xy%10)/10*70    
    def draw(self,screen):
        screen.blit(self.img,(self.x,self.y-(107-70)))
        pygame.draw.rect(screen,(0,0,0),pygame.Rect(85,705,310,40))
        pygame.draw.rect(screen,(225,0,0),pygame.Rect(90,710,self.hp*300/self.maxhp,30))
        pygame.draw.rect(screen,(0,0,0),pygame.Rect(85,750,310,40))
        pygame.draw.rect(screen,(50,107,250),pygame.Rect(90,755,self.mana*300/self.maxmana,30))
        pygame.draw.rect(screen,(0,0,0),pygame.Rect(1425,120,50,500))
        pygame.draw.rect(screen,(52,6,59),pygame.Rect(1425,120,50,self.exp*500/(90+25*(self.level-1)+5*(self.level-1)**2)))
    def move(self,dt):
        dx=self.targetx-self.x
        self.direction='right' if dx>0 else 'left'
        dy=self.targety-self.y
        distance=math.hypot(dx,dy)
        if dx!=0 or dy!=0:    
            if self.mana>0: self.mana-=9*dt
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
    def __init__(self,xy,type,buff):
        self.position=xy
        self.y=xy%10*70
        self.x=(xy-xy%10)/10*70
        self.targetx=self.x
        self.targety=self.y
        self.direction='right'
        self.speed=50*(1+0.01*buff)
        self.touchwall=True
        self.touchwallx=False
        self.touchwally=False
        self.type=type
        self.randomx=0
        self.randomy=0
        self.shoot=0
        self.notry=False
        self.testx=False
        self.testy=False
        self.takedame=False
        if self.type=='normal':
            self.img='assets/ghost.png'
            self.h=30*2
            self.w=24*2
            self.hp=70*(1+0.08*buff)
            self.maxhp=70*(1+0.08*buff)
            self.range=130
            self.view=400
            self.dmg=10*(1+0.05*buff)
        elif self.type=='elite':
            self.img='assets/ghost1.png'
            self.h=30*2
            self.w=24*2
            self.hp=150*(1+0.06*buff)
            self.maxhp=150*(1+0.06*buff)
            self.range=130
            self.view=400
            self.dmg=15*(1+0.05*buff)
        elif self.type=='slime':
            self.img='assets/slime.png'
            self.h=14*2
            self.w=19*2
            self.hp=50*(1+0.07*buff)
            self.maxhp=50*(1+0.07*buff)
            self.range=100
            self.view=400
            self.dmg=5*(1+0.05*buff)
        
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
        if self.y<(70-self.h):
            self.y=70-self.h 
        if self.y>700-self.h:
            self.y=700-self.h
    def update(self):
        self.rect=pygame.Rect(self.x,self.y,self.w,self.h)
    def checkwall(self):
        self.wallrect=pygame.Rect(self.targetx,self.targety+(self.h-70),self.w,70)
class Bullet:
    def __init__(self,x,y,targetx,targety,dmg):
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
        self.dmg=dmg
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
class Smallbullet:
    def __init__(self,x,y,targetx,targety,dmg):
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
        self.dmg=dmg
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
class Slash:
    def __init__(self,x,y,direction,dmg):
        self.y=y
        self.present=0
        self.img='assets/slash.png'
        if direction=='right':
            self.x=x+63
        if direction=='left':
            self.x=x-51
        self.img=pygame.image.load(self.img).convert_alpha()
        self.img=pygame.transform.scale(self.img,(48,107))
        self.rect=pygame.Rect(self.x,self.y,48,107)
        self.dmg=dmg
    def draw(self,screen):
        screen.blit(self.img,(self.x,self.y))
class Plus:
    def __init__(self,type):
        self.type=type
        self.img='assets/plus.png'
        if type=='dmg':
            self.x=600
            self.y=705
        elif type=='maxmana':
            self.x=640
            self.y=750
        elif type=='maxhp':
            self.x=860
            self.y=705
        elif type=='movespeed':
            self.x=914
            self.y=750
        elif type=='manaregen':
            self.x=1150
            self.y=705
        elif type=='attackspeed':
            self.x=1200
            self.y=750
        self.img=pygame.image.load(self.img).convert_alpha()
        self.img=pygame.transform.scale(self.img,(30,30))
        self.rect=pygame.Rect(self.x,self.y,30,30)
    def draw(self,screen):
        screen.blit(self.img,(self.x,self.y))   
class Boss:
    def __init__(self,buff):
        self.x=750
        self.y=400
        self.hp=280*(1+0.09*buff)
        self.maxhp=280*(1+0.09*buff)
        self.speed=182*(1+0.15*buff)
        self.cooldown=0
        self.dmg=20**(1+0.09*buff)
        self.img='assets/skull.png'
        self.w=150
        self.h=150
        self.img=pygame.image.load(self.img).convert_alpha()
        self.img=pygame.transform.scale(self.img,(self.w,self.h))
        self.rect=pygame.Rect(self.x,self.y,self.w,self.h)
        self.targetx=self.x
        self.targety=self.y
        self.takedame=False
        self.skillchoose=0
        self.skillprepare=0
    def draw(self,screen):
        screen.blit(self.img,(self.x,self.y))
        pygame.draw.rect(screen,(112,112,112),pygame.Rect(200,10,1000,30))
        pygame.draw.rect(screen,(225,0,0),pygame.Rect(200,10,self.hp*1000/self.maxhp,30))
    def move(self,dt):
        dx=self.targetx-self.x
        dy=self.targety-self.y
        distance=math.hypot(dx,dy)
        if self.speed*dt>=distance:
            self.x=self.targetx
            self.y=self.targety
        else:
            self.x+=dx/distance*self.speed*dt
            self.y+=dy/distance*self.speed*dt
        if self.x<70:
            self.x=70
        if self.x>(1400-70-self.w):
            self.x=(1400-70-self.w)
        if self.y<70:
            self.y=70 
        if self.y>(700-70-self.h):
            self.y=700-70-self.h
    def update(self):
        self.rect=pygame.Rect(self.x,self.y,self.w,self.h)
class Bossattack:
    def __init__(self,x,y,dmg,width):
        self.y=y
        self.x=x
        self.w=width
        self.img='assets/bossattack.png'
        self.img=pygame.image.load(self.img).convert_alpha()
        self.img=pygame.transform.scale(self.img,(width,width*87/70))
        self.dmg=dmg
    def warn(self):
        pygame.draw.rect(transparentscreen,(225,0,0,20),(self.x,self.y,self.w,self.w*87/70))
        screen.blit(transparentscreen,(0,0))
    def update(self,screen):
        screen.blit(self.img,(self.x,self.y))
        self.rect=pygame.Rect(self.x,self.y,self.w,self.w*87/70)

def render1(firstdoor,map,locate,door,player,insidef,w,goable,sr,sl,srt,slt,slr,slrt,st,wall,v,obstacle,bosses,wave):
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
        player.put(random.choice(door))
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
        player.put(random.choice(door))

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
    firstdoor.clear()
    goable.clear()
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
                            goable.remove(Goable(start+b))
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
                            goable.remove(Goable(start+b))
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
                            goable.remove(Goable(start+b))
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
                            goable.remove(Goable(start+b))
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
def render2(firstdoor,map,locate,door,player,insidef,w,goable,sr,sl,srt,slt,slr,slrt,st,wall,v,obstacle,bosses,wave):
    bosses.append(Boss(wave))
    for i in range(1,199):
        if i%10==1:
            wall.append(Map(i,'W'))
        else:
            map.append(Map(i,'F'))
    for i in range(1,9):
        obstacle.append(Obstacle(i,'SR'))
    for i in range(191,199):
        obstacle.append(Obstacle(i,'SL'))
    for i in range(19,199,10):
        obstacle.append(Obstacle(i,'ST'))
    for i in range(0,200,10):
        obstacle.append(Obstacle(i,'V'))
    obstacle.append(Obstacle(9,'V'))
    obstacle.append(Obstacle(199,'V'))
    player.put(12)          
def render3(firstdoor,map,locate,door,player,insidef,w,goable,sr,sl,srt,slt,slr,slrt,st,wall,v,obstacle,bosses,wave):
        player.put(99)
        for i in range(1,199):
            if i%10==1 and i!=91 and i!=101:
                wall.append(Map(i,'W'))
            else:
                map.append(Map(i,'F'))
        for i in range(1,9):
            obstacle.append(Obstacle(i,'SR'))
        for i in range(191,199):
            obstacle.append(Obstacle(i,'SL'))
        for i in range(19,199,10):
            if i!=99 and i!=109 and i!=119 and i!=89:
                obstacle.append(Obstacle(i,'ST'))
        for i in range(0,200,10):
            if i!=90 and i!=100 and i!=80 and i!=110:
                obstacle.append(Obstacle(i,'V'))
        obstacle.append(Obstacle(9,'V'))
        obstacle.append(Obstacle(199,'V'))
        obstacle.append(Obstacle(80,'SR'))
        obstacle.append(Obstacle(110,'SL'))
        obstacle.append(Obstacle(89,'SRT'))
        obstacle.append(Obstacle(119,'SLT'))
        obstacle.append(Obstacle(143,'SRT'))
        obstacle.append(Obstacle(53,'SLT'))
        for i in range(63,143,10):
            obstacle.append(Obstacle(i,'ST'))
        for i in range(54,57):
            obstacle.append(Obstacle(i,'SL'))
        for i in range(144,147):
            obstacle.append(Obstacle(i,'SR'))
        for i in range(66,146,10):
            obstacle.append(Obstacle(i,'V'))
        for i in range(57,157,10):
            wall.append(Map(i,'W'))
def playerbehave(wave,player,obstacle,keys,slashes,creeps,bosses,dt,pluses):
    creepspeed=50*(1+0.01*wave)
    player.speed=creepspeed-10+(player.maxspeed-creepspeed)*(player.mana/player.maxmana)
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
                
    if keys[pygame.K_LEFT] and player.slashcooldown<=0 and player.mana>=6:
        player.mana-=6
        slashes.append(Slash(player.x,player.y-(107-70),'left',player.dmg))
        player.slashcooldown=1-player.attackspeed
        for creep in creeps:
            creep.takedame=True
        if bosses:
            for boss in bosses:
                boss.takedame=True
                            
    if keys[pygame.K_RIGHT] and player.slashcooldown<=0 and player.mana>=6:
        player.mana-=6
        slashes.append(Slash(player.x,player.y-(107-70),'right',player.dmg))
        player.slashcooldown=1-player.attackspeed
        for creep in creeps:
            creep.takedame=True
        if bosses:
            for boss in bosses:
                boss.takedame=True
    for i in slashes:
        i.present+=dt
        if i.present>=0.1:
            slashes.remove(i)
            for creep in creeps:
                creep.takedame=False
    if not slashes: player.slashcooldown-=dt
    if player.mana<player.maxmana:
        player.mana+=player.manaregen*dt
        if player.mana>player.maxmana:
            player.mana=player.maxmana
    
            
    
    player.move(dt)
    player.update()
    
    if player.exp>=(90+25*(player.level-1)+5*(player.level-1)**2):
        player.level+=1
        player.exp-=(90+25*(player.level-1)+5*(player.level-1)**2)
        player.buffstat+=2
    if player.buffstat==0:
        if pluses: pluses=[]
def creeprandom(creep,obstacle,player,bullets,dt,chase):
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
                creep.notry=False
                break    
    if creep.randomy!=0:
        creep.targety=creep.y+creep.randomy
        creep.checkwall()
        for i in obstacle:
            if i.rect.colliderect(creep.wallrect):
                creep.targety=creep.y
                creep.touchwall=True
                creep.checkwall()
                creep.notry=False
                break
    if creep.x<=0 or creep.x>=(1400-creep.w) or creep.y<=(70-creep.h) or creep.y>=700-creep.h:
        creep.touchwall=True
        creep.notry=False
    creep.move(dt)
    creep.update()
def creepmove(creep,obstacle,player,bullets,dt,chase):
    if creep.touchwally and creep.touchwallx:
        if creep.testx:
            creep.randomx*=(-1)
            creep.touchwallx=False
        elif creep.testy:
            creep.randomy*=(-1)
            creep.touchwally=False                        
        else:
            creep.notry=True
            creep.touchwallx=False
            creep.touchwally=False                                    
    elif creep.testx:
        creep.targetx=creep.x
        creep.targety=creep.y
        creep.testx=False
        creep.touchwallx=False
        creep.touchwally=False
        creep.targetx=creep.x+creep.randomx*chase
        creep.checkwall()
        for i in obstacle:
            if i.rect.colliderect(creep.wallrect):
                creep.targetx=creep.x
                creep.touchwallx=True     
                creep.checkwall()
                break
        if player.y-creep.y>0:
            creep.randomy=1
        elif player.y-creep.y<0:
            creep.randomy=-1
        creep.targety=creep.y+creep.randomy*chase
        creep.checkwall()
        for i in obstacle:
            if i.rect.colliderect(creep.wallrect):
                creep.targety=creep.y
                creep.touchwally=True
                creep.checkwall()
                creep.testx=True
                break
        if creep.x<=0 or creep.x>=(1400-creep.w):
            creep.touchwallx=True
        if creep.y<=(70-creep.h) or creep.y>=700-creep.h:
            creep.touchwally=True
    elif creep.testy:
        creep.targetx=creep.x
        creep.targety=creep.y                    
        creep.testy=False
        creep.touchwallx=False
        creep.touchwally=False
        if player.x-creep.x>0:
            creep.randomx=1
        elif player.x-creep.x<0:
            creep.randomx=-1                    
        creep.targetx=creep.x+creep.randomx*chase
        creep.checkwall()
        for i in obstacle:
            if i.rect.colliderect(creep.wallrect):
                creep.targetx=creep.x
                creep.touchwallx=True     
                creep.checkwall()
                creep.testy=True
                break
        creep.targety=creep.y+creep.randomy*chase
        creep.checkwall()
        for i in obstacle:
            if i.rect.colliderect(creep.wallrect):
                creep.targety=creep.y
                creep.touchwally=True
                creep.checkwall()
                break
        if creep.x<=0 or creep.x>=(1400-creep.w):
            creep.touchwallx=True
        if creep.y<=(70-creep.h) or creep.y>=700-creep.h:
            creep.touchwally=True
    else:
        creep.targetx=creep.x
        creep.targety=creep.y                    
        creep.touchwallx=False
        creep.touchwally=False
        if player.x-creep.x>0:
            creep.randomx=1
        elif player.x-creep.x<0:
            creep.randomx=-1
        creep.targetx=creep.x+creep.randomx*chase
        creep.checkwall()
        for i in obstacle:
            if i.rect.colliderect(creep.wallrect):
                creep.targetx=creep.x
                creep.touchwallx=True     #hết đi được x
                creep.checkwall()
                break
        if player.y-creep.y>0:
            creep.randomy=1
        elif player.y-creep.y<0:
            creep.randomy=-1
        creep.targety=creep.y+creep.randomy*chase
        creep.checkwall()
        for i in obstacle:
            if i.rect.colliderect(creep.wallrect):
                creep.targety=creep.y
                creep.touchwally=True
                creep.checkwall()
                break
        if creep.x<=(70-creep.h) or creep.x>=(1400-creep.w):
            creep.touchwallx=True
        if creep.y<=(70-creep.h) or creep.y>=700-creep.h:
            creep.touchwally=True
        if creep.touchwally and int(creep.x)==int(player.x) and not creep.touchwallx:
            creep.testx=True
            creep.randomx=1 if player.x-creep.x>=0 else -1
        if creep.touchwallx and int(creep.y)==int(player.y) and not creep.touchwally:
            creep.testy=True
            creep.randomy=1 if player.y-creep.y>=0 else -1
    creep.move(dt)
    creep.update()            
def creepshoot(creep,obstacle,player,bullets,dt,chase):
    creep.shoot+=dt
    if creep.shoot>=2.5:
        bullets.append(Bullet(creep.x,creep.y,player.x,player.y,creep.dmg))
        creep.shoot=0
def creepmoveandshoot(creep,obstacle,player,bullets,dt,chase):
    creepmove(creep,obstacle,player,bullets,dt,chase)
    creepshoot(creep,obstacle,player,bullets,dt,chase)
def creepgetdame(slashes,creeps,player,wave):
    for creep in creeps:
        if creep.rect.colliderect(slashes[0].rect) and creep.takedame:
            creep.hp-=slashes[0].dmg
            creep.takedame=False
        if creep.hp<=0:
            creeps.remove(creep)
            player.enemykilled+=1
            if creep.type=='normal':
                player.exp+=12*(1+0.02*wave)
            elif creep.type=='slime':
                player.exp+=8*(1+0.02*wave)
            elif creep.type=='elite':
                player.exp+=30*(1+0.02*wave)
            if len(creeps)==0:
                player.exp+=30*(1+0.02*wave)            
                