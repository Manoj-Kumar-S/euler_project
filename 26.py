import time
s = time.time()

def recurr(x):
    recurr_list = []
    remainder_list = []
    initial = 10
    prevtemp = -1
    while 1:
        if not initial%x:
            return
        digit = initial/x
        recurr_list.append(digit)
        temp = initial%x
        if not temp in remainder_list:
            remainder_list.append(temp)
        else:
            index_ = remainder_list.index(temp)
            return len(remainder_list[index_:])
        initial=(temp)*10

max_ = 1
recdem = 1
for i in range(2, 1000):
    t = recurr(i)
    if t > recdem:
        recdem = t
        max_ = i
print max_, time.time() - s
