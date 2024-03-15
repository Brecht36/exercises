import re

users = dict()      #key: username, value: paswoord

def validate_password(paswoord):    #paswoord is een string
    valide = [ # re.match("(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9][a-zA-Z0-9]{8,})", paswoord)
        '.{8,}',
        '[a-z]+',
        '[A-Z]+',
        '[0-9]+'
    ]
    for regex in valide:
        if not re.search(regex, paswoord):
            return False
    return True

def register():
    while True:
        print(users)
        #valideert username
        username = input('Geef een username in: ')
        if username in users.keys():
            raise Exception('Deze username is al in gebruik!')
        else:
            user = username
        #valideert paswoord
        paswoord = input('Geef een paswoord in: ')
        if validate_password(paswoord):
            wachtwoord = paswoord
        else:
            raise Exception('\nWachtwoord moet voldoen aan volgende puntjes: \n\t -minstens 8 karakters lang zijn \n\t -minstens 1 nummer bevatten \n\t -minstens 1 kleine letter bevatten \n\t -minstens 1 grote letter bevatten')
        #voeg toe aan dict
        users[user] = wachtwoord
        print("You succesfully registered!")
    
register()