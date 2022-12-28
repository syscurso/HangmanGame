import random

sourceDir = "C:/Users/user/Desktop/juegoAhorcado/peliculas.txt"

with open(sourceDir, 'r') as f:
    words = f.readlines()

word = random.choice(words).strip()

errors = 4
intentGuess = []
run = True

while run:

    for letter in word:
        if letter.lower() in intentGuess:
            print(letter, end = ' ')
        else:
            print('_', end = " ")

    print("\n")


    intent = input(f'Errors left {errors}. Next try: ')

    intentGuess.append(intent.lower())

    if intent.lower() not in word.lower():
        errors -= 1
        if errors == 0:
            print(f'Game Over. The word was {word}')
            break
    
    run = False
    for letter in word:
        if letter.lower() not in intentGuess:
            run = True

if run == False:

    print(f'Correct word! It was {word}')
