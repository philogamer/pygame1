import function as fun
gachamap_dic={
    'normal': lambda *a: fun.render1(*a),
    'boss': lambda *a: fun.render2(*a),
    'guide': lambda *a: fun.render3(*a),
}
playerbehaviour_dic={
    'normal': lambda *a: fun.playerbehave(*a),
    'boss': lambda *a: fun.playerbehave(*a),
    'test': lambda *a: fun.playerbehave(*a),
}
creepmove_dic={
    True:{
        True: lambda *a: fun.creeprandom(*a,0),
        False: lambda *a: fun.creepmove(*a,1)
    },
    False:{
        True: lambda *a: fun.creepmove(*a,-1),
        False: lambda *a: fun.creepmove(*a,-1)
    }
}
creepshoot_dic={
    True:lambda*a:fun.creepshoot(*a)
}
enemytakedame_dic={
    'normal': {
        1:lambda *a: fun.creepgetdame(*a)
        },
    'boss':{
        1:lambda *a: fun.bossgetdame(*a)
    },
    'none':{
        10:lambda: fun.donothing()
    }
}
creepspawn_dic={
    0: lambda *a: fun.creepspawn(*a)
}
changemap_dic={
    'normal': lambda *a: fun.changemap(*a),
    'test': lambda *a: fun.changetestmap(*a) 
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
    'end': lambda *a: fun.replay(*a),
    'guide': lambda *a: fun.skip(*a),
    'test': lambda *a: fun.skip(*a),
}
render_dic={
    'normal': lambda *a: fun.drawgame1(*a),
    'boss': lambda *a: fun.drawgame1(*a),
    'test': lambda *a: fun.drawgame1(*a)
    
}
playerbuff_dic={
    'normal': lambda *a: fun.buff(*a),
    'boss': lambda *a: fun.buff(*a),
    'guide': lambda *a: fun.buff(*a),
    'test': lambda *a: fun.buff(*a),
}
typechat_dic={
    'start': lambda *a: fun.typingstart(*a,6),
    'end': lambda *a: fun.typingstart(*a,7),
    'guide': lambda *a: fun.guidetyping(*a,2),
    'test': lambda *a: (fun.returntype(*a), fun.stayline(*a)),
    'none': lambda *a: fun.returntype(*a)
}
guidetotest_dic={
    'guide':lambda a: fun.guidetotest(a)
}
testtoguide_dic={
    'test':lambda a: fun.testtoguide(a)
}
clearslimepath_dic={
    'normal': lambda *a:fun.slimepathclear(*a)
}
slimemove_dic={
    True: lambda *a: fun.creeprandom(*a,0),
    False: lambda *a: fun.slimemove(*a,1)
}
slimepath_dic={
    True: lambda *a:fun.slimepath(*a)
}
chooseafterboss_dic={
    True: lambda *a: fun.healthregen(*a)
}
slimetrap_dic={
    'normal': lambda *a: fun.slimedeath(*a)
}






