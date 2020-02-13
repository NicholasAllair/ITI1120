#######################
#Nicholas Allair
#8147249
#assignment 5 part3

def digit_sum(n):
  if n == 0:
    return 0
  else:
    return (n%10) + digit_sum(n//10)

def digital_root(n):
    
    if len(str(n)) == 1:
        print(n)
        return (n)
    
    else:
        n = digit_sum(n)
        digital_root(n)


        
        


