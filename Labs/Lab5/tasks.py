import math
import random


#################################################################################
'''
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
        

    
high_school_eqsolver(0,0,4)
'''
#################################################################################

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
            i_answer = int(input("What is the result of" ,a,"-" ,b, "?  "))

            if (r_answer == i_answer):
                mark +=1

            question_n += 1

    if flag == 1:
        while question_n <= n:
                           
            a = (random.randint(0,9))
            b = (random.randint(0,9))

            r_answer = a**b
            
            print("Question ",question_n, ":")
            i_answer = int(input("What is the result of" ,a,"^" ,b, "?  "))

            if (r_answer == i_answer):
                mark +=1

            question_n += 1

    performTest(mark,n)

primary_school_quiz(0, 3)



