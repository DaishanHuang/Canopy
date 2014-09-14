def gcdIter(a, b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    if a == 1 or b == 1:
        return 1
    if a < b:
        int = a
    else:
        int =b
    while int > 1:
        if b%int == 0 and a%int == 0:
            return int
        else:
            int -= 1
    return 1