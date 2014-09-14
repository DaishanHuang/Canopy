def clip(lo, x, hi):
    '''
    Takes in three numbers and returns a value based on the value of x.
    Returns:
     - lo, when x < lo
     - hi, when x > hi
     - x, otherwise
    '''
    s = max(lo, x)
    return(min(s, hi))

def clip(lo, x, hi):
    return min(max(x, lo), hi)

def square(x):
    return x*x
    
def fourthPower(x):
    return square(x) * square(x)
    
def odd(x):
    return x % 2 != 0

def isVowel(char):
    v = str(char.lower())
    if v == 'a' or v == 'e' or v == 'i' or v == 'o' or v == 'u':
        return True
    else:
        return False
        
def isVowel(char):
    v = str(char.lower())
    if v in ('aeiou'):
        return True
    else:
        return False