## Without functional abstraction

x = int(raw_input('Enter a number: '))
p = int(raw_input('Enter an integer power: '))

result = 1

for turn in range(p):
    print('iteration: ' + str(turn) + ' current result: ' + str(result))
    result = result * x
print('iteration: ' + str(turn + 1) + ' current result: ' + str(result))

## With functional abstraction
def iterativePower(x,p):
    result = 1
    for turn in range(p):
        print ('iteration: ' + str(turn) + ' current result: ' + str(result))
        result = result * x
    return result

