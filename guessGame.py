print('Please think of a number between  0 and 100 !\n ')
low = 0 
high = 100 
medium = (low + high) // 2
state = True

while state:
    print(f'Is your secret number '+ str(medium) )
    guess = input("Enter 'h' to indicate the guess is too high.\nEnter 'l' to indicate the guess is too low.\nEnter 'c' to indicate I guessed correctly.\n")
    
    if (guess == 'c'):
        print('Game over. your secret number was: ' + str(medium))
        state = False
        break
    elif (guess == 'h'):
        high = medium
        medium = (low + high) // 2
    elif (guess == 'l'):
        low = medium
        medium = (low + high) // 2
    else:
        print('sorry,I did nt understand your input.')
