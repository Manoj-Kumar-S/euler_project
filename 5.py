def isprime(x):
    for n in range(2,x):
        if x % n == 0:
            return False
    return True
number = 1


def factors(number,factor):
    x = number
    for i in range(2,x):
        if isprime(i) and x % i == 0:
            factor.append(i)
            x = x / i
     
    if x == 1 or isprime(x):
        factor.append(x)
        return  
    else:
        factors(x,factor)

notprime = []


def primefactors(parent,daughter):
    
    for x in daughter:
        daughter_count = daughter.count(x)
        parent_count = parent.count(x)
        if daughter_count > parent_count:
            for y in range(daughter_count):
                daughter.remove(x)
            time = daughter_count - parent_count
            for i in range(time):
                parent.append(x)         


prime = []


for x in range(1,21):
    if isprime(x):
        prime.append(x)
        number = number * x
    else:    
        notprime.append(x) 





for x in notprime:
    print x
    if number % x == 0:
        pass
    else:
        pf = []
        factors(x,pf)
        primefactors(prime,pf) 
        

number = 1

for x in prime:
    number = number * x

print number




