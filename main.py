import pygame
import random
import math
import dictionary as dic
import information as info
pygame.init()
pygame.mixer.init()
pygame.font.init()
screen=pygame.display.set_mode((1500,800))
transparentscreen=pygame.Surface((1500,800), pygame.SRCALPHA)
pygame.display.set_caption('Lost Soul')
clock=pygame.time.Clock()


csto=info.Conststore()
lstat=info.Linestat()


#Game loop
while True:
    click=False
    dt=clock.tick(60)/1000
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            quit(0)
        keys=pygame.key.get_pressed()
        #change in guide:
        if keys[pygame.K_c]:
            dic.guideortest_dic.get(csto.stage,lambda *b:None)(csto)
        if event.type==pygame.MOUSEBUTTONDOWN and event.button==1:
            click=True
            mousepos=event.pos
    dic.buttonchangemap_dic.get(csto.stage,lambda *b:None)(csto,keys)
    if csto.rendermap:
        csto.player.mana=csto.player.maxmana
        msto=info.Mapstore()
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
    dic.enemytakedame_dic.get(csto.stage,dic.enemytakedame_dic['none']).get(len(msto.slashes),lambda *b: None)(msto,csto)
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
    dic.typechat_dic.get(csto.stage,dic.typechat_dic['none'])(msto,csto,lstat,dt)
        

        
                  
            
                
            
    
    
    pygame.display.update()
    