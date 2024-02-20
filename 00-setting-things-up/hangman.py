#!/usr/local/bin/python3

import random

def lees_woordenlijst(input):

    with open(input) as word_list:

        result =  [word.strip() for word in word_list.readlines()]
    return result
    
def check_list(woord, lijst):

    complete = True
    print_solution=''

    for w in range(0, len(woord)):
        if woord[w].upper() in lijst:
            print_solution += woord[w]
        else:
            complete = False
            print_solution += '_'
    print(f'Resultaat = {print_solution}')
    return complete

def main():
    levens = 7
    input_list = []
    woordenlijst = lees_woordenlijst("00-setting-things-up/hangman.txt")

    random_woord = random.choice(woordenlijst)
    win = False
    game_over = False
    while not  win and not game_over:
        choice = input("Kies een letter: ")
        if (choice.upper() not in "ABCDEFGHIJKLMNOPQRSTUVWXYZ"):
            print("Give a valid letter")
        else:
            #check letter
            if(choice.upper() in random_woord.upper()):
                input_list.append(choice.upper())
                win = check_list(random_woord, input_list) 
            else:
                print(f"De letter {choice} zit niet in het woord. Aantal levens {levens}")
                levens -= 1
        if levens == 0:
            print("Dood!")
            game_over = True
    if win:
        print('Proficiat!')
    



main()