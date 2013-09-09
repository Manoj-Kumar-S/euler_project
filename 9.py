list1 = range(1,1000)
list2 = range(1,1000)


num = []
for x in list1:
    for y in list2:
        if x + y < 1000: 
            num.append([x,y,1000-(x + y)])
    list2.remove(x)
        

for x in num:
    x.sort()


for x in num:
    if x[0]*x[0] + x[1]*x[1] == x[2]*x[2]:
        print x[0] * x[1] * x[2]
        break






  

   


