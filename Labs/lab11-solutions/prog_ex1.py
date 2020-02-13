def m(i):
     '''(int)->number
     returns the sum 1/3+2/5+3/7+...+i/(2i+1)
     Precondition: i>=1
     '''
     if i == 1:
          return 1 / 3
     else:
          return m(i - 1) + i * 1 / (2 * i + 1)


for i in range(1, 11):
     print('m('+str(i)+')=', m (i) )
