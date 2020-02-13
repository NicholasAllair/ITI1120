#Nicholas Allair
#8147249
#Assignment 5 part 1

#########################
#Question 1a        function call does about 140 000 operations
#########################
def largest_34 (a):
    '''
    list of int -> int
    function takes a list of ints as input return the sum of the 3rd and 4th
    largest value in the list
    Precondition: numbers in the list are distinct and the list contains
                    at least 4 elements
    '''
    a.sort()
    length = len(a)
    return (a[length-3]) + (a[length-4])

#########################
#Question 1b        function call does about 140 000 operations
#########################
def largest_third (a):
    '''
    list of int -> int
    function takes a list of ints as input and returns the sum of the len(a)
    //3 largest numbers in the list
    Precondition: numbers in the list are distinct and the list contains
    at least 3 elements
    '''
    a.sort()
    num = len(a) // 3
    length = len(a)
    total = 0

    for i in range(num):
        i += 1
        total = total + a[len(a)-i]

    return total

#########################
#Question 1c        function call does about len(a) operations
#########################
def third_at_least (a):
    '''
    list of int -> int
    function takes a list of ints and returns a value in a which occurs len(a)//3 +1 times
    if no number exists function returns none
    Precondition: numbers in a are all distinct and there are at least 4 elements in a
    '''

    for i in range(len(a)):
        count = a.count(a[i])
        if count == (len(a)//3 + 1):
            return a[i]

    return None

#########################
#Question 1d        function call does about  operations
#########################
def sum_tri(a,x):
    '''
    list and int -> bool
    function takes in a list of ints and a int.  Returns true if any three numbers in a
    have a sum which equals x.  Else returns Flase.
    '''

    for i in range(len(a)):
        num1 = a[i]
        for o in range(len(a)):
            num2 = a[o]
            for p in range(len(a)):
                num3 = a[p]
                if num1 + num2 + num3 == x:
                    return True

    return False
        
