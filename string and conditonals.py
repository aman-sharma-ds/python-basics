#CHP2:STRING AND CONDITONAL STATEMANT
#string
str1 = "this is string. we are study python"
str2 = "this is string.\n we are study python"
str3 = " this is string.\t we are study python"
print(str1)
print(str2)
print(str3)
#1)concatenation
str1 = "aman"
str2 = "sharma"
print(str1+str2)
#2)length
print(len(str1))
print(len(str2))
#indexing
str = "aman sharma"
print(str[0])
print(str[1])
print(str[2])
print(str[3])
print(str[4])
#slicing
str = "aman sharma"
print(str[0:4])
print(str[1:4])
print(str[5:11])
#isika part hai negative index
str = "aman"
print(str[-4:-1])
print(str[-3:-1])
#string function
#1)endwith("word")
str = "my name is aman sharma"
print(str.endswith("rma"))
print(str.endswith("sha"))
#2)capitalizes 1st char
str = "my name is aman sharma"
print(str.capitalize())
#3)replace any word
str = "my name is aman sharma "
print(str.replace("a", "m"))
print(str.replace("aman", "annu"))
#4)find
str = "my name is aman sharma "
print(str.find("e"))
print(str.find("aman"))
print(str.find("q"))
#5)count word
str = "my name is aman sharma"
print(str.count("name"))
print(str.count("m"))
#Q wap to input user first name and print its length
name = input("enter your name")
print("length of your name is", len(name))
#Q wap to find the occurence of $ in a string
str = "hi, $i am the $ symbol $99.99"
print(str.count("$"))
#CONDITIONAL STATEMENT
#1)if,else
a = int(input("enter your age: "))
print("your age is: ", a)
if(a > 18):
    print("you can drive")
else:
    print("you cannot drive")

appleprice = (210)
budget = (200)
if(appleprice >= budget):
    print("aman can buy apple.")
else:
    print("aman cannot buy apple")

#2)if,elfe
num = int(input("enter the value num: "))
if(num < 0):
    print("number is negative.")
elif(num == 9996):
    print("number is zero.")
else:
    print("number is positive")