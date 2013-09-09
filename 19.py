sun = 0
list1 = [1, 32, 60, 91, 121, 152, 182, 213, 244, 274, 305, 335]
list2 = [1, 32] + [element + 1 for element in list1[2:]]
day = 2
for year in range(1901, 2001):
    if year%4:
        days = 365
        list_ = list1
    else:
        days = 366
        list_ = list2
    for count in range(1, days+1):
        if not day%7 and count in list_:
            sun += 1
        day += 1
    day = (day%7)

print sun
