import pygame
import random
import math
pygame.init()
pygame.mixer.init()
pygame.font.init()
font=pygame.font.Font('assets/font.ttf',30)
titlefont=pygame.font.Font('assets/endfont.ttf',100)
codefont=pygame.font.Font('assets/endfont.ttf',50)
chatfont=pygame.font.Font('assets/endfont.ttf',30)
smallfont=pygame.font.Font('assets/endfont.ttf',15)
class Map:
    def __init__(self,xy,type):
        self.position=xy
        self.y=xy%10*70
        self.x=(xy-xy%10)/10*70
        if type=='w':
            self.img='assets/wall.png'
        elif type=='f':
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
        if type=='v':
            self.img='assets/V.png'
        elif type=='sl':
            self.img='assets/SL.png'
        elif type=='slr':
            self.img='assets/SLR.png'
        elif type=='slrt':
            self.img='assets/SLRT.png'
        elif type=='slt':
            self.img='assets/SLT.png'
        elif type=='sr':
            self.img='assets/SR.png'
        elif type=='st':
            self.img='assets/ST.png'
        elif type=='srt':           
            self.img='assets/SRT.png'
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
        self.sloweffect=0
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
        self.tested='none'
        if self.type=='normal':
            self.img='assets/ghost.png'
            self.h=30*2
            self.w=24*2
            self.hp=70*(1+0.08*buff)
            self.maxhp=70*(1+0.08*buff)
            self.range=125
            self.view=400
            self.dmg=10*(1+0.05*buff)
        elif self.type=='elite':
            self.img='assets/ghost1.png'
            self.h=30*2
            self.w=24*2
            self.hp=150*(1+0.06*buff)
            self.maxhp=150*(1+0.06*buff)
            self.range=125
            self.view=400
            self.dmg=15*(1+0.05*buff)
        elif self.type=='slime':
            self.img='assets/slime.png'
            self.h=14*2
            self.w=19*2
            self.hp=50*(1+0.07*buff)
            self.maxhp=50*(1+0.07*buff)
            self.range=130
            self.view=400
            self.dmg=5*(1+0.05*buff)
        
        self.faketargetx=self.x
        self.faketargety=self.y
        self.skill=False
        self.skillduration=0
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
class Slimepath:
    def __init__(self,x,y,type):
        self.x=x
        self.y=y
        self.h=14*2
        self.w=19*2
        self.img='assets/slimepath.png'
        self.img=pygame.image.load(self.img).convert_alpha()
        self.img=pygame.transform.scale(self.img,(self.w,self.h))
        self.rect=pygame.Rect(self.x,self.y,self.w,self.h)
        self.duration=0
    def draw(self,screen):
        screen.blit(self.img,(self.x,self.y))
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
    def warn(self,transparentscreen,screen):
        pygame.draw.rect(transparentscreen,(225,0,0,20),(self.x,self.y,self.w,self.w*87/70))
        screen.blit(transparentscreen,(0,0))
    def update(self,screen):
        screen.blit(self.img,(self.x,self.y))
        self.rect=pygame.Rect(self.x,self.y,self.w,self.w*87/70)
class Regen:
    def __init__(self,x,y,type):
        self.x=x
        self.y=y
        self.duration=0
        self.type=type
        if type=='health':
            self.img='assets/healthregen.png'
        elif type=='mana':
            self.img='assets/manaregen.png'
        self.img=pygame.image.load(self.img).convert_alpha()
        self.img=pygame.transform.scale(self.img,(61,107))
    def draw(self,screen,dt):
        self.duration+=dt
        screen.blit(self.img,(self.x,self.y-self.duration*50))
        

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
        self.stage='normal'
        self.player=Player()
        self.bosses=[]
        self.pluses=[]
        #end and start
        self.startwrite=0
        self.writeduration=0
        self.changeline=1
        #guid
        self.guidenumber=1
        #self.guiding=1 #is guiding
        self.endchat=0 #chat not end

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
        self.slimes=[]
        self.bullets=[]
        self.smallbullets=[]
        self.slimepaths=[]
        self.slashes=[]
        self.mapstay=0
        self.bossattacks=[]
        self.regens=[]

class Linestat:
    def __init__(self):
        self.line='just for save'
        self.font=pygame.font.Font('assets/font.ttf',30)
        self.color=(0,0,0)
        self.x=0
        self.y=0


def getinfo(x):
    return str(x)        
        
        
chat_info={
    'start':{
        'line1':{
            'line':'Lost soul',
            'font': titlefont,
            'color':(111,13,181),
            'x': 30,
            'y': 5
                 },
        'line2':{
            'line':'adventure',
            'font': codefont,
            'color':(111,13,181),
            'x': 50,
            'y': 150
                 },
        'line3':{
            'line':'combat',
            'font': codefont,
            'color':(111,13,181),
            'x': 50,
            'y': 250
                 },
        'line4':{
            'line':'level up',
            'font': codefont,
            'color':(111,13,181),
            'x': 50,
            'y': 350
                 },
        'line5':{
            'line':'survive as long as you can',
            'font': codefont,
            'color':(111,13,181),
            'x': 50,
            'y': 450
                 },
        'line6':{
            'line':'press P to start>>',
            'font': codefont,
            'color':(111,13,181),
            'x': 50,
            'y': 550
                 },
    },
    'end':{
        'line1':{
            'line':'You dead!',
            'font': titlefont,
            'color':(111,13,181),
            'x': 30,
            'y': 5
                 },
        'line2':{
            'line':lambda a:'level '+getinfo(a),
            'font': codefont,
            'color':(111,13,181),
            'x': 50,
            'y': 150
                 },
        'line3':{
            'line':lambda a:'wave '+getinfo(a),
            'font': codefont,
            'color':(111,13,181),
            'x': 50,
            'y': 250
                 },
        'line4':{
            'line':lambda a:'map '+getinfo(a),
            'font': codefont,
            'color':(111,13,181),
            'x': 50,
            'y': 350
                 },
        'line5':{
            'line':lambda a:'enemy killed: '+getinfo(a),
            'font': codefont,
            'color':(111,13,181),
            'x': 50,
            'y': 450
                 },
        'line6':{
            'line':lambda a:'boss killed: '+getinfo(a),
            'font': codefont,
            'color':(111,13,181),
            'x': 50,
            'y': 550
                 },
        'line7':{
            'line':'press R to replay >>',
            'font': codefont,
            'color':(111,13,181),
            'x': 50,
            'y': 650
                 },                
    },
    'guide':{
        1:{
            'line1':{
                'line':'this is your character, you will',
                'font': chatfont,
                'color':(111,13,181),
                'x': 385,
                'y': 235
                    },
            'line2':{
                'line':'control him by WASD',
                'font': chatfont,
                'color':(111,13,181),
                'x': 385,
                'y': 275
                    },        
        },
        2:{
            'line1':{
                'line':'This is your mana and your health',
                'font': chatfont,
                'color':(111,13,181),
                'x': 385,
                'y': 235
                    },
            'line2':{
                'line':'point',
                'font': chatfont,
                'color':(111,13,181),
                'x': 385,
                'y': 275
                    },        
        },
        3:{
            'line1':{
                'line':'left arrow and right arrow to attack',
                'font': chatfont,
                'color':(111,13,181),
                'x': 385,
                'y': 235
                    },
            'line2':{
                'line':'each time cost an amount of mana',
                'font': chatfont,
                'color':(111,13,181),
                'x': 385,
                'y': 275
                    },        
        },
        4:{
            'line1':{
                'line':'slower mana slower moving, moving',
                'font': chatfont,
                'color':(111,13,181),
                'x': 385,
                'y': 235
                    },
            'line2':{
                'line':'make the mana regen more slowly',
                'font': chatfont,
                'color':(111,13,181),
                'x': 385,
                'y': 275
                    },        
        },
        5:{
            'line1':{
                'line':'you can go to next map through path',
                'font': chatfont,
                'color':(111,13,181),
                'x': 385,
                'y': 235
                    },
            'line2':{
                'line':'other than the one you entered',
                'font': chatfont,
                'color':(111,13,181),
                'x': 385,
                'y': 275
                    },     
        },
        6:{
            'line1':{
                'line':'each time you get into a new map',
                'font': chatfont,
                'color':(111,13,181),
                'x': 385,
                'y': 235
                    },
            'line2':{
                'line':'your player mana regen all',
                'font': chatfont,
                'color':(111,13,181),
                'x': 385,
                'y': 275
                    },     
        },
        7:{
            'line1':{
                'line':'each group of enemy borned, call',
                'font': chatfont,
                'color':(111,13,181),
                'x': 385,
                'y': 235
                    },
            'line2':{
                'line':'a wave',
                'font': chatfont,
                'color':(111,13,181),
                'x': 385,
                'y': 275
                    },     
        },
        8:{
            'line1':{
                'line':'after 4 waves of normal enemy, you',
                'font': chatfont,
                'color':(111,13,181),
                'x': 385,
                'y': 235
                    },
            'line2':{
                'line':'will meet a boss',
                'font': chatfont,
                'color':(111,13,181),
                'x': 385,
                'y': 275
                    },     
        },
        9:{
            'line1':{
                'line':'this is your experience bar, present',
                'font': chatfont,
                'color':(111,13,181),
                'x': 385,
                'y': 235
                    },
            'line2':{
                'line':'level and target level',
                'font': chatfont,
                'color':(111,13,181),
                'x': 385,
                'y': 275
                    },     
        },
        10:{
            'line1':{
                'line':'kill enemy will give you experience',
                'font': chatfont,
                'color':(111,13,181),
                'x': 385,
                'y': 235
                    },
            'line2':{
                'line':'point rely on which type of enemy',
                'font': chatfont,
                'color':(111,13,181),
                'x': 385,
                'y': 275
                    },     
        },
        11:{
            'line1':{
                'line':'clear stage also give you a big',
                'font': chatfont,
                'color':(111,13,181),
                'x': 385,
                'y': 235
                    },
            'line2':{
                'line':'amount of experience point',
                'font': chatfont,
                'color':(111,13,181),
                'x': 385,
                'y': 275
                    },     
        },
        12:{
            'line1':{
                'line':'after each level up, you have 2',
                'font': chatfont,
                'color':(111,13,181),
                'x': 385,
                'y': 235
                    },
            'line2':{
                'line':'points to upgrade your player stats',
                'font': chatfont,
                'color':(111,13,181),
                'x': 385,
                'y': 275
                    },     
        },
        13:{
            'line1':{
                'line':'ready to start?, press T to play',
                'font': chatfont,
                'color':(111,13,181),
                'x': 385,
                'y': 235
                    },
            'line2':{
                'line':'',
                'font': chatfont,
                'color':(111,13,181),
                'x': 385,
                'y': 275
                    },     
        },
    },
}

stayline_info={
    'guide':{
            'line1':{
                'line':'K to skip',
                'font': smallfont,
                'color':(227,206,14),
                'x': 385,
                'y': 460
                     },
            'line2':{
                'line':'T to test',
                'font': smallfont,
                'color':(227,206,14),
                'x': 925,
                'y': 460
                     },        
        },
    'test':{
            'line1':{
                'line':'K to skip',
                'font': smallfont,
                'color':(227,206,14),
                'x': 385,
                'y': 460
                     },
            'line2':{
                'line':'G to next guide',
                'font': smallfont,
                'color':(227,206,14),
                'x': 875,
                'y': 460
                     },        
        },
}









