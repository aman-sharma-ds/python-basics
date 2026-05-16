print("aman sharma.", "My age is 18.")
print(12345)
print(18+3)
#1)variables
name = "aman" #string type data
age = 18 #integers
price = 18.18 #floats
print(name)
print(age)
print("my name is : ", name)
print("my age is : ", age)
print(type(name))
print(type(age))                                                                       
print(type(price))
age = 18
old = False #boolean
a = None #none
print(type(old))
print(type(a))
a = 6
b = 4
sum = a + b
print(sum)
a = 1000
b = 500
diff = a - b
print(diff)
#arithmetic operators
a = 5
b = 2
print(a + b)
print(a - b )
print(a * b)
print(a / b)
print(a % b)
print(a ** b)
#relational operators
a = 50 
b = 20
print(a == b)
print(a != b)
print(a > b)
print(a < b)
print(a >= b)
print(a <= b)
#assigmant operators
num = 10
num += 5
print("num :", num)
#logical operators
a = 50 
b = 30
print(not False)
print(not (a > b))
val1 = True
val2 = False
print("and operator:", val1 and val2)
print("or operator:", val1 or val2)
print("or operator:", (a == b) or (a > b))
#type conversion
a = 2
b = 4.25
sum = a + b
print(sum)
#a="2" error

#type casting
a = int("2")
b = 4.25
print(type(a))
print(a + b)

#bitwise operators
a = 10
b = 4
print(a&b)
print(-a)
print(a>>2)
print(a<<2)

#mambership operators
x = 24
y = 20
list_1 = [10,20,30,40,50]
if(x not in list_1):
    print("x is NOT present in list")
else:
    print("x is present in list")
if(y in list_1):
    print("y is present in list")
else:
    print("y is not present in list")

#identity operators
a = 10 
b = 20
c = 9
print(a is not a)
print(a is a)
print(a is not c)
