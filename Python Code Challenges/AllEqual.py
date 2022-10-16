def all_equal(new_lst):
    for num in range(len(new_lst)-1):
        if new_lst[num] != new_lst[num+1]:
            return False
    return True


print(all_equal([1,2,1,1]))