a = range(1000)
answer = []
for x in a:
    if x % 3 == 0 or x % 5 == 0:
        answer.append(x)
print answer

print sum(answer) 
