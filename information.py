def giveinfo(a):
    return str(a)
chat_dic={
    'start':{
        'line1':'Lost soul',
        'line2' : 'adventure',
        'line3' : 'combat',
        'line4' : 'level up',
        'line5' : 'survive as long as you can',
        'line6' : 'press P to start>>'
    },
    'end':{
        'line1' : 'You dead!',
        'line2' : lambda a: 'level '+giveinfo(a),
        'line3':lambda a: 'wave '+giveinfo(a),
        'line4':lambda a: 'map '+giveinfo(a),
        'line5':lambda a: 'enemy killed: '+giveinfo(a),
        'line6':lambda a: 'boss killed: '+giveinfo(a),
        'line7':'press R to replay >>'        
    },
    'guide':{
        'line1':'this is your character, you will',
        'line2':'control him by WASD'        
    }
}