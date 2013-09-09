def isprime(x):
    for z in range(2,x/2):
        if x % z == 0:
            return False
    return True

number = 600851475143

count = 3

prime = []
while number != 1:
    if isprime(count) and number % count == 0:
        prime.append(count)
        number = number/count
    count = count + 1
       
print prime
