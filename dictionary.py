import function as fun
rendermap_dic={
    'normal': lambda *a: fun.render1(*a),
    'boss': lambda *a: fun.render2(*a),
    'guide': lambda *a: fun.render3(*a),
}
playerbehaviour_dic={
    'normal': lambda *a: fun.playerbehave(*a),
    'boss': lambda *a: fun.playerbehave(*a),
}
creepmove_dic={
    True:{
        True: lambda *a: fun.creeprandom(*a,0),
        False: lambda *a: fun.creepmove(*a,1)
    },
    False:{
        True: lambda *a: fun.creepmoveandshoot(*a,-1),
        False: lambda *a: fun.creepmoveandshoot(*a,-1) 
    }
}
enemytakedame_dic={
    'normal': {
        1:lambda *a: fun.creepgetdame(*a)
        },
    'boss':{
        1:lambda *a: fun.bossgetdame(*a)
    },
    'guide':{
        10:lambda: fun.donothing()
    },
    'start':{
        10:lambda: fun.donothing()
    },
    'end':{
        10:lambda: fun.donothing()
    },
}
creepspawn_dic={
    0: lambda *a: fun.creepspawn(*a)
}
changemap_dic={
    'normal': lambda *a: fun.changemap(*a) 
}
skillboss_dic={
    True:{
        0: lambda *a: fun.chooseskillboss(*a),
        1: lambda *a: fun.skillboss1(*a),
        2: lambda *a: fun.skillboss2(*a),
        3: lambda *a: fun.skillboss3(*a),
        4: lambda *a: fun.skillboss4(*a)
    },
    False:{
        1000: fun.donothing()
    }
}
bullets_dic={
    'bullet': lambda *a: fun.bulleteffect(*a),
    'smallbullet': lambda *a: fun.smallbulleteffect(*a),
    'slashbullet': lambda *a: fun.slashbullet(*a), 
}
buttonchangemap_dic={
    'start': lambda *a: fun.startgame(*a),
    'end': lambda *a: fun.replay(*a)
}
render_dic={
    'normal': lambda *a: fun.drawgame1(*a),
    'boss': lambda *a: fun.drawgame1(*a),
}

