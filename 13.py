array = []

def digits(y):
    temp = []        
    x = int(y[0])
    while x > 0:
        temp.append(x % 10)
        x = x / 10
    return temp   

a = open('dance.txt','r')
while 1:
    x = a.readline()
    if x:
        array.append(digits(x.split()))
    else:
        break


dum = 0
answer = []
new = []

print array[98][0]

for i in range(50):
    son = 0
    for j in range(100):        
        son = son + array[j][i]
    son = dum + son
    new.append(son)
    answer.append(son % 10)
    dum = son / 10

print answer , new, len(answer)




