def is_palindrome(s):
     '''(str)->bool
     Returns True if string s forms a palindrom and False otherwise
     '''
     if len(s) <= 1: # base case
          return True
     elif (s[0].lower()  != s[len(s)-1].lower() ):
          return False
     else:
          return is_palindrome(s[1:len(s)-1])  


def is_palindrome_v2(s):
     '''(str)->bool
     Returns True if string s forms a palindrom and False otherwise
     (while ignoring all special characters)
     '''
     if len(s) <= 1: # base case
          return True
     else:
          first=s[0].lower()
          last=s[len(s)-1].lower()

          if first.isalpha() and last.isalpha():
               if first==last:
                    return is_palindrome_v2(s[1:len(s)-1])
               else:
                    return False
          elif not last.isalpha(): #remove the last character
               return is_palindrome_v2(s[0:len(s)-1])
          else : # now we know that first.isalpha() is False
               # thus remove first character
               return is_palindrome_v2(s[1:len(s)]) 
 
