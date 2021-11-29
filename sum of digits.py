n=int(input('enter a number '))
d=n
res=0

while n>0:
    d=n%10
    res=res+d
    n=n//10
    
print(res)
