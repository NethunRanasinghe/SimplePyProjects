def largest_difference(n_list):
    n_list.sort()
    return n_list[-1] - n_list[0]

print(largest_difference([1, 2, 3]))