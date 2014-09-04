print('Please think of a number between 0 and 100! ')
low = 0
high = 100
guess = 50
hl = ''
while hl != 'c':
    print('Is your secret number ' + str(guess) + '?')
    print ('Enter \'h\' to indicate the guess is too high.'),
    print('Enter \'l\' to indicate the guess is too low.'),
    print('Enter \'c\' to indicate I guessed correctly. '),
    hl = str(raw_input())
    if hl == 'l':
        low = guess
        guess = (high + low)/2
    elif hl == 'h':
        high = guess 
        guess = (high + low)/2
    elif hl == 'c':
        break
    else:
        print('Sorry, I did not understand your input.')
print('Game over. Your secret number was: ' + str(guess))

