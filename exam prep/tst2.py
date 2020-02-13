def min_or_max_index (lst, TF):
    
    s_lst = lst.sort()

    print (s_lst[0])
    
    if TF == True:
        min_value = s_lst[0]
        pos = lst.index(min_value)
        
        return (min_value,pos)
        

        
