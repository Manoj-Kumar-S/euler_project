import time
s = time.time()

count = []
num = 1


def collatz(x,count,num,init):
    if x % 2 == 0:
        
        if x < init:
            count.append(num + count[x - 2] - 1)
            return
        
        
        collatz(x/2 , count , num + 1, init)
    elif x == 1:
        count.append(num)
        return
    else:
        
        if x < init:
            count.append(num + count[x - 2] - 1)
            return 
        
        
        collatz(3 * x + 1 , count , num +1 , init)

i = 2

while i < 1000000 :
    num = 1
    collatz(i , count ,num,i)
    i = i + 1

print count.index(max(count)) + 2


print time.time() - s
