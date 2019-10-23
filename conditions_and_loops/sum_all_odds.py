# Given: Two positive integers a and b (a < b < 10000).
#
# Return: The sum of all odd integers from a through b, inclusively.
#
# Hint: You can use a % 2 == 1 to test if a is odd.

def sum_all_odd(a, b):
    sum = 0
    if a%2==0: a+=1
    for i in range(a, b, 2):
        sum +=i
    return sum


print(sum_all_odd(7134,7500))
