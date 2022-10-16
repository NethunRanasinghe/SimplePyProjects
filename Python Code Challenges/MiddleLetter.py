def mid(pword):
    
    if (len(pword)%2 == 0):
        return ""
    else:
        return pword[int(len(pword)/2)]

    
word = "aaaa"

print(mid(word))