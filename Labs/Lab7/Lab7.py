#5.16
def indexes (word, char):
    '''list,string -> list
    program returns the location of a letter in word '''

    word = list(word)
    x = []

    for i in range(len(word)):
            if char == word[i]:
                x.append(i)
    return x
#5.17
def doubles (lst):

    for i in range(len(lst)-1):
        if 2*lst[i] == lst[i+1]:
            print(lst[i+1])
#5.18
def four_letter(lst):

    x = []

    for i in range(len(lst)):
        if len(lst[i]) == 4:
            x.append(lst[i])

    return x
#5.19 
def inBoth (lst1, lst2):

    for i in range(len(lst1)):
        if lst1[i] in lst2:
            return True
    for i in range(len(lst2)):
        if lst2[i] in lst1:
            return True
    return False
#5.20
def intersect (lst1,lst2):
    x = []
    for i in range(len(lst1)):
        if (lst1[i] in lst2) and (lst1[i] not in x):
            x.append(lst1[i])
    for i in range(len(lst2)):
        if (lst2[i] in lst1) and (lst2[i] not in x):
            x.append(lst2[i])
    return x
#5.21

    
    
        
    
        
        
    
            
        
    
        
            
