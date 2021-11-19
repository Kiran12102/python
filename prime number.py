'''
def start():
    num=int(input('enter a number'))


def count_of_factors(num:int)->int:
    count_of_factors_of_num=int()
    for n in range(1,num+1):
        count_of_factors_of_num+=1

    return count_of_factors_of_num
def is_prime(num:int)->bool:
    if count_of_factors(num)==2: return True
    else:return False

print(is_prime)
'''
'''
num=int(input('enter a number'))

    
for n in range(2,num):
    if num%n==0:
        print('num is prime')
    else:
        print('not prime')
'''
 
        
    
