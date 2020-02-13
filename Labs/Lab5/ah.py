def ah(l,x,y):
    lst = []
    while x <= y:
        lst.append(x)
        x +=1
        print(lst)
        
    for i in range(len(l)):
        print (l[i])
            
t=[5, 1, -2.5, 10, 13, 8]
ah(t, 2,11)
