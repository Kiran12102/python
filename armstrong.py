def start():
    num=int(input('enter a num'))
    is_armstrong(num)

def get_last_digit(num:int)->int:
    return num%10
def remove_last_digit(num:int)->int:
    return num//10
def count_digit(num:int)->int:
    count=0
    while num>0:
        num=remove_last_digit(num)
        count=count+1
    return count
def add(num1:int, num2:int)->int:
    return num1+num2

def armstrong(num:int)->int:
    count_of_digit=count_digit(num)
    res=0
    while num>0:
        last_digit=get_last_digit(num)
        res=add(res, pow(last_digit , count_of_digit))
        num=remove_last_digit(num)
    return res

def is_armstrong(num:int)->int:
    if num==armstrong(num):
        print('armstrong number')
    else:
        print('not armstrong number')
