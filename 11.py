import time

s = time.time()
x = open('dance.txt','r')
numbers = []

while 1:
    a = x.readline()
    if a == '':
        break
    numbers.append(a.split())

multiply = []

for row in numbers:
    for i in range(len(row)):
        try:
            multiply.append(int(row[i]) * int(row[i+1]) * int(row[i+2]) * int(row[i+3]))
        except IndexError:
            break

for i in range(len(numbers)):
   for x in range(len(numbers)):
       try:
           multiply.append(int(numbers[x][i]) * int(numbers[x+1][i]) * int(numbers[x+2][i]) * int(numbers[x+3][i])) 
       except IndexError:
           break




for i in range(len(numbers)):
   k = i
   for num in range(i,len(numbers) - 3):
       multiply.append(int(numbers[num][num - k]) * int(numbers[num + 1][num - k +1]) * int(numbers[num +2][num - k + 2]) * int(numbers[num + 3][num - k + 3]))         


for i in range(len(numbers)):
   k = i
   for num in range(i , len(numbers) - 3):       
       multiply.append(int(numbers[num - k][num]) * int(numbers[num-k + 1][num +1]) * int(numbers[num-k+2][num + 2]) * int(numbers[num -k+ 3][num + 3]))        

for i in range(len(numbers)):

    numbers[i].reverse()

for i in range(len(numbers)):
   k = i
   for num in range(i,len(numbers) - 3):
       multiply.append(int(numbers[num][num - k]) * int(numbers[num + 1][num - k +1]) * int(numbers[num +2][num - k + 2]) * int(numbers[num + 3][num - k + 3]))         


for i in range(len(numbers)):
   k = i
   for num in range(i , len(numbers) - 3):       
       multiply.append(int(numbers[num - k][num]) * int(numbers[num-k + 1][num +1]) * int(numbers[num-k+2][num + 2]) * int(numbers[num -k+ 3][num + 3]))    


print numbers
print max(multiply)

print time.time() - s
