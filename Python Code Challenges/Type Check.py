def only_ints(a,b):
    TypeCheck = lambda c,d : True if type(c) == int and type(d) == int else False
    return  TypeCheck(a,b)

print(only_ints(1,2))