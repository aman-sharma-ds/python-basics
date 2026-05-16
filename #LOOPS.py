#LOOPS
#for loop
name = "aman sharma"
for i in name:
    print(i)

colors = ["red","orange","yellow","green"]
for color in colors:
    print(color)
for i in color:
    print(i)

for i in range(5):
    print(i+1)

for i in range (1,7):
    print(i)

#while loop
i = 0 
while(i<3):
    print(i)
    i=i+1

i = 0
while(i<=5):
    print(i)
    i = i + 1

i = int(input("enter number: "))
while(i<=40):
    i = int(input("enter number: "))
    print(i)

i = 5
while(i>0):
    print(i)
    i = i - 1

#break and contineu
for i in range(12):
    if(i == 10):
        break
    print("5 * ", i+1, "=", 5 * (i+1))

for i in range(12):
    if(i == 10):
        continue
    print("5*", i+1, "=", 5*(i+1))
