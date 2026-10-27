import random
rendermap=True
firstdoor=[]
if rendermap:
    locate=list(range(200))
    door=[]
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
        firstdoor.append(doorside)
        firstdoor.append(doorlong)
        if doorside==(-1):
            firstexactdoor=random.choice(list(range(19,189+1-doorlong*10,10)))
            firstdoor.append(firstexactdoor)                
            for i in range(0,doorlong):   
                f.append(firstexactdoor+i*10)
                locate.remove(firstexactdoor+i*10)
                door.append(firstexactdoor+i*10)
        elif doorside==(1):
            firstexactdoor=random.choice(list(range(10,180+1-doorlong*10,10)))
            firstdoor.append(firstexactdoor)
            for i in range(0,doorlong):
                f.append(firstexactdoor+i*10)
                locate.remove(firstexactdoor+i*10)
                door.append(firstexactdoor+i*10)    
        elif doorside==(2):
            firstexactdoor=random.choice(list(range(1,8+1-doorlong)))
            firstdoor.append(firstexactdoor)
            for i in range(0,doorlong):
                f.append(firstexactdoor+i)
                locate.remove(firstexactdoor+i)
                door.append(firstexactdoor+i)                
        elif doorside==(-2):
            firstexactdoor=random.choice(list(range(191,198+1-doorlong)))
            firstdoor.append(firstexactdoor)
            for i in range(0,doorlong):
                f.append(firstexactdoor+i)
                locate.remove(firstexactdoor+i)
                door.append(firstexactdoor+i)
    else:
        doorlong=firstdoor[1]
        doorside=firstdoor[0]*(-1)
        if doorside==(-1):
            firstexactdoor=firstdoor[2]+9       
            for i in range(0,doorlong):   
                f.append(firstexactdoor+i*10)
                locate.remove(firstexactdoor+i*10)
                door.append(firstexactdoor+i*10)
        elif doorside==(1):
            firstexactdoor=firstdoor[2]-9
            for i in range(0,doorlong):
                f.append(firstexactdoor+i*10)
                locate.remove(firstexactdoor+i*10)
                door.append(firstexactdoor+i*10)    
        elif doorside==(2):
            firstexactdoor=firstdoor[2]-90
            for i in range(0,doorlong):
                f.append(firstexactdoor+i)
                locate.remove(firstexactdoor+i)
                door.append(firstexactdoor+i*10)                
        elif doorside==(-2):
            firstexactdoor=firstdoor[2]+90
            for i in range(0,doorlong):
                f.append(firstexactdoor+i)
                locate.remove(firstexactdoor+i)
                door.append(firstexactdoor+i*10)

    start=random.choice(door)
    c=0
    while start in door:
        a=[1,-1,10,-10]
        if c!=0: 
            if len(a)==0:
                break
            elif len(a)==1:
                c=0
            else:
                a.remove(c)
        b=random.choice(a)
        if (start+b) in locate and not (start+b) in [0,9,199,190]:
            start+=b
            f.append(start)
            locate.remove(start)
        else:
            c=b
    c=0
    doorside=0
    doorlong=0
    while True:
        a=[1,-1,10,-10]
        if c!=0: 
            if len(a)==0:
                break
            elif len(a)==1:
                c=0
            else:
                a.remove(c)
        b=random.choice(a)
        if (start+b) in locate and not (start+b) in [0,9,199,190] and not (start+b) in door:
            d=list(range(1,9))+list(range(10,190,10))+list(range(19,199,10))+list(range(191,199))
            if (start+b) in d:
                if (start+b) in list(range(1,9)):
                    if doorside==0: 
                        doorside=2
                    elif doorside!=2:
                        break
                    else:
                        doorlong+=1
                    if doorlong==6:
                        break
                elif (start+b) in list(range(10,190)):
                    if doorside==0: 
                        doorside=1
                    elif doorside!=1:
                        break
                    else:
                        doorlong+=1
                    if doorlong==6:
                        break
                elif (start+b) in list(range(19,199)):
                    if doorside==0: 
                        doorside=-1
                    elif doorside!=(-1):
                        break
                    else:
                        doorlong+=1
                    if doorlong==6:
                        break
                elif (start+b) in list(range(191,199)):
                    if doorside==0: 
                        doorside=-2
                    elif doorside!=(-1):
                        break
                    else:
                        doorlong+=1
                    if doorlong==6:
                        break
            start+=b
            f.append(start)
            locate.remove(start)  
        else:
            c=b
    rendermap=False
    print(firstdoor,doorlong,door,doorside,f)