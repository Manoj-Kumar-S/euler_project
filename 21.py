from math import sqrt

def divisors(n):
    sum = 0
    divlist = []
    k = n
    start = 2
    for j in range(2, int(sqrt(n)+1)):
        if not n%j:
            sum += j
            sum += (n/j)
    sum += 1
    return sum

list_ = range(2, 10000)

answer = []
for k in list_:
    r = divisors(k)
    if r != k and divisors(r) == k:
        answer.append(r)

print sum(answer)
