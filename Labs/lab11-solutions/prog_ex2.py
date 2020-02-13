# a recursive function that computes and returns the number of digits in given input non-negative integer.

def count_digits(n):
     '''(int)->int
     Returns the number of digits in n
     Precondition: n a non-negative integer
     '''
     count=0
     rest_of_digits = n // 10
     if rest_of_digits == 0:
          count= 1
     else:
          count = 1 + count_digits(rest_of_digits)
        
     return count


# this is the same ... just has few less lines of code

def count_digits_v2(n):
     '''(int)->int
     Returns the number of digits in n
     Precondition: n a non-negative integer
     '''
     rest_of_digits = n // 10
     if rest_of_digits == 0:
          return 1
     else:
          return 1 + count_digits(rest_of_digits)
