def isprime(x):
    for i in range(2,x):
        if x % i == 0:
            return False
    return True

i = 0
count = 2
prime = []
while 1:
    
    if isprime(count):
         
        prime.append(count)
    count = count + 1
    
    
    if len(prime) == 10001:
        break

print len(prime)
print prime  
