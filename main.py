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


csto=Conststore()


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
    dic.buttonchangemap_dic.get(csto.stage,lambda *b:None)(csto,keys)
    if csto.rendermap:
        csto.player.mana=csto.player.maxmana
        msto=Mapstore()
        csto.player.slashcooldown=0
        csto.mapcount+=1
        dic.gachamap_dic.get(csto.stage,lambda*b:None)(msto,csto)
        csto.rendermap=False
    
    if csto.stage=='guide':
        if csto.player.y<=-((107-70)-(107-70)): 
            csto.player.put(99)
            csto.player.mana=csto.player.maxmana
            

            
        
        
        
        #main character logic   
    dic.playerbehaviour_dic.get(csto.stage,lambda *b: None)(msto,csto,dt,keys)
    dic.playerbuff_dic.get(csto.stage,lambda *b: None)(csto)
    if csto.player.hp<=0:
        csto.stage='end'                    
                        
                    
                
        #creep logic
    if csto.stage=='normal':
        dic.creepspawn_dic.get(len(csto.creeps),lambda *b: None)((msto,csto))   
        for creep in csto.creeps:
            dic.creepmove_dic.get(math.hypot(csto.player.x-creep.x,csto.player.y-creep.y)>creep.range
            ).get(math.hypot(csto.player.x-creep.x,csto.player.y-creep.y)>creep.view or creep.notry)(creep,msto,csto,dt)
    dic.enemytakedame_dic.get(csto.stage).get(len(msto.slashes),lambda *b: None)(msto,csto)
    dic.changemap_dic.get(csto.stage,lambda *b: None)(msto,csto)
    if csto.stage=='boss':
        for boss in csto.csto.bosses:
            boss.update()
            boss.cooldown+=dt
            dic.skillboss_dic.get(boss.cooldown>=1.8).get(boss.skillchoose, lambda *b: None)(boss,msto,csto)       
                        
                    
                    
                              
    if csto.stage=='normal' or csto.stage=='boss':    
        dic.bullets_dic.get('bullet')(msto,csto,dt)
        dic.bullets_dic.get('smallbullet')(msto,csto,dt)
        dic.bullets_dic.get('slashbullet')(msto,csto,dt)
             
                
                
    
        

        
            
        
                       
                
    #draw on screen
    dic.render_dic.get(csto.stage, lambda *b:None)(msto,csto)
    if csto.stage=='normal' or csto.stage=='boss':
        csto.startwrite=0
    def drawsmallfeatures():
        screen.fill((70,70,70))
        for i in map:
            i.draw(screen)
        for i in wall:
            i.draw(screen)
        for i in obstacle:
            i.draw(screen)
        for i in csto.creeps:
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
            
        csto.player.draw(screen)
        for i in bullets:
            i.draw(screen)
        for i in smallbullets:
            i.draw(screen)
            
        for i in slashes:
            i.draw(screen)
        for i in pluses:
            i.draw(screen)                
    if csto.stage=='guide': startwrite+=dt
    if csto.stage=='guide':
        line1='this is your character, you will'
        line2='control him by WASD'
    if csto.stage=='guide':
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


    if csto.stage=='end':
        line1='You dead!'
        line2='level '+str(csto.player.level)
        line3='csto.wave '+str(csto.wave)
        line4='map '+str(csto.mapcount)
        line5='enemy killed: '+str(csto.enemykilled)
        line6='boss killed: '+str(csto.csto.bosscount)
        line7='press R to replay >>'
    if csto.stage=='end' and changeline!=8: startwrite+=dt
    if csto.stage=='end' and startwrite>=0.125:
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
    if csto.stage=='start':
        line1='Lost soul'
        line2='adventure'
        line3='combat'
        line4='level up'
        line5='survive as long as you can'
        line6='press P to start>>'
    if csto.stage=='start' and changeline!=7: startwrite+=dt
    if csto.stage=='start' and startwrite>=0.125:
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
    