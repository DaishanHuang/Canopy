def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string
    
    returns: True if char is in aStr; False otherwise
    '''
    if aStr == '':
        return False
    if char == aStr:
        return True
    if char > aStr[-1]:
        return False
    if char < aStr[0]:
        return False
        
    mid = len(aStr)/2
    if char == aStr[mid]:
        return True
    if mid == 1:
        return False
#    print('mid: ' + str(aStr[mid]) )
    if char < aStr[mid]:
#        print('isIn(' + str(char) + ', ' + str(aStr[0:mid]) + ')' )
        return isIn(str(char), str(aStr[0:mid]))
    else:
#        print('isIn(' + str(char) + ', ' + str(aStr[mid:]) + ')' )
        return isIn(char, aStr[mid:])
