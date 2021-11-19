num=int(input('enter a number  '))
temp=num
res=0
while num>0:
    d=num%10
    num==num//10
    a = fact(d)
    res=res+a
if total==temp:
    print("the number is a strong num")
else:
    print("the number is not strong number")



def fact(n):
    i=1
    f=1
    while i<=n:
        f=f*i
        i=i+1
    return f
