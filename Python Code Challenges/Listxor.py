def list_xor(n,list1,list2):
    e_xor1 = lambda a,l1,l2: True if a in l1 and a not in l2 else False
    e_xor2 = lambda a,l1,l2: True if a in l2 and a not in l1 else False

    if e_xor1(n,list1,list2) or e_xor2(n,list1,list2) is True:
        return True
    else:
        return False


print(list_xor(1, [1, 2, 3], [1, 5, 6]))