import pygame
import random
import math

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


class Conststore:
    def __init__(self):
        self.enemykilled=0
        self.bosscount=0
        self.rendermap=True
        self.firstdoor=[]
        self.wave=0
        self.creepspeed=50
        self.bosscount=0
        self.mapcount=0
        self.stage='start'
        self.player=Player()
        self.bosses=[]
        self.pluses=[]
        #end and start
        self.startwrite=0
        self.writeduration=0
        self.changeline=1
        #guid
        self.guidenumber=1

class Mapstore:
    def __init__(self):
        self.locate=list(range(200))
        self.goable=[]
        self.map=[]
        self.obstacle=[]
        self.door=[]
        self.w=[]
        self.sr=[]
        self.sl=[]
        self.v=[]
        self.slr=[]
        self.slrt=[]
        self.slt=[]
        self.srt=[]
        self.st=[]
        self.insidef=[]
        self.wall=[]
        self.creeps=[]
        self.bullets=[]
        self.smallbullets=[]
        self.slashes=[]
        self.mapstay=0
        self.bossattacks=[]
        

chat_dic={
    'start':{
        'line1':'Lost soul',
        'line2':'adventure',
        'line3':'combat',
        'line4':'level up',
        'line5':'survive as long as you can',
        'line6':'press P to start>>'
    },
    'end':{
        'line1':'You dead!',
        'line2':lambda a: 'level '+ ,
        'line3':lambda a: 'wave '+ ,
        'line4':lambda a: 'map '+ ,
        'line5':lambda a: 'enemy killed: '+,
        'line6':lambda a: 'boss killed: '+ ,
        'line7':'press R to replay >>'        
    },
    'guide':{
        'line1':'this is your character, you will',
        'line2':'control him by WASD'        
    }
}