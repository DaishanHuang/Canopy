# lecture 3.4, slide 3

num = int(raw_input('Enter an integer: '))

if num < 0:
    isNeg = True
    num = abs(num)
else:
    isNeg = False
result = ''
if num == 0:
    result = '0'
while num > 0:
    # add remainder
    result = str(num%2) + result
    # shift bits left
    num = num/2
if isNeg:
    result = '-' + result
print(result)