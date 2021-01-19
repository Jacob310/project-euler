"""
A palindromic number reads the same both ways. 
The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""

# x = 10
# #y = 10

# # while len(str(x)) < 3:
# #     #print(x)
# #     while len(str(y)) < 3:
# #         z = x * y
# #         print(z)
# #     x += 1
# #     y += 1

# for i in range(10,100):
#     z = x * i
#     for j in range(10,100):
#         y = z * j
#         print(y)
#     #print(z)

def is_pal(c):
    return int(str(c)[::-1]) == c

pal = 0

for a in range(999, 99, -1):
    for b in range(a, 99, -1):
        product = a * b
        if is_pal(product) and product > pal:
            pal = product

print(pal)

# product of two digit numbers create list of products
# for element in list:
    # list() function to separate number into list elements
    # use == to determine if lists are equal backwards
# append to new list
# find largest number