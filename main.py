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
        dic.creepspawn_dic.get(len(msto.creeps),lambda *b: None)(msto,csto)   
        for creep in msto.creeps:
            dic.creepmove_dic.get(math.hypot(csto.player.x-creep.x,csto.player.y-creep.y)>creep.range
            ).get(math.hypot(csto.player.x-creep.x,csto.player.y-creep.y)>creep.view or creep.notry)(creep,msto,csto,dt)
    dic.enemytakedame_dic.get(csto.stage).get(len(msto.slashes),lambda *b: None)(msto,csto)
    dic.changemap_dic.get(csto.stage,lambda *b: None)(msto,csto)
    if csto.stage=='boss':
        for boss in csto.bosses:
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
    if csto.stage=='guide': csto.startwrite+=dt
    if csto.stage=='guide':
        line1='this is your character, you will'
        line2='control him by WASD'
    if csto.stage=='guide':
        if csto.guidenumber==1:
            if csto.startwrite>=0.125:
                csto.startwrite=0
                csto.writeduration+=1
                screen.fill((0,0,0))
                pygame.draw.rect(screen,(0,0,0),pygame.Rect(420,280,560,140))
                transparentscreen.fill((0,0,0,170))
                if csto.changeline==3: pygame.draw.circle(transparentscreen,(225,225,225,0),(662,655),65)
                screen.blit(transparentscreen)
                if csto.writeduration<len(line1) and csto.changeline==1:
                    write(line1[:csto.writeduration]+'_',csto.chatfont,(111,13,181),385,235)
                elif csto.changeline>=1:
                    write(line1,csto.chatfont,(111,13,181),385,235)
                    if csto.changeline==1:
                        csto.changeline+=1
                        csto.writeduration=0
                if csto.writeduration<len(line2) and csto.changeline==2:
                    write(line2[:csto.writeduration]+'_',csto.chatfont,(111,13,181),385,275)
                elif csto.changeline>=2:
                    write(line2,csto.chatfont,(111,13,181),385,275)
                    if csto.changeline==2:
                        csto.changeline+=1
                        csto.writeduration=0


    if csto.stage=='end':
        line1='You dead!'
        line2='level '+str(csto.player.level)
        line3='csto.wave '+str(csto.wave)
        line4='map '+str(csto.mapcount)
        line5='enemy killed: '+str(csto.enemykilled)
        line6='boss killed: '+str(csto.bosscount)
        line7='press R to replay >>'
    if csto.stage=='end' and csto.changeline!=8: csto.startwrite+=dt
    if csto.stage=='end' and csto.startwrite>=0.125:
        csto.startwrite=0
        csto.writeduration+=1
        screen.fill((0,0,0))
        if csto.writeduration<len(line1) and csto.changeline==1:
            write(line1[:csto.writeduration]+'_',csto.titlefont,(111,13,181),30,5)
        elif csto.changeline>=1:
            write(line1,csto.titlefont,(111,13,181),30,5)
            if csto.changeline==1:
                csto.changeline+=1
                csto.writeduration=0
        if csto.writeduration<len(line2) and csto.changeline==2:
            write(line2[:csto.writeduration]+'_',csto.codefont,(111,13,181),50,150)
        elif csto.changeline>=2:
            write(line2,csto.codefont,(111,13,181),50,150)
            if csto.changeline==2:
                csto.changeline+=1
                csto.writeduration=0
        if csto.writeduration<len(line3) and csto.changeline==3:
            write(line3[:csto.writeduration]+'_',csto.codefont,(111,13,181),50,250)
        elif csto.changeline>=3:
            write(line3,csto.codefont,(111,13,181),50,250)
            if csto.changeline==3:
                csto.changeline+=1
                csto.writeduration=0
        if csto.writeduration<len(line4) and csto.changeline==4:
            write(line4[:csto.writeduration]+'_',csto.codefont,(111,13,181),50,350)
        elif csto.changeline>=4:
            write(line4,csto.codefont,(111,13,181),50,350)
            if csto.changeline==4:
                csto.changeline+=1
                csto.writeduration=0            
        if csto.writeduration<len(line5) and csto.changeline==5:
            write(line5[:csto.writeduration]+'_',csto.codefont,(111,13,181),50,450)
        elif csto.changeline>=5:
            write(line5,csto.codefont,(111,13,181),50,450)
            if csto.changeline==5:
                csto.changeline+=1
                csto.writeduration=0
        if csto.writeduration<len(line6) and csto.changeline==6:
            write(line6[:csto.writeduration]+'_',csto.codefont,(111,13,181),50,550)
        elif csto.changeline>=6:
            write(line6,csto.codefont,(111,13,181),50,550)
            if csto.changeline==6:
                csto.changeline+=1
                csto.writeduration=0
        if csto.writeduration<len(line7) and csto.changeline==7:
            write(line7[:csto.writeduration]+'_',csto.codefont,(111,13,181),50,650)
        elif csto.changeline>=7:
            write(line7,csto.codefont,(111,13,181),50,650)
            if csto.changeline==7:
                csto.changeline+=1
                csto.writeduration=0
    if csto.stage=='start':
        line1='Lost soul'
        line2='adventure'
        line3='combat'
        line4='level up'
        line5='survive as long as you can'
        line6='press P to start>>'
    if csto.stage=='start' and csto.changeline!=7: csto.startwrite+=dt
    if csto.stage=='start' and csto.startwrite>=0.125:
        csto.startwrite=0
        csto.writeduration+=1
        screen.fill((0,0,0))
        if csto.writeduration<len(line1) and csto.changeline==1:
            write(line1[:csto.writeduration]+'_',csto.titlefont,(111,13,181),30,5)
        elif csto.changeline>=1:
            write(line1,csto.titlefont,(111,13,181),30,5)
            if csto.changeline==1:
                csto.changeline+=1
                csto.writeduration=0
        if csto.writeduration<len(line2) and csto.changeline==2:
            write(line2[:csto.writeduration]+'_',csto.codefont,(111,13,181),50,150)
        elif csto.changeline>=2:
            write(line2,csto.codefont,(111,13,181),50,150)
            if csto.changeline==2:
                csto.changeline+=1
                csto.writeduration=0
        if csto.writeduration<len(line3) and csto.changeline==3:
            write(line3[:csto.writeduration]+'_',csto.codefont,(111,13,181),50,250)
        elif csto.changeline>=3:
            write(line3,csto.codefont,(111,13,181),50,250)
            if csto.changeline==3:
                csto.changeline+=1
                csto.writeduration=0
        if csto.writeduration<len(line4) and csto.changeline==4:
            write(line4[:csto.writeduration]+'_',csto.codefont,(111,13,181),50,350)
        elif csto.changeline>=4:
            write(line4,csto.codefont,(111,13,181),50,350)
            if csto.changeline==4:
                csto.changeline+=1
                csto.writeduration=0            
        if csto.writeduration<len(line5) and csto.changeline==5:
            write(line5[:csto.writeduration]+'_',csto.codefont,(111,13,181),50,450)
        elif csto.changeline>=5:
            write(line5,csto.codefont,(111,13,181),50,450)
            if csto.changeline==5:
                csto.changeline+=1
                csto.writeduration=0
        if csto.writeduration<len(line6) and csto.changeline==6:
            write(line6[:csto.writeduration]+'_',csto.codefont,(111,13,181),50,550)
        elif csto.changeline>=6:
            write(line6,csto.codefont,(111,13,181),50,550)
            if csto.changeline==6:
                csto.changeline+=1
                csto.writeduration=0
        

        
                  
            
                
            
    
    
    pygame.display.update()
    