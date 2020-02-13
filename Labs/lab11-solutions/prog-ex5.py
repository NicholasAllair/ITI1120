def gcd(a, b):
    '''(int,int)->int
    Returns the greatest common divisor of a and b
    Precondition: a and b are both positive integers
    '''  
    if a % b == 0:
         return b
    else:
      return gcd(b, a % b)
