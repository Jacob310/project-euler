"""
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""

# import math

# print('Enter number')
#x = 13195
#x = int(input())
#y = math.sqrt(x)
# z = 1
w = []
# print('The square root of ' + str(x) + ' is ' + str(y))

# while z <= y:
#     #print(z)
#     if x % 2 == 0:
#         print(str(x) + ' is even - not a prime number.')
#         break
#     if x % z == 0:
#         #print(str(x) + ' is divisible by 3.')
#         w.append(z)
    # if z % 5 == 0:
    #     print(str(x) + ' is divisible by 5.')
    #     w.append(z)
    # if x % 7 == 0:
    #     print(str(x) + ' is divisible by 7.')
    #     w.append(z)
    #z = z + 1

#print(w)
    #if x % z == 0:

# for i in range(1,x+1):
#     #if i <= y:
#     #print(i)
#     # if x % 2 == 0:
#     #     print(str(x) + ' is even - not a prime number.')
#     #     continue
#     if i % 3 == 0 and i % 2 != 0:
#         print(str(i) + ' is divisible by 3')
#         w.append(i)
#     # if i % 5 == 0 and i % 2 != 0:
#     #     print(str(i) + ' is divisible by 5')
#     #     w.append(i)
#     if i % 7 == 0 and i % 2 != 0:
#         print(str(i) + ' is divisible by 7')
#         w.append(i)
#     if i % 13 == 0 and i % 2 != 0:
#         print(str(i) + ' is divisible by 13')
#         w.append(i)
# print(w)

# input number
# list of primes
# sqrt of number
# iterate through prime list with modulus
# add to list
# take last number from list


# Python program to print all 
# prime number in an interval
#number should be greater than 1
# end = int(input())
# y = int(math.sqrt(end))
# #print(y)
# w = []
 
# for i in range(y-1000,y):
#   if i>1:
#     for j in range(2,i):
#         if(i % j==0):
#             break
#     else:
#         if i <= y:
#             w.append(i)
# print(w)
# print(w[-1])
print('Enter number:')
n = int(input())
i = 2
x = str(n)

while i * i < n:
    while n % i == 0:
        n = n / i
    i = i + 1

print('The largest prime factor of ' + x + ' is ' + str(n))