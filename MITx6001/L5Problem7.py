def lenRecur(aStr):
    '''
    aStr: a string
    
    returns: int, the length of aStr
    '''
    if aStr == '':
        return 0
    if aStr[0] == aStr:
        return 1
    return 1 + lenRecur(aStr[0:-1])
