
enemies = [
    {'type':'Orc','health':0 },
    {'type':'Orc', 'heath':0},
    {'type':'Orc', 'health':1},
    {'type':'Orc','health':2}
]

if any([enemies['health'] for enemy in enemies]):
    print('The battle is not over')
else:
    print('No more enemies remail!')


