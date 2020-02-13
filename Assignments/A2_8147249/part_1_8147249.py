import math
import random


def primary_school_quiz(flag, n):

    def performTest (mark,n):
        
        score = mark / n
        
        if score >= 0.9:
            print("Congradualtions" +name+ "!  You'll probably get an A tomorrow.  Now go eat you dinner and go to sleep.")

        elif (score >= 0.7) and (score < 0.9):
            print("You did well " +name+ " but I know you can do better")

        elif (score < 0.7):
            print("You did well " +name+ " but I know you can do better")

        
        return(score)

    question_n = 1
    mark = 0

    if flag == 0:
        while question_n <= n:
            a = (random.randint(0,9))
            b = (random.randint(0,9))

            r_answer = a-b
            
            print("Question ",question_n, ":")
            
            print("What is the result of" ,a,"-" ,b, "?  ")
            i_answer = int(input(""))

            if (r_answer == i_answer):
                mark +=1

            question_n += 1

    if flag == 1:
        while question_n <= n:
                           
            a = (random.randint(0,9))
            b = (random.randint(0,9))

            r_answer = a**b

            print("Question ",question_n, ":")

            print("What is the result of" ,a,"^" ,b, "?  ")
            i_answer = int(input(questionstring))####################################

            if (r_answer == i_answer):
                mark +=1

            question_n += 1

    performTest(mark,n)


def high_school_eqsolver(a,b,c):

    if (a != 0) and (b != 0):
        print("The quadratic equation " ,a, "*x^2 + " ,b, "x + " ,c, " = 0")

        D = b**2 - 4*a*c

        if D<0:
            print("has the following complex roots:")

            root_real =(-b)/(2*a)
            root_i =((abs(D))**(1/2)) / (2*a)

            print (root_real, " + ",root_i,"i")
            print ("and")
            print (root_real, " - ",root_i,"i")

        elif D==0:
            root = (-b)/(2*a)
            print("has only one solution, a real root:")
            print(root)


        elif D>0:
            root_1 = ((-b)+((D)**(1/2)))/(2*a) 
            root_2 = ((-b)-((D)**(1/2)))/(2*a)

            print("has the following real roots")
            print (root_1, " and " , root_2)
            
    if (a==0) and (b != 0):
        print("The linear equation " ,b, "x + ", c, " = 0")
        solution = (-c) / b
        print("has th following root/solution:" ,solution,)
        

    if (a == 0) and (b == 0) and (c != 0):
        print("The quadratic equation " ,a, "*x^2 + " ,b, "x + " ,c, " = 0\nis satisfied for no number x")       


    if (a == 0) and (b == 0) and (c == 0):
        print("The quadratic equation " ,a, "*x^2 + " ,b, "x + " ,c, " = 0\nis satisfied for all number x")
    


########### main ##########

print ("*************************************************************")
print ("*                                                           *")
print ("*  __Welcome to my math quiz-generator / equation-solver__  *")
print ("*                                                           *")
print ("*************************************************************")

print("")

name=input("What is your name? ")

status=input("Hi "+name+". Are you in? Enter \n1 for primary school\n2 for high school or\n3 for none of the above?\n")

if status=='1':

    print('*'*(69+len(name)))
    print("*", end="")
    print(' '*(67+len(name)), end="")
    print("*")
    print("*  __"+name+ ", welcome to my quiz-generator for primary school students.__  *")
    print("*", end="")
    print(' '*(67+len(name)), end="")
    print("*")
    print('*'*(69+len(name)))

    print("")

    print(name+ " what would you like to practice? Enter\n0 for subtraction\n1 for exponentiation")

    flag = int(input())

    n = int(input("How many questions would you like to do?"))

    primary_school_quiz(flag, n)
    
elif status=='2':

    print('*'*(61+len(name)))
    print("*", end="")
    print(' '*(59+len(name)), end="")
    print("*")
    print("*  __quadratic equation, a·x^2 + b·x + c= 0, solver for " +name+ "__  *")
    print("*", end="")
    print(' '*(59+len(name)), end="")
    print("*")
    print('*'*(61+len(name)))
    
    loop=True
    
    while loop:
        question=input(name+", would you like a quadratic equation solved?")
        
        if (question == 'Yes') or (question == 'YEs') or (question == 'YeS') or (question =='yES') or (question =='YES') or (question =='yes') or (question =='yeS') or (question =='yEs'):
            
            print("Good choice!")
            
            a= int(input("Enter a number for the coefficient a:"))
            b= int(input("Enter a number for the coefficient b:"))
            c= int(input("Enter a number for the coefficient c:"))

            high_school_eqsolver(a,b,c)
            
        else:
            
            loop = False
            
 
else:
    print("This Program is not for you")
    

print("Good bye "+name+"!")
