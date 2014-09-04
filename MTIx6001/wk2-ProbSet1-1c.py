# Count the occurences of vowels w/raw_input
string = str(raw_input('Enter a string to count vowels: '))
vowels = 'aeiou'
count = 0
i = 0
while i < len(string):
    if string[i].lower() in vowels:
        count += 1
        print('vowel: ' + string[i])
    i += 1
print('String ' + string + ' contains ' + str(count) + ' vowels.')