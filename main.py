import pygame
import random
import math
import dictionary as dic
from function import *
pygame.init()
pygame.mixer.init()
pygame.font.init()
screen=pygame.display.set_mode((1500,800))
transparentscreen=pygame.Surface((1500,800), pygame.SRCALPHA)
pygame.display.set_caption('Lost Soul')
clock=pygame.time.Clock()

stage='start'
#normal and boss
rendermap=True
firstdoor=[]  #for save the door for next map
wave=0
pluses=[]
creepspeed=50
bosscount=0
mapcount=0
player=Player()
bosses=[]
#end and start
startwrite=0
writeduration=0
changeline=1
#guide
guidenumber=1


#Game loop
while True:
    click=False
    dt=clock.tick(60)/1000
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            quit(0)
        keys=pygame.key.get_pressed()
        if event.type==pygame.MOUSEBUTTONDOWN and event.button==1:
            click=True
            mousepos=event.pos
    stage,startwrite,writeduration,changeline,rendermap,firstdoor,wave,pluses,creepspeed,bosscount,player,mapcount,bosses=dic.buttonchangemap_dic.get(stage,
    lambda *b:(stage,startwrite,writeduration,changeline,rendermap,firstdoor,wave,pluses,creepspeed,
    bosscount,player,mapcount,bosses))(keys,changeline,rendermap,firstdoor,wave,pluses,creepspeed,bosscount,player,mapcount,
    bosses,stage,startwrite,writeduration)
    if rendermap:
        player.mana=player.maxmana
        locate=list(range(200))
        goable=[]
        map=[]
        obstacle=[]
        door=[]
        w=[]
        sr=[]
        sl=[]
        v=[]
        slr=[]
        slrt=[]
        slt=[]
        srt=[]
        st=[]
        insidef=[]
        wall=[]
        creeps=[]
        bullets=[]
        smallbullets=[]
        slashes=[]
        player.slashcooldown=0
        mapstay=0
        mapcount+=1
        bossattacks=[]
        dic.rendermap_dic.get(stage,lambda*b:None)(firstdoor,map,locate,door,player,insidef,w,goable,
        sr,sl,srt,slt,slr,slrt,st,wall,v,obstacle,bosses,wave)
        rendermap=False
    
    if stage=='guide':
        if player.y<=-((107-70)-(107-70)): 
            player.put(99)
            player.mana=player.maxmana
            

            
        
        
        
        #main character logic   
    dic.playerbehaviour_dic.get(stage,lambda *b: None)(wave,player,obstacle,keys,slashes,creeps,bosses,dt,pluses)      
    if player.buffstat>0:
        if not pluses:
            pluses.append(Plus('dmg'))
            pluses.append(Plus('maxmana'))
            pluses.append(Plus('maxhp'))
            pluses.append(Plus('movespeed'))
            pluses.append(Plus('manaregen'))
            pluses.append(Plus('attackspeed'))
        for plus in pluses:
            if click:
                if plus.rect.collidepoint(mousepos):
                    player.buffstat-=1
                    if plus.type=='dmg':
                        player.dmg+=1
                    elif plus.type=='maxmana':
                        player.maxmana+=15
                        player.mana+=15
                    elif plus.type=='maxhp':
                        player.maxhp+=35
                        player.hp+=15
                    elif plus.type=='movespeed':
                        player.maxspeed+=1                        
                    elif plus.type=='manaregen':
                        player.manaregen+=1
                    elif plus.type=='attackspeed':
                        player.attackspeed+=0.03
    else:
        pluses.clear()
    if player.hp<=0:
        stage='end'                    
                        
                    
                
        #creep logic
    if stage=='normal':
        stage,rendermap,wave,mapstay=dic.creepspawn_dic.get(len(creeps),
        lambda *b: (stage,rendermap,wave,mapstay))(insidef,creeps,stage,rendermap,wave,mapstay)   
        for creep in creeps:
            dic.creepmove_dic.get(math.hypot(player.x-creep.x,player.y-creep.y)>creep.range
            ).get(math.hypot(player.x-creep.x,player.y-creep.y)>creep.view or creep.notry)(creep,obstacle,player,bullets,dt)
    stage,rendermap=dic.enemytakedame_dic.get(stage).get(len(slashes),lambda *b: (stage,rendermap))(slashes
    ,creeps,bosses,player,wave,stage,rendermap)
    rendermap=dic.changemap_dic.get(stage,lambda *b: (rendermap))(goable,player,rendermap)
    if stage=='boss':
        for boss in bosses:
            boss.update()
            boss.cooldown+=dt
            dic.skillboss_dic.get(boss.cooldown>=1.8).get(boss.skillchoose, lambda *b: None)(boss
            ,bullets,player,dt,bossattacks,bosscount)              
                        
                    
                    
                              
    if stage=='normal' or stage=='boss':    
        dic.bullets_dic.get('bullet')(bullets,dt,player,obstacle,bosscount,stage,smallbullets,boss,slashes)
        dic.bullets_dic.get('smallbullet')(bullets,dt,player,obstacle,bosscount,stage,smallbullets,boss,slashes)
        dic.bullets_dic.get('slashbullet')(bullets,dt,player,obstacle,bosscount,stage,smallbullets,boss,slashes)
             
                
                
    
        

        
            
        
                       
                
    #draw on screen
    
    if stage=='normal' or stage=='boss':
        startwrite=0
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
            if boss.skillprepare<1:
                for bossattack in bossattacks:
                    bossattack.warn()
            elif boss.skillprepare>=1:
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
    def drawsmallfeatures():
        screen.fill((70,70,70))
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
            
        player.draw(screen)
        for i in bullets:
            i.draw(screen)
        for i in smallbullets:
            i.draw(screen)
            
        for i in slashes:
            i.draw(screen)
        for i in pluses:
            i.draw(screen)                
    if stage=='guide': startwrite+=dt
    if stage=='guide':
        line1='this is your character, you will'
        line2='control him by WASD'
    if stage=='guide':
        if guidenumber==1:
            if startwrite>=0.125:
                startwrite=0
                writeduration+=1
                screen.fill((0,0,0))
                drawsmallfeatures()
                pygame.draw.rect(screen,(0,0,0),pygame.Rect(420,280,560,140))
                transparentscreen.fill((0,0,0,170))
                if changeline==3: pygame.draw.circle(transparentscreen,(225,225,225,0),(662,655),65)
                screen.blit(transparentscreen)
                if writeduration<len(line1) and changeline==1:
                    write(line1[:writeduration]+'_',chatfont,(111,13,181),385,235)
                elif changeline>=1:
                    write(line1,chatfont,(111,13,181),385,235)
                    if changeline==1:
                        changeline+=1
                        writeduration=0
                if writeduration<len(line2) and changeline==2:
                    write(line2[:writeduration]+'_',chatfont,(111,13,181),385,275)
                elif changeline>=2:
                    write(line2,chatfont,(111,13,181),385,275)
                    if changeline==2:
                        changeline+=1
                        writeduration=0


    if stage=='end':
        line1='You dead!'
        line2='level '+str(player.level)
        line3='wave '+str(wave)
        line4='map '+str(mapcount)
        line5='enemy killed: '+str(player.enemykilled)
        line6='boss killed: '+str(bosscount)
        line7='press R to replay >>'
    if stage=='end' and changeline!=8: startwrite+=dt
    if stage=='end' and startwrite>=0.125:
        startwrite=0
        writeduration+=1
        screen.fill((0,0,0))
        if writeduration<len(line1) and changeline==1:
            write(line1[:writeduration]+'_',titlefont,(111,13,181),30,5)
        elif changeline>=1:
            write(line1,titlefont,(111,13,181),30,5)
            if changeline==1:
                changeline+=1
                writeduration=0
        if writeduration<len(line2) and changeline==2:
            write(line2[:writeduration]+'_',codefont,(111,13,181),50,150)
        elif changeline>=2:
            write(line2,codefont,(111,13,181),50,150)
            if changeline==2:
                changeline+=1
                writeduration=0
        if writeduration<len(line3) and changeline==3:
            write(line3[:writeduration]+'_',codefont,(111,13,181),50,250)
        elif changeline>=3:
            write(line3,codefont,(111,13,181),50,250)
            if changeline==3:
                changeline+=1
                writeduration=0
        if writeduration<len(line4) and changeline==4:
            write(line4[:writeduration]+'_',codefont,(111,13,181),50,350)
        elif changeline>=4:
            write(line4,codefont,(111,13,181),50,350)
            if changeline==4:
                changeline+=1
                writeduration=0            
        if writeduration<len(line5) and changeline==5:
            write(line5[:writeduration]+'_',codefont,(111,13,181),50,450)
        elif changeline>=5:
            write(line5,codefont,(111,13,181),50,450)
            if changeline==5:
                changeline+=1
                writeduration=0
        if writeduration<len(line6) and changeline==6:
            write(line6[:writeduration]+'_',codefont,(111,13,181),50,550)
        elif changeline>=6:
            write(line6,codefont,(111,13,181),50,550)
            if changeline==6:
                changeline+=1
                writeduration=0
        if writeduration<len(line7) and changeline==7:
            write(line7[:writeduration]+'_',codefont,(111,13,181),50,650)
        elif changeline>=7:
            write(line7,codefont,(111,13,181),50,650)
            if changeline==7:
                changeline+=1
                writeduration=0
    if stage=='start':
        line1='Lost soul'
        line2='adventure'
        line3='combat'
        line4='level up'
        line5='survive as long as you can'
        line6='press P to start>>'
    if stage=='start' and changeline!=7: startwrite+=dt
    if stage=='start' and startwrite>=0.125:
        startwrite=0
        writeduration+=1
        screen.fill((0,0,0))
        if writeduration<len(line1) and changeline==1:
            write(line1[:writeduration]+'_',titlefont,(111,13,181),30,5)
        elif changeline>=1:
            write(line1,titlefont,(111,13,181),30,5)
            if changeline==1:
                changeline+=1
                writeduration=0
        if writeduration<len(line2) and changeline==2:
            write(line2[:writeduration]+'_',codefont,(111,13,181),50,150)
        elif changeline>=2:
            write(line2,codefont,(111,13,181),50,150)
            if changeline==2:
                changeline+=1
                writeduration=0
        if writeduration<len(line3) and changeline==3:
            write(line3[:writeduration]+'_',codefont,(111,13,181),50,250)
        elif changeline>=3:
            write(line3,codefont,(111,13,181),50,250)
            if changeline==3:
                changeline+=1
                writeduration=0
        if writeduration<len(line4) and changeline==4:
            write(line4[:writeduration]+'_',codefont,(111,13,181),50,350)
        elif changeline>=4:
            write(line4,codefont,(111,13,181),50,350)
            if changeline==4:
                changeline+=1
                writeduration=0            
        if writeduration<len(line5) and changeline==5:
            write(line5[:writeduration]+'_',codefont,(111,13,181),50,450)
        elif changeline>=5:
            write(line5,codefont,(111,13,181),50,450)
            if changeline==5:
                changeline+=1
                writeduration=0
        if writeduration<len(line6) and changeline==6:
            write(line6[:writeduration]+'_',codefont,(111,13,181),50,550)
        elif changeline>=6:
            write(line6,codefont,(111,13,181),50,550)
            if changeline==6:
                changeline+=1
                writeduration=0
        

        
                  
            
                
            
    
    
    pygame.display.update()
    