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





def write(text,font,color,x,y):
    screen.blit(font.render(text,True,color),(x,y))

def render1(map,locate,door,player,insidef,w,goable,sr,sl,srt,slt,slr,slrt,st,wall,v,obstacle,bosses,csto):
    if not csto.csto.firstdoor:
        doorlong=random.randint(1,5)
        doorside=random.choice([-1,1,-2,2])
        csto.csto.firstdoor.append(doorside)
        csto.csto.firstdoor.append(doorlong)
        if doorside==(-1):
            firstexactdoor=random.choice(list(range(19,189+1-doorlong*10,10)))
            csto.csto.firstdoor.append(firstexactdoor)                
            for i in range(0,doorlong):   
                map.append(Map(firstexactdoor+i*10,'F'))
                locate.remove(firstexactdoor+i*10)
                door.append(firstexactdoor+i*10)
        elif doorside==(1):
            firstexactdoor=random.choice(list(range(10,180+1-doorlong*10,10)))
            csto.csto.firstdoor.append(firstexactdoor)
            for i in range(0,doorlong):
                map.append(Map(firstexactdoor+i*10,'F'))
                locate.remove(firstexactdoor+i*10)
                door.append(firstexactdoor+i*10)    
        elif doorside==(2):
            firstexactdoor=random.choice(list(range(1,8+1-doorlong)))
            csto.csto.firstdoor.append(firstexactdoor)
            for i in range(0,doorlong):
                map.append(Map(firstexactdoor+i,'F'))
                locate.remove(firstexactdoor+i)
                door.append(firstexactdoor+i)                
        elif doorside==(-2):
            firstexactdoor=random.choice(list(range(191,198+1-doorlong)))
            csto.csto.firstdoor.append(firstexactdoor)
            for i in range(0,doorlong):
                map.append(Map(firstexactdoor+i,'F'))
                locate.remove(firstexactdoor+i)
                door.append(firstexactdoor+i)
        player.put(random.choice(door))
    else:
        doorlong=csto.csto.firstdoor[1]
        doorside=csto.csto.firstdoor[0]*(-1)
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
    csto.csto.firstdoor.clear()
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
    csto.csto.firstdoor.append(doorside)
    csto.csto.firstdoor.append(doorlong+1)   
    csto.rendermap=False
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
def render2(map,locate,door,player,insidef,w,goable,sr,sl,srt,slt,slr,slrt,st,wall,v,obstacle,bosses,csto):
    bosses.append(Boss(csto.csto.wave))
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
def render3(map,locate,door,player,insidef,w,goable,sr,sl,srt,slt,slr,slrt,st,wall,v,obstacle,bosses,csto):
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
def playerbehave(csto.wave,player,obstacle,keys,slashes,creeps,bosses,dt,pluses):
    csto.creepspeed=50*(1+0.01*csto.wave)
    player.speed=csto.creepspeed-10+(player.maxspeed-csto.creepspeed)*(player.mana/player.maxmana)
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
def creepspawn(insidef,creeps,csto.stage,csto.rendermap,csto.wave,mapstay):
    csto.wave+=1
    if csto.wave%5==0:
        csto.stage='boss'
        csto.rendermap=True
    else:
        creepsquare=random.sample(insidef,int(len(insidef)/12*(1+0.5*mapstay)))
        mapstay+=1
        for i in creepsquare:
            creeps.append(Creep(i,random.choice(['slime','normal']),csto.wave))
        creeps.append(Creep(random.choice(insidef),'elite',csto.wave))
    return csto.stage,csto.rendermap,csto.wave,mapstay
def creepgetdame(slashes,creeps,bosses,player,csto.wave,csto):
    for creep in creeps:
        if creep.rect.colliderect(slashes[0].rect) and creep.takedame:
            creep.hp-=slashes[0].dmg
            creep.takedame=False
        if creep.hp<=0:
            creeps.remove(creep)
            csto.enemykilled+=1
            if creep.type=='normal':
                player.exp+=12*(1+0.02*csto.wave)
            elif creep.type=='slime':
                player.exp+=8*(1+0.02*csto.wave)
            elif creep.type=='elite':
                player.exp+=30*(1+0.02*csto.wave)
            if len(creeps)==0:
                player.exp+=30*(1+0.02*csto.wave)
def bossgetdame(slashes,creeps,bosses,player,csto.wave,csto):
    boss=bosses[0]
    if boss.rect.colliderect(slashes[0].rect) and boss.takedame:
        boss.hp-=slashes[0].dmg
        boss.takedame=False
    if boss.hp<=0:
        bosses.remove(boss)
        csto.csto.bosscount+=1
        player.exp+=90*(1+0.02*csto.wave)
        csto.csto.stage='normal'
        import pygame
        csto.csto.rendermap=True 
def donothing():
    pass
def changemap(goable,player,csto.rendermap):
    for i in goable:
        if i.rect.colliderect(player.rect):
            if player.x<=0 or player.x>=(1400-61) or player.y<=-((107-70)-(107-70)) or player.y>=((700-107)+(107-70)):
                csto.rendermap=True
                break
    return csto.rendermap
def chooseskillboss(boss,bullets,player,dt,bossattacks,csto):
    boss.skillchoose=random.randint(1,4)
    boss.skillprepare=0
def skillboss1(boss,bullets,player,dt,bossattacks,csto):
    for i in range(0,360,int(360/(24+6*csto.csto.bosscount))):
        bullets.append(Bullet(boss.x+boss.w/2,boss.y+boss.h/2-18,boss.x+2000*math.cos(math.radians(i)),boss.y+2000*math.sin(math.radians(i)),boss.dmg))
        boss.cooldown=0
        boss.skillchoose=0  
def skillboss2(boss,bullets,player,dt,bossattacks,csto):
    if boss.skillprepare==0:
        boss.targetx=player.x
        boss.targety=player.y
        boss.skillprepare=1
        player.takedame=True
    else:
        boss.move(dt)
        boss.update()
        if boss.rect.colliderect(player.rect) and player.takedame:
            player.hp-=boss.dmg
            player.takedame=False
        if boss.x==boss.targetx and boss.y==boss.targety:
            boss.skillchoose=0
            boss.cooldown=0
def skillboss3(boss,bullets,player,dt,bossattacks,csto):               
    if boss.skillprepare==0:
        for i in range(8+2*csto.csto.bosscount):
            bossattacks.append(Bossattack(random.uniform(71,1329),random.uniform(141,629),0.6*boss.dmg,90+10*csto.csto.bosscount))
    elif boss.skillprepare>=1:
        for bossattack in bossattacks:
            if bossattack.rect.colliderect(player.rect):
                player.hp-=bossattack.dmg
                bossattacks.remove(bossattack)
        if boss.skillprepare>=2:
            boss.skillchoose=0
            boss.cooldown=0
            bossattacks.clear()
    boss.skillprepare+=dt
def skillboss4(boss,bullets,player,dt,bossattacks,csto):             
    if boss.cooldown>=1.85:
        boss.cooldown=1.8
    if boss.skillprepare<360:
        bullets.append(Bullet(boss.x+boss.w/2,boss.y+boss.h/2-18,boss.x+2000*math.cos(math.radians(boss.skillprepare)),boss.y+2000*math.sin(math.radians(boss.skillprepare)),boss.dmg))
        boss.skillprepare+=int(360/(24+6*csto.bosscount))
    else:    
        boss.skillchoose=0
        boss.cooldown=0           
def bulleteffect(bullets,dt,player,obstacle,csto.bosscount,csto.stage,smallbullets,boss,slashes):
    for bullet in bullets:
        bullet.move(dt)
        bullet.update()
        if bullet.rect.colliderect(player.rect):
            player.hp-=bullet.dmg
            bullets.remove(bullet)
        elif bullet.x>=(1400-20) or bullet.x<=0 or bullet.y<=0 or bullet.y>=(700-20):
            bullets.remove(bullet)
        else:
            for object in obstacle:
                if bullet.wallrect.colliderect(object.rect):
                    bullets.remove(bullet)
                    if csto.bosscount>=2 and csto.stage=='boss':
                        for i in range(0,360,int(360/(6+1*csto.bosscount))):
                            smallbullets.append(Smallbullet(bullet.x,bullet.y,boss.x+2000*math.cos(math.radians(i)),boss.y+2000*math.sin(math.radians(i)),boss.dmg/2))        
                    break
def smallbulleteffect(bullets,dt,player,obstacle,smallbullets,slashes):
    for bullet in smallbullets:
        bullet.move(dt)
        bullet.update()
        if bullet.rect.colliderect(player.rect):
            player.hp-=bullet.dmg
            smallbullets.remove(bullet)
        elif bullet.x>=(1400-20) or bullet.x<=0 or bullet.y<=0 or bullet.y>=(700-20):
            bullets.remove(bullet)
        else:
            for object in obstacle:
                if bullet.wallrect.colliderect(object.rect):
                    smallbullets.remove(bullet)
                    break        
def slashbullet(bullets,dt,player,obstacle,smallbullets,slashes):
    if slashes:
        for bullet in bullets:
            if bullet.rect.colliderect(slashes[0].rect):
                bullets.remove(bullet)                    
        for bullet in smallbullets:
            if bullet.rect.colliderect(slashes[0].rect):
                smallbullets.remove(bullet)  
def startgame(keys,changeline,csto.rendermap,csto.firstdoor,csto.wave,pluses,csto.creepspeed,csto.bosscount,player,csto.csto.mapcount,bosses,csto.stage,startwrite,writeduration):
    if keys[pygame.K_p] and changeline>6:
        csto.stage='guide'
        startwrite=0
        writeduration=0
        changeline=1
        csto.rendermap=True
    return csto.stage,startwrite,writeduration,changeline,csto.rendermap,csto.firstdoor,csto.wave,pluses,csto.creepspeed,csto.bosscount,player,csto.csto.mapcount,bosses
def replay(keys,changeline,csto.rendermap,csto.firstdoor,csto.wave,pluses,csto.creepspeed,csto.bosscount,player,csto.csto.mapcount,bosses,csto.stage,startwrite,writeduration):
    if keys[pygame.K_r] and changeline>7:
        csto.stage='normal'
        csto.rendermap=True
        csto.csto.firstdoor=[]
        csto.wave=0
        pluses=[]
        csto.creepspeed=50
        csto.bosscount=0
        player=Player()
        csto.csto.mapcount=0
        bosses=[]
        startwrite=0
        writeduration=0
        changeline=1
    return csto.stage,startwrite,writeduration,changeline,csto.rendermap,csto.firstdoor,csto.wave,pluses,csto.creepspeed,csto.bosscount,player,csto.csto.mapcount,bosses
def drawgame1(wall,obstacle,creeps,player,bosses,bossattacks,bullets,smallbullets,slashes,pluses,goable):
    screen.fill((70,70,70))
    transparentscreen.fill((0,0,0,0))
    for i in map:
        i.draw(screen)
    for i in wall:
        i.draw(screen)
    for i in obstacle:
        i.draw(screen)
    for i in creeps:
        i.draw(screen)
    write('HP',font,(0,0,0),40,699)
    write('MANA',font,(0,0,0),20,744)
    write('DAMAGE:'+str(player.dmg),font,(0,0,0),450,699)
    write('MAX MANA:'+str(player.maxmana),font,(0,0,0),450,744)
    write('MAX HP:'+str(player.maxhp),font,(0,0,0),700,699)
    write('MOVE SPEED:'+str(player.maxspeed),font,(0,0,0),700,744)
    write('MANA REGEN:'+str(player.manaregen),font,(0,0,0),950,699)
    write('ATTACK SPEED:'+str(player.attackspeed),font,(0,0,0),950,744)
    write('level',font,(0,0,0),1410,30)
    write(str(player.level),font,(0,0,0),1430,70)
    write(str(player.level+1),font,(0,0,0),1430,630)
    for i in bosses:
        i.draw(screen)
        if bossattacks:
            if i.skillprepare<1:
                for bossattack in bossattacks:
                    bossattack.warn()
            elif i.skillprepare>=1:
                for bossattack in bossattacks:
                    bossattack.update(screen)    
    player.draw(screen)
    for i in bullets:
        i.draw(screen)
    for i in smallbullets:
        i.draw(screen)
        
    for i in slashes:
        i.draw(screen)
    for i in pluses:
        i.draw(screen)
    for i in goable:
        pygame.draw.rect(screen,(225,0,0),i.rect,1)
def type():
    if writeduration<len(line1) and changeline==1:
        write(line1[:writeduration]+'_',chatfont,(111,13,181),385,235)
    elif changeline>=1:
        write(line1,chatfont,(111,13,181),385,235)
        if changeline==1:
            changeline+=1
            writeduration=0





    
                
                