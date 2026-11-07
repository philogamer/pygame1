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
creeptakedame_dic={
    True: lambda *a: fun.creepgetdame(*a)
}



