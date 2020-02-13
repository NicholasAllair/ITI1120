def orange(n):
    if n > 0:
        print(n, end=" ")
        orange(n-2)

orange(10)

print ('new')

def guava(n):
    if n>0:
        guava(n-2)
        print (n,end=" ")
        
guava(10)
