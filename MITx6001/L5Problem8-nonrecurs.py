def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string
    
    returns: True if char is in aStr; False otherwise
    '''
    if char == aStr:
        return True
    elif char > aStr[-1]:
        return False
    elif char < aStr[0]:
        return False
    found = False        
    low = aStr[0]
    mid = len(aStr)/2
    hi  = aStr[-1]
    while not found or mid > 1:
        if char == aStr[mid]:
            found = True
        elif char < aStr[mid]:
            hi = mid
        else:
            low = mid
        mid = len(aStr)/2
    return found