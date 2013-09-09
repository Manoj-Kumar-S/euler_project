from math import sqrt
import time

s = time.time()
def abundant(n):
    sum_ = 1
    for i in range(2, int(sqrt(n)) + 1):
        if not n%i:
            if i**2==n:
                sum_ += i
            else:
                sum_ += i + (n/i)
            if sum_ > n:
                return True

sum_ = sum(range(24))
for num in range(24, 28124):
    flag = 1
    for factor in range(12, num/2 + 1):
        if abundant(factor) and abundant(num - factor):
            flag = 0
            break
    if flag == 1:
        sum_ += num

print sum_
print time.time() - s
