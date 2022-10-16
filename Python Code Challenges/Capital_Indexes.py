def capital_indexes(word):
    Cap_Indexes = []
    x = 0

    for a in word:
        if str(a).isupper():
            Cap_Indexes.append(x)
        x +=1
    
    return Cap_Indexes

name = input("Enter a string  : ")

print(capital_indexes(name))

