a = range(1,101)

x = map(lambda x: (x*x),a)

print sum(a)*sum(a) - sum(x)
