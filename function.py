import pygame
import random
import math
from information import *

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
smallfont=pygame.font.Font('assets/endfont.ttf',15)





def write(text,font,color,x,y):
    screen.blit(font.render(text,True,color),(x,y))
def donothing():
    pass

def render1(msto,csto):
    if not csto.firstdoor:
        doorlong=random.randint(1,5)
        doorside=random.choice([-1,1,-2,2])
        csto.firstdoor.append(doorside)
        csto.firstdoor.append(doorlong)
        if doorside==(-1):
            firstexactdoor=random.choice(list(range(19,189+1-doorlong*10,10)))
            csto.firstdoor.append(firstexactdoor)                
            for i in range(0,doorlong):   
                msto.map.append(Map(firstexactdoor+i*10,'f'))
                msto.locate.remove(firstexactdoor+i*10)
                msto.door.append(firstexactdoor+i*10)
        elif doorside==(1):
            firstexactdoor=random.choice(list(range(10,180+1-doorlong*10,10)))
            csto.firstdoor.append(firstexactdoor)
            for i in range(0,doorlong):
                msto.map.append(Map(firstexactdoor+i*10,'f'))
                msto.locate.remove(firstexactdoor+i*10)
                msto.door.append(firstexactdoor+i*10)    
        elif doorside==(2):
            firstexactdoor=random.choice(list(range(1,8+1-doorlong)))
            csto.firstdoor.append(firstexactdoor)
            for i in range(0,doorlong):
                msto.map.append(Map(firstexactdoor+i,'f'))
                msto.locate.remove(firstexactdoor+i)
                msto.door.append(firstexactdoor+i)                
        elif doorside==(-2):
            firstexactdoor=random.choice(list(range(191,198+1-doorlong)))
            csto.firstdoor.append(firstexactdoor)
            for i in range(0,doorlong):
                msto.map.append(Map(firstexactdoor+i,'f'))
                msto.locate.remove(firstexactdoor+i)
                msto.door.append(firstexactdoor+i)
        csto.player.put(random.choice(msto.door))
    else:
        doorlong=csto.firstdoor[1]
        doorside=csto.firstdoor[0]*(-1)
        if doorside==(-1):
            firstexactdoor=random.choice(list(range(19,189+1-doorlong*10,10)))
            for i in range(0,doorlong):   
                msto.map.append(Map(firstexactdoor+i*10,'f'))
                msto.locate.remove(firstexactdoor+i*10)
                msto.door.append(firstexactdoor+i*10)
        elif doorside==(1):
            firstexactdoor=random.choice(list(range(10,180+1-doorlong*10,10)))
            for i in range(0,doorlong):
                msto.map.append(Map(firstexactdoor+i*10,'f'))
                msto.locate.remove(firstexactdoor+i*10)
                msto.door.append(firstexactdoor+i*10)    
        elif doorside==(2):
            firstexactdoor=random.choice(list(range(1,8+1-doorlong)))
            for i in range(0,doorlong):
                msto.map.append(Map(firstexactdoor+i,'f'))
                msto.locate.remove(firstexactdoor+i)
                msto.door.append(firstexactdoor+i)                
        elif doorside==(-2):
            firstexactdoor=random.choice(list(range(191,198+1-doorlong)))
            for i in range(0,doorlong):
                msto.map.append(Map(firstexactdoor+i,'f'))
                msto.locate.remove(firstexactdoor+i)
                msto.door.append(firstexactdoor+i)
        csto.player.put(random.choice(msto.door))

    start=random.choice(msto.door)
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
    msto.map.append(Map(start,'f'))    
    msto.locate.remove(start)
    doorban.extend(msto.door)            
    c=0
    doorside=0
    doorlong=0
    startablefloor=[]
    csto.firstdoor.clear()
    msto.goable.clear()
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
            if (start+b) in msto.locate and not (start+b) in doorban:
                side=0
                c=0
                d=list(range(1,9))+list(range(10,190,10))+list(range(19,199,10))+list(range(191,199))
                if (start+b) in d:
                    if (start+b) in list(range(1,9)):
                        if doorside==0: 
                            doorside=2
                            msto.door.append(start+b)
                            msto.goable.append(Goable(start+b))
                        elif doorside!=2:                            
                            break
                        elif unablemeetagain:
                            break
                        else:
                            doorlong+=1
                            msto.door.append(start+b)
                            msto.goable.append(Goable(start+b))
                        if doorlong==5:
                            doorlong-=1
                            if Goable(start+b) in msto.goable: msto.goable.remove(Goable(start+b))
                            break
                        side=1
                    elif (start+b) in list(range(10,190,10)):
                        if doorside==0: 
                            doorside=1
                            msto.door.append(start+b)
                            msto.goable.append(Goable(start+b))
                        elif doorside!=1:                             
                            break
                        elif unablemeetagain:
                            break
                        else:
                            doorlong+=1
                            msto.door.append(start+b)
                            msto.goable.append(Goable(start+b))
                        if doorlong==5:
                            doorlong-=1
                            if Goable(start+b) in msto.goable: msto.goable.remove(Goable(start+b))
                            break
                        side=1
                    elif (start+b) in list(range(19,199,10)):
                        if doorside==0: 
                            doorside=-1
                            msto.door.append(start+b)
                            msto.goable.append(Goable(start+b))
                        elif doorside!=(-1):                          
                            break
                        elif unablemeetagain:
                            break
                        else:
                            doorlong+=1
                            msto.door.append(start+b)
                            msto.goable.append(Goable(start+b))
                        if doorlong==5:
                            doorlong-=1
                            if Goable(start+b) in msto.goable: msto.goable.remove(Goable(start+b))
                            break
                        side=1
                    elif (start+b) in list(range(191,199)):
                        if doorside==0: 
                            doorside=-2
                            msto.door.append(start+b)
                            msto.goable.append(Goable(start+b))
                        elif doorside!=(-2):
                            break
                        elif unablemeetagain:
                            break
                        else:
                            doorlong+=1
                            msto.door.append(start+b)
                            msto.goable.append(Goable(start+b))
                        if doorlong==5:
                            doorlong-=1
                            if Goable(start+b) in msto.goable: msto.goable.remove(Goable(start+b))
                            break
                        side=1
                start+=b
                msto.map.append(Map(start,'f'))
                msto.locate.remove(start)
                if side==0: startablefloor.append(start)  
            else:
                c=b
        c=0
        if doorside!=0:
            if len(msto.locate)<=130:
                break
            else:
                doorban.extend(d)
        while True:
            start=random.choice(startablefloor)
            if ((start+1) in msto.locate and not (start+1) in doorban) or ((start-1) in msto.locate and not (start-1) in doorban) or ((start+10) in msto.locate and not (start+10) in doorban) or ((start-10) in msto.locate and not (start-10) in doorban):
                break
            else:
                startablefloor.remove(start)
    csto.firstdoor.append(doorside)
    csto.firstdoor.append(doorlong+1)   
    csto.rendermap=False
    for i in msto.map:
        msto.insidef.append(i.position)
    for i in msto.insidef:
        if not i in list(range(10,190,10)):
            i-=1
            if i in msto.locate:
                msto.locate.remove(i)
                if i-1 in msto.locate:
                    msto.wall.append(Map(i,'w'))
                    msto.w.append(i)
                else:
                    if i in d:
                        msto.wall.append(Map(i,'w'))
                        msto.w.append(i)
                    else:                        
                        msto.map.append(Map(i,'f'))
                        msto.insidef.append(i)
    for i in msto.insidef:
        if not i in list(range(1,9)):
            i-=10
            if i in msto.locate:
                msto.sr.append(i)
    for i in msto.w:
        if not i in list(range(1,9)):
            i-=10
            if i in msto.locate:
                msto.sr.append(i)
    for i in msto.insidef:
        if not i in list(range(191,199)):
            i+=10
            if i in msto.locate:
                if i in msto.sr:
                    msto.slr.append(i)
                    msto.sr.remove(i)
                else:
                    msto.sl.append(i)
    for i in msto.w:
        if not i in list(range(191,199)):
            i+=10
            if i in msto.locate:
                if i in msto.sr:
                    msto.slr.append(i)
                    msto.sr.remove(i)
                else:
                    msto.sl.append(i)
    for i in msto.insidef:
        if not i in list(range(19,199,10)) and not i==0:
            i+=1
            if i in msto.locate:
                if i in msto.sr:
                    msto.srt.append(i)
                    msto.sr.remove(i)
                elif i in msto.sl:
                    msto.slt.append(i)
                    msto.sl.remove(i)
                elif i in msto.slr:
                    msto.slrt.append(i)
                    msto.slr.remove(i)                            
                else:
                    msto.st.append(i)
                    
    for i in msto.locate:
        msto.v.append(i)
    if msto.v:
        for i in msto.v:
            msto.obstacle.append(Obstacle(i,'v'))
    if msto.sr:
        for i in msto.sr:
            msto.locate.remove(i)
            msto.obstacle.append(Obstacle(i,'sr'))
    if msto.sl:
        for i in msto.sl:
            msto.locate.remove(i)
            msto.obstacle.append(Obstacle(i,'sl'))
    if msto.slr:
        for i in msto.slr:
            msto.locate.remove(i)
            msto.obstacle.append(Obstacle(i,'slr'))
    if msto.slrt:
        for i in msto.slrt:
            msto.locate.remove(i)
            msto.obstacle.append(Obstacle(i,'slrt'))
    if msto.slt:
        for i in msto.slt:
            msto.locate.remove(i)
            msto.obstacle.append(Obstacle(i,'slt'))
    if msto.srt:
        for i in msto.srt:
            msto.locate.remove(i)
            msto.obstacle.append(Obstacle(i,'srt'))
    if msto.st:
        for i in msto.st:
            msto.locate.remove(i)
            msto.obstacle.append(Obstacle(i,'st'))
def render2(msto,csto):
    csto.bosses.append(Boss(csto.wave))
    for i in range(1,199):
        if i%10==1:
            msto.wall.append(Map(i,'w'))
        else:
            msto.map.append(Map(i,'f'))
    for i in range(1,9):
        msto.obstacle.append(Obstacle(i,'sr'))
    for i in range(191,199):
        msto.obstacle.append(Obstacle(i,'sl'))
    for i in range(19,199,10):
        msto.obstacle.append(Obstacle(i,'st'))
    for i in range(0,200,10):
        msto.obstacle.append(Obstacle(i,'v'))
    msto.obstacle.append(Obstacle(9,'v'))
    msto.obstacle.append(Obstacle(199,'v'))
    csto.player.put(12)          
def render3(msto,csto):
        csto.player.put(99)
        for i in range(1,199):
            if i%10==1 and i!=91 and i!=101:
                msto.wall.append(Map(i,'w'))
            else:
                msto.map.append(Map(i,'f'))
        for i in range(1,9):
            msto.obstacle.append(Obstacle(i,'sr'))
        for i in range(191,199):
            msto.obstacle.append(Obstacle(i,'sl'))
        for i in range(19,199,10):
            if i!=99 and i!=109 and i!=119 and i!=89:
                msto.obstacle.append(Obstacle(i,'st'))
        for i in range(0,200,10):
            if i!=90 and i!=100 and i!=80 and i!=110:
                msto.obstacle.append(Obstacle(i,'v'))
        msto.obstacle.append(Obstacle(9,'v'))
        msto.obstacle.append(Obstacle(199,'v'))
        msto.obstacle.append(Obstacle(80,'sr'))
        msto.obstacle.append(Obstacle(110,'sl'))
        msto.obstacle.append(Obstacle(89,'srt'))
        msto.obstacle.append(Obstacle(119,'slt'))
        msto.obstacle.append(Obstacle(143,'srt'))
        msto.obstacle.append(Obstacle(53,'slt'))
        for i in range(63,143,10):
            msto.obstacle.append(Obstacle(i,'st'))
        for i in range(54,57):
            msto.obstacle.append(Obstacle(i,'sl'))
        for i in range(144,147):
            msto.obstacle.append(Obstacle(i,'sr'))
        for i in range(66,146,10):
            msto.obstacle.append(Obstacle(i,'v'))
        for i in range(64,144,10):
            msto.obstacle.append(Obstacle(i,'v'))
        for i in range(65,145,10):
            msto.obstacle.append(Obstacle(i,'v'))
        for i in range(57,157,10):
            msto.wall.append(Map(i,'w'))

def playerbehave(msto,csto,dt,keys):
    csto.creepspeed=50*(1+0.01*csto.wave)
    csto.player.speed=csto.creepspeed-10+(csto.player.maxspeed-csto.creepspeed)*(csto.player.mana/(csto.player.maxmana))
    csto.player.sloweffect=0
    for i in msto.slimepaths:
        if i.rect.colliderect(csto.player.rect):
            csto.player.sloweffect=1
            break
    csto.player.speed-=csto.player.sloweffect*0.7*csto.player.speed
    csto.player.targetx=csto.player.x
    csto.player.targety=csto.player.y
    if keys[pygame.K_a]:
        csto.player.targetx=csto.player.x-1
        csto.player.checkwall()
        for i in msto.obstacle:
            if i.rect.colliderect(csto.player.wallrect):
                csto.player.targetx=csto.player.x
                csto.player.checkwall()
    if keys[pygame.K_d]:
        csto.player.targetx=csto.player.x+1
        csto.player.checkwall()
        for i in msto.obstacle:
            if i.rect.colliderect(csto.player.wallrect):
                csto.player.targetx=csto.player.x
                csto.player.checkwall() 
    if keys[pygame.K_w]:
        csto.player.targety=csto.player.y-1
        csto.player.checkwall()
        for i in msto.obstacle:
            if i.rect.colliderect(csto.player.wallrect):
                csto.player.targety=csto.player.y
                csto.player.checkwall()
    if keys[pygame.K_s]:
        csto.player.targety=csto.player.y+1
        csto.player.checkwall()
        for i in msto.obstacle:
            if i.rect.colliderect(csto.player.wallrect):
                csto.player.targety=csto.player.y
                csto.player.checkwall()
                
    if keys[pygame.K_LEFT] and csto.player.slashcooldown<=0 and csto.player.mana>=6:
        csto.player.mana-=6
        msto.slashes.append(Slash(csto.player.x,csto.player.y-(107-70),'left',csto.player.dmg))
        csto.player.slashcooldown=1-csto.player.attackspeed
        for creep in msto.creeps+msto.slimes:
            creep.takedame=True
        if csto.bosses:
            for boss in csto.bosses:
                boss.takedame=True
                            
    if keys[pygame.K_RIGHT] and csto.player.slashcooldown<=0 and csto.player.mana>=6:
        csto.player.mana-=6
        msto.slashes.append(Slash(csto.player.x,csto.player.y-(107-70),'right',csto.player.dmg))
        csto.player.slashcooldown=1-csto.player.attackspeed
        for creep in msto.creeps+msto.slimes:
            creep.takedame=True
        if csto.bosses:
            for boss in csto.bosses:
                boss.takedame=True
    for i in msto.slashes:
        i.present+=dt
        if i.present>=0.1:
            msto.slashes.remove(i)
            for creep in msto.creeps:
                creep.takedame=False
    if not msto.slashes: csto.player.slashcooldown-=dt
    if csto.player.mana<csto.player.maxmana:
        csto.player.mana+=csto.player.manaregen*dt
        if csto.player.mana>csto.player.maxmana:
            csto.player.mana=csto.player.maxmana
    
            
    
    csto.player.move(dt)
    csto.player.update()
    
    if csto.player.exp>=(90+25*(csto.player.level-1)+5*(csto.player.level-1)**2):
        csto.player.level+=1
        csto.player.exp-=(90+25*(csto.player.level-1)+5*(csto.player.level-1)**2)
        csto.player.buffstat+=2
    if csto.player.buffstat==0:
        if csto.pluses: csto.pluses=[]
def buff(csto,click,mousepos):
    if csto.player.buffstat>0:
        if not csto.pluses:
            csto.pluses.append(Plus('dmg'))
            csto.pluses.append(Plus('maxmana'))
            csto.pluses.append(Plus('maxhp'))
            csto.pluses.append(Plus('movespeed'))
            csto.pluses.append(Plus('manaregen'))
            csto.pluses.append(Plus('attackspeed'))
        for plus in csto.pluses:
            if click:
                if plus.rect.collidepoint(mousepos):
                    csto.player.buffstat-=1
                    if plus.type=='dmg':
                        csto.player.dmg+=1
                    elif plus.type=='maxmana':
                        csto.player.maxmana+=15
                        csto.player.mana+=15
                    elif plus.type=='maxhp':
                        csto.player.maxhp+=35
                        csto.player.hp+=15
                    elif plus.type=='movespeed':
                        csto.player.maxspeed+=1                        
                    elif plus.type=='manaregen':
                        csto.player.manaregen+=1
                    elif plus.type=='attackspeed':
                        csto.player.attackspeed+=0.03
    else:
        csto.pluses.clear()

def creeprandom(creep,msto,csto,dt,chase):
    creep.tested='none'
    creep.targetx=creep.x
    creep.targety=creep.y
    if creep.touchwall:
        creep.randomx=random.choice([-1,1])
        creep.randomy=random.choice([-1,1])
        creep.touchwall=False
    if creep.randomx!=0:
        creep.targetx=creep.x+creep.randomx
        creep.checkwall()
        for i in msto.obstacle:
            if i.rect.colliderect(creep.wallrect):
                creep.targetx=creep.x
                creep.touchwall=True
                creep.checkwall()
                creep.notry=False
                break    
    if creep.randomy!=0:
        creep.targety=creep.y+creep.randomy
        creep.checkwall()
        for i in msto.obstacle:
            if i.rect.colliderect(creep.wallrect):
                creep.targety=creep.y
                creep.touchwall=True
                creep.checkwall()
                creep.notry=False
                break
    if creep.x<=0+5 or creep.x>=(1400-creep.w)-5 or creep.y<=(70-creep.h)+5 or creep.y>=700-creep.h-5:
        creep.touchwall=True
        creep.notry=False
    creep.move(dt)
    creep.update()
    creep.faketargetx=creep.x
    creep.faketargety=creep.y
def creepmove(creep,msto,csto,dt,chase):
    if creep.touchwally and creep.touchwallx:
        if creep.testx and not creep.tested=='x2':
            if creep.tested=='none':
                creep.tested='x1'
                creep.randomx*=(-1)
                creep.touchwallx=False                
            elif creep.tested=='x1':
                creep.tested='x2'            
        elif creep.testy and not creep.tested=='y2':
            if creep.tested=='none':
                creep.tested='y1'
                creep.randomy*=(-1)
                creep.touchwally=False
            elif creep.tested=='y1':
                creep.tested='y2'                        
        else:
            if chase==1:
                creep.notry=True
                creep.touchwallx=False
                creep.touchwally=False
            else:
                if creep.tested=='none':
                    creep.testy=True
                elif creep.tested=='x2':
                    creep.testy=True
                elif creep.tested=='y2':
                    creep.testx=True                               
    elif creep.testx:
        if creep.tested=='none':
            creep.tested='x1'
        creep.targetx=creep.x
        creep.targety=creep.y
        creep.testx=False
        creep.touchwallx=False
        creep.touchwally=False
        creep.targetx=creep.x+creep.randomx*chase
        creep.checkwall()
        for i in msto.obstacle:
            if i.rect.colliderect(creep.wallrect):
                creep.targetx=creep.x
                creep.touchwallx=True     
                creep.checkwall()
                break
        if csto.player.y-creep.y>0:
            creep.randomy=1
        elif csto.player.y-creep.y<0:
            creep.randomy=-1
        creep.targety=creep.y+creep.randomy*chase
        creep.checkwall()
        for i in msto.obstacle:
            if i.rect.colliderect(creep.wallrect):
                creep.targety=creep.y
                creep.touchwally=True
                creep.checkwall()
                creep.testx=True
                break
        if creep.x<=0+5 or creep.x>=(1400-creep.w)-5:
            creep.touchwallx=True
        if creep.y<=(70-creep.h)+5 or creep.y>=700-creep.h-5:
            creep.touchwally=True
    elif creep.testy:
        if creep.tested=='none':
            creep.tested='x1'
        creep.targetx=creep.x
        creep.targety=creep.y                    
        creep.testy=False
        creep.touchwallx=False
        creep.touchwally=False
        if csto.player.x-creep.x>0:
            creep.randomx=1
        elif csto.player.x-creep.x<0:
            creep.randomx=-1                    
        creep.targetx=creep.x+creep.randomx*chase
        creep.checkwall()
        for i in msto.obstacle:
            if i.rect.colliderect(creep.wallrect):
                creep.targetx=creep.x
                creep.touchwallx=True     
                creep.checkwall()
                creep.testy=True
                break
        creep.targety=creep.y+creep.randomy*chase
        creep.checkwall()
        for i in msto.obstacle:
            if i.rect.colliderect(creep.wallrect):
                creep.targety=creep.y
                creep.touchwally=True
                creep.checkwall()
                break
        if creep.x<=0+5 or creep.x>=(1400-creep.w)-5:
            creep.touchwallx=True
        if creep.y<=(70-creep.h)+5 or creep.y>=700-creep.h-5:
            creep.touchwally=True
    else:
        creep.tested='none'
        creep.targetx=creep.x
        creep.targety=creep.y                    
        creep.touchwallx=False
        creep.touchwally=False
        if csto.player.x-creep.x>0:
            creep.randomx=1
        elif csto.player.x-creep.x<0:
            creep.randomx=-1
        creep.targetx=creep.x+creep.randomx*chase
        creep.checkwall()
        for i in msto.obstacle:
            if i.rect.colliderect(creep.wallrect):
                creep.targetx=creep.x
                creep.touchwallx=True     
                creep.checkwall()
                break
        if csto.player.y-creep.y>0:
            creep.randomy=1
        elif csto.player.y-creep.y<0:
            creep.randomy=-1
        creep.targety=creep.y+creep.randomy*chase
        creep.checkwall()
        for i in msto.obstacle:
            if i.rect.colliderect(creep.wallrect):
                creep.targety=creep.y
                creep.touchwally=True
                creep.checkwall()
                break
        if creep.x<=0+5 or creep.x>=(1400-creep.w)-5:
            creep.touchwallx=True
        if creep.y<=(70-creep.h)+5 or creep.y>=700-creep.h-5:
            creep.touchwally=True
        if creep.touchwally and int(creep.x)==int(csto.player.x) and not creep.touchwallx:
            creep.testx=True
            creep.randomx=1 if csto.player.x-creep.x>=0 else -1
        if creep.touchwallx and int(creep.y)==int(csto.player.y) and not creep.touchwally:
            creep.testy=True
            creep.randomy=1 if csto.player.y-creep.y>=0 else -1
    creep.move(dt)
    creep.update()            
def creepshoot(creep,msto,csto,dt):
    creep.shoot+=dt
    if creep.shoot>=2.5:
        msto.bullets.append(Bullet(creep.x,creep.y,csto.player.x,csto.player.y,creep.dmg))
        creep.shoot=0
def creepspawn(msto,csto):
    csto.wave+=1
    if csto.wave%5==0:
        csto.stage='boss'
        csto.rendermap=True
    else:
        creepsquare=random.sample(msto.insidef,int(len(msto.insidef)/12*(1+0.5*msto.mapstay)))
        msto.mapstay+=1
        for i in creepsquare:
            if i%2==0:
                msto.creeps.append(Creep(i,'normal',csto.wave))
            else:
                msto.slimes.append(Creep(i,'slime',csto.wave))
        msto.creeps.append(Creep(random.choice(msto.insidef),'elite',csto.wave))
def creepgetdame(msto,csto):
    for creep in msto.creeps + msto.slimes:
        if creep.rect.colliderect(msto.slashes[0].rect) and creep.takedame:
            creep.hp-=msto.slashes[0].dmg
            creep.takedame=False
        if creep.hp<=0:
            if creep in msto.creeps: msto.creeps.remove(creep)
            if creep in msto.slimes: msto.slimes.remove(creep)
            csto.enemykilled+=1
            if creep.type=='normal':
                csto.player.exp+=12*(1+0.02*csto.wave)
            elif creep.type=='slime':
                csto.player.exp+=8*(1+0.02*csto.wave)
            elif creep.type=='elite':
                csto.player.exp+=30*(1+0.02*csto.wave)
            if len(msto.creeps)==0:
                csto.player.exp+=30*(1+0.02*csto.wave)

def slimemove(creep,msto,csto,dt,chase):
    if (int(creep.faketargetx)==int(creep.x) and int(creep.faketargety)==int(creep.y)) or creep.notry:
        testlist=list(range(-(creep.range-10),creep.range-10))
        while True:
            a=random.choice(testlist)
            creep.touchwallx=False
            creep.targetx=csto.player.x+a
            creep.checkwall()
            for i in msto.obstacle:
                if i.rect.colliderect(creep.wallrect):
                    if a in testlist: testlist.remove(a)
                    creep.touchwallx=True
                    break
            if not creep.touchwallx or not testlist: break
        testlist=list(range(-(creep.range-10),creep.range-10))
        while True:
            a=random.choice(testlist)
            creep.touchwally=False
            creep.targety=csto.player.y+a
            creep.checkwall()
            for i in msto.obstacle:
                if i.rect.colliderect(creep.wallrect):
                    if a in testlist: testlist.remove(a)
                    creep.touchwally=True
                    break
            if not creep.touchwally or not testlist: break
        creep.faketargetx=creep.targetx
        creep.faketargety=creep.targety
        creep.tested='none'
        creep.notry=False
    else:
        if creep.touchwally and creep.touchwallx:
            if creep.testx and not creep.tested=='x2':
                if creep.tested=='none':
                    creep.tested='x1'
                    creep.randomx*=(-1)
                    creep.touchwallx=False                
                elif creep.tested=='x1':
                    creep.tested='x2'
                    creep.notry=True            
            elif creep.testy and not creep.tested=='y2':
                if creep.tested=='none':
                    creep.tested='y1'
                    creep.randomy*=(-1)
                    creep.touchwally=False
                elif creep.tested=='y1':
                    creep.tested='y2'
                    creep.notry=True                        
            else:
                    creep.notry=True
                    creep.touchwallx=False
                    creep.touchwally=False                        
        elif creep.testx:
            if creep.tested=='none':
                creep.tested='x1'
            creep.targetx=creep.x
            creep.targety=creep.y
            creep.testx=False
            creep.touchwallx=False
            creep.touchwally=False
            creep.targetx=creep.x+creep.randomx*chase
            creep.checkwall()
            for i in msto.obstacle:
                if i.rect.colliderect(creep.wallrect):
                    creep.targetx=creep.x
                    creep.touchwallx=True     
                    creep.checkwall()
                    break
            if creep.faketargety-creep.y>0:
                creep.randomy=1
            elif creep.faketargety-creep.y<0:
                creep.randomy=-1
            creep.targety=creep.y+creep.randomy*chase
            creep.checkwall()
            for i in msto.obstacle:
                if i.rect.colliderect(creep.wallrect):
                    creep.targety=creep.y
                    creep.touchwally=True
                    creep.checkwall()
                    creep.testx=True
                    break
            if creep.x<=0+5 or creep.x>=(1400-creep.w)-5:
                creep.touchwallx=True
            if creep.y<=(70-creep.h)+5 or creep.y>=700-creep.h-5:
                creep.touchwally=True
        elif creep.testy:
            if creep.tested=='none':
                creep.tested='x1'
            creep.targetx=creep.x
            creep.targety=creep.y                    
            creep.testy=False
            creep.touchwallx=False
            creep.touchwally=False
            if creep.faketargetx-creep.x>0:
                creep.randomx=1
            elif creep.faketargetx-creep.x<0:
                creep.randomx=-1                    
            creep.targetx=creep.x+creep.randomx*chase
            creep.checkwall()
            for i in msto.obstacle:
                if i.rect.colliderect(creep.wallrect):
                    creep.targetx=creep.x
                    creep.touchwallx=True     
                    creep.checkwall()
                    creep.testy=True
                    break
            creep.targety=creep.y+creep.randomy*chase
            creep.checkwall()
            for i in msto.obstacle:
                if i.rect.colliderect(creep.wallrect):
                    creep.targety=creep.y
                    creep.touchwally=True
                    creep.checkwall()
                    break
            if creep.x<=0+5 or creep.x>=(1400-creep.w)-5:
                creep.touchwallx=True
            if creep.y<=(70-creep.h)+5 or creep.y>=700-creep.h-5:
                creep.touchwally=True
        else:
            creep.tested='none'
            creep.targetx=creep.x
            creep.targety=creep.y                    
            creep.touchwallx=False
            creep.touchwally=False
            if creep.faketargetx-creep.x>0:
                creep.randomx=1
            elif creep.faketargetx-creep.x<0:
                creep.randomx=-1
            creep.targetx=creep.x+creep.randomx*chase
            creep.checkwall()
            for i in msto.obstacle:
                if i.rect.colliderect(creep.wallrect):
                    creep.targetx=creep.x
                    creep.touchwallx=True     
                    creep.checkwall()
                    break
            if creep.faketargety-creep.y>0:
                creep.randomy=1
            elif creep.faketargety-creep.y<0:
                creep.randomy=-1
            creep.targety=creep.y+creep.randomy*chase
            creep.checkwall()
            for i in msto.obstacle:
                if i.rect.colliderect(creep.wallrect):
                    creep.targety=creep.y
                    creep.touchwally=True
                    creep.checkwall()
                    break
            if creep.x<=0+5 or creep.x>=(1400-creep.w)-5:
                creep.touchwallx=True
            if creep.y<=(70-creep.h)+5 or creep.y>=700-creep.h-5:
                creep.touchwally=True
            if creep.touchwally and int(creep.x)==int(csto.player.x) and not creep.touchwallx:
                creep.testx=True
                creep.randomx=1 if csto.player.x-creep.x>=0 else -1
            if creep.touchwallx and int(creep.y)==int(csto.player.y) and not creep.touchwally:
                creep.testy=True
                creep.randomy=1 if csto.player.y-creep.y>=0 else -1
    creep.move(dt)
    creep.update()   
def slimepath(creep,msto,csto,dt):
    msto.slimepaths.append(Slimepath(creep.x,creep.y,1))
def slimepathclear(msto,dt):
    for block in msto.slimepaths:
        block.duration+=dt
        if block.duration>=4.5:
            msto.slimepaths.remove(block)

def bossgetdame(msto,csto):
    if csto.bosses:
        boss=csto.bosses[0]
        if boss.rect.colliderect(msto.slashes[0].rect) and boss.takedame:
            boss.hp-=msto.slashes[0].dmg
            boss.takedame=False
        if boss.hp<=0:
            csto.bosses.remove(boss)
            csto.bosscount+=1
            csto.player.exp+=90*(1+0.02*csto.wave)
            csto.stage='normal'
            import pygame
            csto.rendermap=True 
def chooseskillboss(boss,msto,csto,dt):
    boss.skillchoose=random.randint(1,4)
    boss.skillprepare=0
def skillboss1(boss,msto,csto,dt):
    for i in range(0,360,int(360/(24+6*csto.bosscount))):
        msto.bullets.append(Bullet(boss.x+boss.w/2,boss.y+boss.h/2-18,boss.x+2000*math.cos(math.radians(i)),boss.y+2000*math.sin(math.radians(i)),boss.dmg))
        boss.cooldown=0
        boss.skillchoose=0  
def skillboss2(boss,msto,csto,dt):
    if boss.skillprepare==0:
        boss.targetx=csto.player.x
        boss.targety=csto.player.y
        boss.skillprepare=1
        csto.player.takedame=True
    else:
        boss.move(dt)
        boss.update()
        if boss.rect.colliderect(csto.player.rect) and csto.player.takedame:
            csto.player.hp-=boss.dmg
            csto.player.takedame=False
        if int(boss.x)==int(boss.targetx) and int(boss.y)==int(boss.targety):
            boss.skillchoose=0
            boss.cooldown=0
def skillboss3(boss,msto,csto,dt):               
    if boss.skillprepare==0:
        for i in range(8+2*csto.bosscount):
            msto.bossattacks.append(Bossattack(random.uniform(71,1329),random.uniform(141,629),0.6*boss.dmg,90+10*csto.bosscount))
    elif boss.skillprepare>=1:
        for bossattack in msto.bossattacks:
            if bossattack.rect.colliderect(csto.player.rect):
                csto.player.hp-=bossattack.dmg
                msto.bossattacks.remove(bossattack)
        if boss.skillprepare>=2:
            boss.skillchoose=0
            boss.cooldown=0
            msto.bossattacks.clear()
    boss.skillprepare+=dt
def skillboss4(boss,msto,csto,dt):             
    if boss.cooldown>=1.85:
        boss.cooldown=1.8
    if boss.skillprepare<360:
        msto.bullets.append(Bullet(boss.x+boss.w/2,boss.y+boss.h/2-18,boss.x+2000*math.cos(math.radians(boss.skillprepare)),boss.y+2000*math.sin(math.radians(boss.skillprepare)),boss.dmg))
        boss.skillprepare+=int(360/(24+6*csto.bosscount))
    else:    
        boss.skillchoose=0
        boss.cooldown=0           


def changemap(msto,csto):
    for i in msto.goable:
        if i.rect.colliderect(csto.player.rect):
            if csto.player.x<=0 or csto.player.x>=(1400-61) or csto.player.y<=-((107-70)-(107-70)) or csto.player.y>=((700-107)+(107-70)):
                csto.rendermap=True
                break
def changetestmap(msto,csto):
    if csto.player.y<=-((107-70)-(107-70)):
        csto.player.put(99)
        csto.player.mana=csto.player.maxmana


def bulleteffect(msto,csto,dt):
    for bullet in msto.bullets:
        bullet.move(dt)
        bullet.update()
        if bullet.rect.colliderect(csto.player.rect):
            csto.player.hp-=bullet.dmg
            msto.bullets.remove(bullet)
        elif bullet.x>=(1400-20) or bullet.x<=0 or bullet.y<=0 or bullet.y>=(700-20):
            msto.bullets.remove(bullet)
        else:
            for object in msto.obstacle:
                if bullet.wallrect.colliderect(object.rect):
                    msto.bullets.remove(bullet)
                    if csto.bosscount>=2 and csto.stage=='boss':
                        for i in range(0,360,int(360/(6+1*csto.bosscount))):
                            msto.smallbullets.append(Smallbullet(bullet.x,bullet.y,csto.bosses[0].x+2000*math.cos(math.radians(i)),csto.bosses[0].y+2000*math.sin(math.radians(i)),csto.bosses[0].dmg/2))        
                    break
def smallbulleteffect(msto,csto,dt):
    for bullet in msto.smallbullets:
        bullet.move(dt)
        bullet.update()
        if bullet.rect.colliderect(csto.player.rect):
            csto.player.hp-=bullet.dmg
            msto.smallbullets.remove(bullet)
        elif bullet.x>=(1400-20) or bullet.x<=0 or bullet.y<=0 or bullet.y>=(700-20):
            msto.bullets.remove(bullet)
        else:
            for object in msto.obstacle:
                if bullet.wallrect.colliderect(object.rect):
                    msto.smallbullets.remove(bullet)
                    break        
def slashbullet(msto,csto,dt):
    if msto.slashes:
        for bullet in msto.bullets:
            if bullet.rect.colliderect(msto.slashes[0].rect):
                msto.bullets.remove(bullet)                    
        for bullet in msto.smallbullets:
            if bullet.rect.colliderect(msto.slashes[0].rect):
                msto.smallbullets.remove(bullet)  

def startgame(csto,keys,msto,lstat,dt):
    if keys[pygame.K_p] and csto.changeline>6:
        csto.stage='guide'
        csto.rendermap=True
        returntype(msto,csto,lstat,dt)
    return csto
def replay(csto,keys,msto,lstat,dt):
    if keys[pygame.K_r] and csto.changeline>7:
        csto=Conststore()
        csto.stage='guide'
    return csto
def skip(csto,keys,msto,lstat,dt):
    if keys[pygame.K_k]:
        csto.stage='normal'
        csto.rendermap=True
        returntype(msto,csto,lstat,dt)   
    return csto

def drawgame1(msto,csto):
    screen.fill((70,70,70))
    transparentscreen.fill((0,0,0,0))
    for i in msto.map:
        i.draw(screen)
    for i in msto.wall:
        i.draw(screen)
    for i in msto.obstacle:
        i.draw(screen)
    for i in msto.slimepaths:
        i.draw(screen)
    for i in msto.creeps:
        i.draw(screen)
    for i in msto.slimes:
        i.draw(screen)
    write('HP',font,(0,0,0),40,699)
    write('MANA',font,(0,0,0),20,744)
    write('DAMAGE:'+str(csto.player.dmg),font,(0,0,0),450,699)
    write('MAX MANA:'+str(csto.player.maxmana),font,(0,0,0),450,744)
    write('MAX HP:'+str(csto.player.maxhp),font,(0,0,0),700,699)
    write('MOVE SPEED:'+str(csto.player.maxspeed),font,(0,0,0),700,744)
    write('MANA REGEN:'+str(csto.player.manaregen),font,(0,0,0),950,699)
    write('ATTACK SPEED:'+str(csto.player.attackspeed),font,(0,0,0),950,744)
    write('level',font,(0,0,0),1410,30)
    write(str(csto.player.level),font,(0,0,0),1430,70)
    write(str(csto.player.level+1),font,(0,0,0),1430,630)
    for i in csto.bosses:
        i.draw(screen)
        if msto.bossattacks:
            if i.skillprepare<1:
                for bossattack in msto.bossattacks:
                    bossattack.warn(transparentscreen,screen)
            elif i.skillprepare>=1:
                for bossattack in msto.bossattacks:
                    bossattack.update(screen)    
    csto.player.draw(screen)
    for i in msto.bullets:
        i.draw(screen)
    for i in msto.smallbullets:
        i.draw(screen)
    for i in msto.slashes:
        i.draw(screen)
    for i in csto.pluses:
        i.draw(screen)
    for i in msto.goable:
        pygame.draw.rect(screen,(225,0,0),i.rect,1)
def renewscreen(msto,csto):
    screen.fill((0,0,0))

def takeline(csto,number,lstat):
    lstat.line=chat_info.get(csto.stage).get('line'+str(number)).get('line')
    lstat.font=chat_info.get(csto.stage).get('line'+str(number)).get('font')
    lstat.color=chat_info.get(csto.stage).get('line'+str(number)).get('color')
    lstat.x=chat_info.get(csto.stage).get('line'+str(number)).get('x')
    lstat.y=chat_info.get(csto.stage).get('line'+str(number)).get('y')
def takelinevariables(csto,number,lstat):
    if number==1 or number==7:
        lstat.line=chat_info.get(csto.stage,lambda *b:'none').get('line'+str(number)).get('line')
    elif number==2:
        lstat.line=chat_info.get(csto.stage,lambda *b:'none').get('line'+str(number)).get('line')(csto.player.level)
    elif number==3:
        lstat.line=chat_info.get(csto.stage,lambda *b:'none').get('line'+str(number)).get('line')(csto.wave)
    elif number==4:
        lstat.line=chat_info.get(csto.stage,lambda *b:'none').get('line'+str(number)).get('line')(csto.mapcount)
    elif number==5:
        lstat.line=chat_info.get(csto.stage,lambda *b:'none').get('line'+str(number)).get('line')(csto.enemykilled)
    elif number==6:
        lstat.line=chat_info.get(csto.stage,lambda *b:'none').get('line'+str(number)).get('line')(csto.bosscount)
    lstat.font=chat_info.get(csto.stage,lambda *b:'none').get('line'+str(number)).get('font')
    lstat.color=chat_info.get(csto.stage,lambda *b:'none').get('line'+str(number)).get('color')
    lstat.x=chat_info.get(csto.stage,lambda *b:'none').get('line'+str(number)).get('x')
    lstat.y=chat_info.get(csto.stage,lambda *b:'none').get('line'+str(number)).get('y')
def takeguide(csto,number,lstat):
    lstat.line=chat_info.get(csto.stage).get(csto.guidenumber).get('line'+str(number)).get('line')
    lstat.font=chat_info.get(csto.stage).get(csto.guidenumber).get('line'+str(number)).get('font')
    lstat.color=chat_info.get(csto.stage).get(csto.guidenumber).get('line'+str(number)).get('color')
    lstat.x=chat_info.get(csto.stage).get(csto.guidenumber).get('line'+str(number)).get('x')
    lstat.y=chat_info.get(csto.stage).get(csto.guidenumber).get('line'+str(number)).get('y')
def smalltyping(csto,number,lstat):
    if csto.stage=='end': 
        takelinevariables(csto,number,lstat)
    elif csto.stage=='guide':
        takeguide(csto,number,lstat)
    else:    
        takeline(csto,number,lstat)
    if csto.writeduration<len(lstat.line) and csto.changeline==number:
        write(lstat.line[:csto.writeduration]+'_',lstat.font,lstat.color,lstat.x,lstat.y)
    elif csto.changeline>=number:
        write(lstat.line,lstat.font,lstat.color,lstat.x,lstat.y)
        if csto.changeline==number:
            csto.changeline+=1
            csto.writeduration=0
def typingstart(msto,csto,lstat,dt,lenofeachstage):
    if csto.changeline<=lenofeachstage: 
        csto.startwrite+=dt
        csto.endchat=0
    else:
        csto.endchat=1
    if csto.startwrite>=0.125:
        renewscreen(msto,csto)
        csto.startwrite=0
        csto.writeduration+=1
        for i in range(1,lenofeachstage+1):
            smalltyping(csto,i,lstat)
def returntype(msto,csto,lstat,dt):
    csto.startwrite=0
    csto.changeline=1
    csto.writeduration=0
    csto.endchat==0
def darken(msto,csto):
    drawgame1(msto,csto)
    transparentscreen.fill((0,0,0,210))
    if csto.guidenumber==12: csto.player.buffstat=2
    if csto.endchat==1: 
        if csto.guidenumber==1: pygame.draw.circle(transparentscreen,(225,225,225,0),(662,655),65)
        if csto.guidenumber==2: pygame.draw.rect(transparentscreen,(225,225,225,0),pygame.Rect(15,700,400,90))
        if csto.guidenumber==5: pygame.draw.circle(transparentscreen,(225,225,225,0),(700,20),100)
        if csto.guidenumber==4 or csto.guidenumber==6: csto.player.mana=0
        if csto.guidenumber==9: pygame.draw.rect(transparentscreen,(225,225,225,0),pygame.Rect(1410,30,80,650))
        if csto.guidenumber==12: pygame.draw.rect(transparentscreen,(225,225,225,0),pygame.Rect(445,700,755,90))
    screen.blit(transparentscreen)     
def guidetyping(msto,csto,lstat,dt,lenofeachstage):    
    csto.startwrite+=dt
    if csto.changeline<=lenofeachstage:
        csto.endchat=0
    else:
        csto.endchat=1
    if csto.startwrite>=0.1:
        csto.startwrite=0
        csto.writeduration+=1
        darken(msto,csto)
        for i in range(1,lenofeachstage+1):
            smalltyping(csto,i,lstat)
        stayline(msto,csto,lstat,dt) 
def gainconstline(csto,number,lstat):
    lstat.line=stayline_info.get(csto.stage).get('line'+str(number)).get('line')
    lstat.font=stayline_info.get(csto.stage).get('line'+str(number)).get('font')
    lstat.color=stayline_info.get(csto.stage).get('line'+str(number)).get('color')
    lstat.x=stayline_info.get(csto.stage).get('line'+str(number)).get('x')
    lstat.y=stayline_info.get(csto.stage).get('line'+str(number)).get('y')
def stayline(msto,csto,lstat,dt):
    for i in range(1,3):
        gainconstline(csto,i,lstat)
        write(lstat.line,lstat.font,lstat.color,lstat.x,lstat.y)

def guidetotest(csto):
    if csto.guidenumber<13:
        csto.stage='test'
        csto.guidenumber+=1
    else:
        csto.stage='normal'
        csto.player.buffstat=0
        csto.player=Player()
        csto.rendermap=True
def testtoguide(csto):
    csto.stage='guide'        
        
    
    
                