"""
def fib(n):
    if n == 1 or n == 2:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)
"""
def digits(n):
    sum_ = 0
    while n:
        sum_ += 1
        n = n/10
    return sum_

a = 1
b = 1
count = 3
while 1:
    c = a + b
    if c == 144:
        print count
        break
    a = b
    b = c
    count += 1





