a = [0, 3, 3, 5, 4, 4, 3, 5, 5, 4]
ten = [3, 6, 6, 8, 8, 7, 7, 9, 8, 8]
hor = [0, 0, 6, 6, 5, 5, 5, 7, 6, 6]

def con_to_num(i):
	ans = 0
	h = i / 100  # hundreds digit
	t = (i - (h*100)) / 10  # tens digit
	s = (i - (h*100) - (t*10))  # ones digit
	if h:
		ans += a[h] + len('hundred')
		if t == 1:  # eleven type
			ans += ten[s] + len('and')
		elif s or t:
			ans += a[s] + hor[t] + len('and')
	else:
		if t == 1:
			ans += ten[s]
		else:
			ans += hor[t] + a[s]
	return ans
sum = 0
for i in range(1, 1000):
	sum += con_to_num(i)

print sum + len('onethousand')