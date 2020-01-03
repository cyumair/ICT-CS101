import random
user = int(input('ROCK(1), PAPER(2), SESSIOR(3) '))
computer = random.randint(1,3)
if user == 1:
    print('You Are Rock and Computer is ', end = "" )
    if computer == 1:
        print('Rock')
        print("DRAW")
    elif computer == 2:
        print('Paper')
        print('You Won')
    elif computer == 3:
        print('Sessors')
        print('You Lost')
elif user == 2:
    print('You Are Paper and Computer is ', end = "" )
    if computer == 1:
        print('Rock')
        print("You Won")
    elif computer == 2:
        print('Paper')
        print('DRAW')
    elif computer == 3:
        print('Sessors')
        print('You Lost')
elif user == 3:
    print('You Are Sessors and Computer is ', end = "" )
    if computer == 1:
        print('Rock')
        print("You Lost")
    elif computer == 2:
        print('Paper')
        print('You Won')
    elif computer == 3:
        print('Sessors')
        print('DRAW')