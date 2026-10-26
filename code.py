import pygame
import random
import math

pygame.init()
pygame.mixer.init()
screen=pygame.display.set_mode((1500,750))
pygame.display.set_caption('Lost Soul')
stage='map'
clock=pygame.time.clock()


class map:
    def _init_(self,xy,type):
        self.y=xy%10
        self.x=xy-self.y
        if type=='W':
            self.img='assets/wall.png'
        elif type=='V':
            self.img='assets/V.png'
        elif type=='CL':
            self.img='assets/CL.png'
        elif type=='CR':
            self.img='assets/CR.png'
        elif type=='CRL':
            self.img='assets/CRL.png'
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
        elif type=='F':
            a='assets/F'+str(random.randint(1,3))+'.png'
            self.img=a
            self.img=pygame.transform.rotate(self.img, random.choice([0,90,180,360]))
        self.img=pygame.image.load(self.img).convert_alpha()
        self.img=pygame.transform.scale(self.img,(75,75))
    def draw(self,screen):
        screen.blit(self.img,(self.x,self.y))

rendermap=True
firstdoor=[]  #for save the door for next map
#Game loop
while True:
    dt=clock.tick(60)/1000
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            quit(0)
    if rendermap:
        locate=list(range(100))
        f=[]
        w=[]
        sr=[]
        sl=[]
        v=[]
        cl=[]
        cr=[]
        crl=[]
        slr=[]
        slrt=[]
        slt=[]
        st=[]
        if not firstdoor:
            doorlong=random.randint(1,5)
            doorside=random.choice([-1,1,-2,2])
            if doorside==(-1):
                firstexactdoor=random.choice(list(range(9,100,10)))
                if firstexactdoor+doorlong*10 >=99:
                    for i in range(doorlong):
                        f.append(firstexactdoor-i)
        while True:
            
    
    
    pygame.display.flip()
    