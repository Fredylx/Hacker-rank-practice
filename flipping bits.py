def flippingBits(n):
    # Write your code here
    '''
    simple subtraction if you think about it: Value of 32bit in full: 2^32 - 1 (cuz first bit is 0 not 1) To flip a bit number n: 2^32 - 1 - n
    '''
    return (2**32 - 1 - n)   
