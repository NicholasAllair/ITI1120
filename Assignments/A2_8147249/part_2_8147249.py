#Family Name: Nicholas Allair
#Student number: 8147249
#Course: ITI1121
#Assignment Number 2

import math
import turtle

####################
#Question 1
####################
def min_enclosing_rectangle(radius, x, y):
    rx = x-radius
    ry = y -radius
    return (rx, ry)

####################
#Question 2
####################
def series_sum ():
    n = int(input("Please enter a non- negative integer: "))
    if n>=0:
        loop = 1
        total = 1000

        while loop <=n:
            add = 1/(loop**2)
            loop += 1
            total = total + add
            
        return(total)

    else:
        print("")
    
####################
#Question 3
####################
def pell(n):
	if n < 0:
		return None
	if n<=2:
		return n
	return 2 * pell(n - 1) + pell(n - 2)

####################
#Question 4
####################
def countMembers(s):
    x = 0
    x = s.count('e')
    x = x+ s.count ('f')
    x = x+ s.count ('g')
    x = x+ s.count ('h')
    x = x+ s.count ('i')
    x = x+ s.count ('j')
    x = x+ s.count ('F')
    x = x+ s.count ('G')
    x = x+ s.count ('H')
    x = x+ s.count ('I')
    x = x+ s.count ('J')
    x = x+ s.count ('K')
    x = x+ s.count ('L')
    x = x+ s.count ('M')
    x = x+ s.count ('N')
    x = x+ s.count ('O')
    x = x+ s.count ('P')
    x = x+ s.count ('Q')
    x = x+ s.count ('R')
    x = x+ s.count ('S')
    x = x+ s.count ('T')
    x = x+ s.count ('U')
    x = x+ s.count ('V')
    x = x+ s.count ('W')
    x = x+ s.count ('X')
    x = x+ s.count ('2')
    x = x+ s.count ('3')
    x = x+ s.count ('4')
    x = x+ s.count ('5')
    x = x+ s.count ('6')
    x = x+ s.count ('!')
    x = x+ s.count (',')
    x = x+ s.count ('\\')

    return x

####################
#Question 5
####################

def casual_number(s):
	s = s.split(",")
	count = 0
	s = "".join([i for i in s ])
	try:
		return int(s)
	except ValueError:
		return None

####################
#Question 10
####################
def nonrepetitive(s):
	if s == "":
		return True
	for i in range(len(s)):
		if s[i+1:] == s[:i]:
			return True
	return False


  
    
    


        
            
            
            


