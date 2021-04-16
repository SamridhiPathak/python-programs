def palindrome(name1):
    rev_name=(name1[-1::-1])
    if(rev_name==name1):
        return "input word is palindrome"
    else:
      return "input word isn't palindrome"  
    
name=input('input a name')
print(palindrome(name))
