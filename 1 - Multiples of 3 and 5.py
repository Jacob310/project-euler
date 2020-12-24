# A program to solve the first project Euler problem
"""
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
"""

y=[]
for i in range(1,1000):
    x = ""
    if i % 3 == 0:
        x = i
    if i % 5 == 0:
        x = i
    if x != "":
        #print(x)
        y.append(x)
print(y)
print(sum(y))
