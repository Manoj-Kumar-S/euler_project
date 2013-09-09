fib = [0,1]
sum = 0 
while 1:
    fib.append(fib[-1] + fib[-2])
    if fib[-1] > 4000000:
        break
    if fib[-1] % 2 == 0:
        sum = sum + fib[-1]
print fib
print sum
