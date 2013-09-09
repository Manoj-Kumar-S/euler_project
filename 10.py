import math
import time

y = time.time()


def isprime(x):
    for p in range(2,int(math.sqrt(x) + 2)):
        if x % p == 0:
            return False
    return True



num = 5

prime = 5

while num < 2000000:
    if isprime(num):
        
        prime = prime + num
    num = num + 2
    if num < 2000000 and isprime(num):
        prime = prime + num
    num = num + 4


print prime

print time.time() - y
