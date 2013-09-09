import time
s = time.time()
list_ = xrange(10)

def lex_perm(num_list):
    if len(num_list) == 2:
        max_ = max(num_list)
        min_ = min(num_list)
        for i in range(2):
            if not i:
                yield [min_, max_]
            else:
                yield [max_, min_]
    else:
        for num in num_list:
            temp_list = num_list[:]
            temp_list.remove(num)
            for perm in lex_perm(temp_list):
                permtemp = perm[:] 
                permtemp.insert(0, num)
                yield permtemp

generator = lex_perm(range(10))
i = 1
for term in generator:
    if i == 1000000:
        print term
        break
    i += 1

print time.time() - s
