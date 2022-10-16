def convert(param_list):
    return ["{}".format(j) for j in param_list]


# # using map
# def convert(ns):
#     return list(map(str, ns))


print(convert([1, 7, 3]))