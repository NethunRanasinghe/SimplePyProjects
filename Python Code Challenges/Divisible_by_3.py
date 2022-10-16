def div_3(num):
    divisible_check = lambda a:True if a % 3 == 0 else False
    return divisible_check(num)

print(div_3(6))