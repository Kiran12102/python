def count():
    n=int(input('eneter a num'))
    count=0
    while (n>0):
        n = n//10
        count = count+1

    print(count, 'is a number of digits in number')

    
