def double_letters(word):
    
    for count,value in enumerate (word):
        if(word[count -1] == value):
            return True

    return False
        
            

print(double_letters("hello"))