#FILE I/O
#reading to a file
f = open("demo.txt", "r")
data = f.read()
print(data)
print(type(data))

f = open("demo.txt", "r")
line1 = f.readline()
print(line1)

line2 = f.readline()
print(line2)

#writing to a file
f = open("demo.txt", "w")
f.write("i am study python.")

f.write("\nyou can also learn python")

#r+
f = open("demo.txt", "r+")
f.write("abc")

#w+
f = open("demo.txt", "w+")
print(f.read())
f.write("python")
f.close()

#a+
f = open("demo.txt", "a+")
print(f.read())
f.write("abc")

#deleting a file
import os
os.remove("untitled-1.txt")