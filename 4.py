def palindrome(x):
    dummy = 0 
    temp = x  
    while x != 0:       
        c = x % 10
        dummy = dummy*10 + c
        x = x / 10
    if dummy == temp:
        return True
    else:
        return False


a = range(100,1000)

b = range(100,1000)

number = 297792 

palindrom = []

for x in a:
    for y in b:
        if palindrome(x*y) and x * y >= number: 
            number = x * y
            
    b.remove(x) 

print number
