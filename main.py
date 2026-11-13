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
click=False
mousepos=(0,0)
msto=info.Mapstore()

#Game loop
while True:
    click=False
    dt=clock.tick(60)/1000
    mousetouch=pygame.mouse.get_pos()
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            quit(0)
        keys=pygame.key.get_pressed()
        #change in guide:
        if keys[pygame.K_t]:
            dic.guidetotest_dic.get(csto.stage,lambda *b:None)(csto)
        if keys[pygame.K_g]:
            dic.testtoguide_dic.get(csto.stage,lambda *b:None)(csto)
        if event.type==pygame.MOUSEBUTTONDOWN and event.button==1:
            click=True
            mousepos=event.pos
    
    if csto.rendermap:
        csto.player.mana=csto.player.maxmana
        msto=info.Mapstore()
        csto.player.slashcooldown=0
        csto.mapcount+=1
        dic.gachamap_dic.get(csto.stage,lambda*b:None)(msto,csto)
        csto.rendermap=False
    csto=dic.buttonchangemap_dic.get(csto.stage,lambda *b:csto)(csto,keys,msto,lstat,dt)
    if csto.stage=='guide':
        if csto.player.y<=-((107-70)-(107-70)): 
            csto.player.put(99)
            csto.player.mana=csto.player.maxmana
            
             
        #main character logic   
    dic.playerbehaviour_dic.get(csto.stage,lambda *b: None)(msto,csto,dt,keys)
    dic.playerbuff_dic.get(csto.stage,lambda *b: None)(csto,click,mousepos)
    if csto.player.hp<=0:
        csto.stage='end'                    
                        
             
        #creep logic
    if csto.stage=='normal':
        dic.creepspawn_dic.get(len(msto.creeps),lambda *b: None)(msto,csto)   
        for creep in msto.creeps:
            dic.creepmove_dic.get(math.hypot(csto.player.x-creep.x,csto.player.y-creep.y)>creep.range
            ).get(math.hypot(csto.player.x-creep.x,csto.player.y-creep.y)>creep.view or creep.notry)(creep,msto,csto,dt)
            dic.creepshoot_dic.get(math.hypot(csto.player.x-creep.x,csto.player.y-creep.y)<=(creep.range+5),lambda *b: None
            )(creep,msto,csto,dt)
        for creep in msto.slimes:
            if creep.hp>0:
                dic.slimemove_dic.get(math.hypot(csto.player.x-creep.x,csto.player.y-creep.y)>creep.view)(creep,msto,csto,dt)            
                dic.slimepath_dic.get(math.hypot(csto.player.x-creep.x,csto.player.y-creep.y)<=(creep.range+5),lambda *b: None
                )(creep,msto,csto,dt)
            else: dic.slimetrap_dic.get(csto.stage,lambda *b: None)(creep,msto,csto,dt) 
    dic.enemytakedame_dic.get(csto.stage,dic.enemytakedame_dic['none']).get(len(msto.slashes),lambda *b: None)(msto,csto)
    dic.clearslimepath_dic.get(csto.stage,lambda *b: None)(msto,dt)
    dic.changemap_dic.get(csto.stage,lambda *b: None)(msto,csto)
    if csto.stage=='boss':
        for boss in csto.bosses:
            boss.update()
            boss.cooldown+=dt
            dic.skillboss_dic.get(boss.cooldown>=1.8).get(boss.skillchoose, lambda *b: None)(boss,msto,csto,dt)       
    dic.chooseafterboss_dic.get(click,lambda *b:None)(msto,csto,mousepos)
                                        
    if csto.stage=='normal' or csto.stage=='boss':    
        dic.bullets_dic.get('bullet')(msto,csto,dt)
        dic.bullets_dic.get('smallbullet')(msto,csto,dt)
        dic.bullets_dic.get('slashbullet')(msto,csto,dt)
                
         
    
    #draw on screen
    dic.render_dic.get(csto.stage, lambda *b:None)(msto,csto,dt,mousetouch)
    dic.typechat_dic.get(csto.stage,dic.typechat_dic['none'])(msto,csto,lstat,dt)
        

        
                  
            
                
            
    
    
    pygame.display.update()
    