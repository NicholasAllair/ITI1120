#Family Name: Nicholas Allair
#Student number: 8147249
#Course: ITI1121
#Assignment Number 1

import math
import turtle


####################
#Question 1
####################
def mh2kh(s):
    
    return(s*1.609344)


####################
#Question 2
####################
def pythagorean_pair(a,b):
     c=(a**2 + b**2)**(1/2)
     if c%1==0:
             c='True'
     else:
             c='False'
     return(c)

####################
#Question 3
####################
def in_out(xs,ys,side):
    side=abs(side)
    x=input("Enter a number for the x coordinate of a query point:   ")
    y=input("Enter a number for the y coordinate of a query point:   ")

    x=float(x)
    y=float(y)

    yb=ys + side
    
    if xs<=x<=(xs + side):       
        if ys<=y<=(ys + side):
            print("True")
    else:
        print("False")
    
        
    return()



####################
#Question 4
####################
def safe(n):
    if -1>n>100:
        return("number must be positive and at most two digits")

    if n%9==0:
        return(False)

    if n >= 89:
        return(False)

    if n +1 == 10:
        return(False)

    if n +1 == 20:
        return(False)

    if n +1 == 30:
        return(False)

    if n +1 == 40:
        return(False)

    if n +1 == 50:
        return(False)

    if n +1 == 60:
        return(False)

    if n +1 == 70:
        return(False)

    if n +1 == 80:
        return(False)

    else:
        return (True)



####################
#Question 5
####################
def quote_maker(quote, name, year):

    print ("In %d, a person called"  %year)
    print("" +name+ "")
    print("said: '" +quote+ "'")
    return

####################
#Question 6
####################
QUOTE=input("Input the quote")
NAME=input("Input the name")
YEAR=input("Input the year")
QUOTE=str(QUOTE)
NAME=str(NAME)
YEAR=str(YEAR)


def quote_maker(quote, name, year):

    print ("In %s, a person called"  %year)
    print("" +name+ "")
    print("said: '" +quote+ "'")
    return


quote_maker(QUOTE, NAME, YEAR)

####################
#Question 7
####################
def rps_winner():

    player1='choice'
    player2='choice'
    
    print("What choice did player 1 make?")
    player1=input("Type one of the following options: rock paper, scissors:  ")
    print("What choice did player 2 make?")
    player2=input("Type one of the following options: rock paper, scissors:  ")

    

    if player1 == player2:
        print("Player 1 Wins. That is not true")
        print("It is a tie.  That is true")

    if player1 == 'rock':
        if player2 == 'scissors':
            print("Player 1 Wins. That is True")
            print("It is a tie.  That is not true")

    if player1 == 'scissors':
        if plaeyer2 == 'paper':
            print("Player 1 Wins. That is True")
            print("It is a tie.  That is not true")

    if player1 == 'paper':
        if plaeyer2 == 'rock':
            print("Player 1 Wins. That is True")
            print("It is a tie.  That is not true")

    else:
            print("Player 1 Wins. That is not True")
            print("It is a tie.  That is not true")
            

####################
#Question 8
####################

def fun(x):
   
    Y= (math.log10(x+3))/4
    return (Y)

####################
#Question 9
####################

def ascii_name_plaque(name):

    print('*'*(10+len(name)))
    print("*", end="")
    print(' '*(8+len(name)), end="")
    print("*")
    print("*  __" +name+ "__  *")
    print("*", end="")
    print(' '*(8+len(name)), end="")
    print("*")
    print('*'*(10+len(name)))

####################
#Question 10       The link in the question licked me to a drawing of a car, so i drew it
####################
s=turtle.Screen()
t=turtle.Turtle()
def my_fun_drawing():
    s=turtle.Screen()
    t=turtle.Turtle()
    
    #Wheels
    t.penup()
    t.goto(-200,-20)
    t.pendown()
    t.circle(35)
    t.penup()

    
    t.goto(0,-20)
    t.pendown()
    t.circle(35)
    t.penup()

    t.goto(0,5)
    t.pendown()
    t.circle(10)
    t.penup()

    
    t.goto(-200,5)
    t.pendown()
    t.circle(10)
    t.penup()

    #Chassis
    t.goto(-168,5)
    t.pendown()
    t.goto(-32,5)
    t.penup()

    t.goto(32,5)
    t.pendown()
    t.goto(60,5)
    t.left(70)
    t.forward(35)
    t.left(110)
    t.forward(45)
    t.back(15)
    t.right(90)
    t.forward(50)
    t.left(80)
    t.forward(70)
    t.right(50)
    t.forward(60)
    t.left(65)
    t.forward(100)
    t.left(85)
    t.forward(35)
    t.left(90)
    t.forward(125)
    t.back(125)
    t.right(180)
    t.forward(175)
    t.left(90)
    t.forward(80)
    t.left(90)
    t.forward(101)

    t.penup()
    t.goto(-140,5)
    t.left(90)
    pendown()
    t.forward(140)

####################
#Question 11
####################
def alogical(n):

    count=0
    while n>1:
        n=n/2
        count += 1
    print (count)
    
####################
#Question 12
####################
def time_formater(h,m):

    
    if m>33:
        h+=1
    if h ==24:
        h=0
    #this line rounds to the nearest 5
    m=int(5 * round(float(m)/5))

    if m==60:
        m=0

    

    if m==0:
        print(h, " o'clock")

    if m==30:
        print("half past %d o'clock"  % h)

    if 5<=m<=25:
        print(m, "minutes past ", h, " o'clock")

    if 35<=m<=55:
        print(60-m, "minutes to ", h, " o'clock")


####################
#Question 13
####################
def cad_cashier(price,payment):

    price = round(0.05*round(price/0.05), 2)

    change= payment-price

    return(change)

####################
#Question 14
####################

















          


    




















            
