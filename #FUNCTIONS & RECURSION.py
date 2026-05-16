#FUNCTIONS & RECURSION
def calc_sum(a, b):
    sum = a + b
    print(sum)
    return sum
calc_sum(5, 10)
calc_sum(10, 3)
calc_sum(7, 45)

def calc_avg(a,b,c):
    sum = a+b+c
    avg = sum / 3
    print(avg)
    return avg
calc_avg(1,2,3)

#defult parameters
def calc_prod(a=4,b=2):
    print(a*b)
    return a*b
calc_prod()

#recursion
def show(n):
    if(n == 0):
        return
    print(n)
    show(n-1)
show(5)

def show(n):
    if(n == -1):
        return
    print(n)
    show(n-1)
show(5)

def fact(n):
    if(n == 1 or n == 0):
        return 1
    return fact(n-1) * n
print(fact(4))