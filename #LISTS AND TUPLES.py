#LISTS AND TUPLES
#1)list in python
marks = [1.5,2.6,6.3,]
print(marks)
print(type(marks))

#length
print(len(marks))

#index
print(marks[0])
print(marks[1])

#slicing
print(marks[0:3])
print(marks[1:2])
print(marks[-3:-2])
#
student = ["aman",9.4,18,"mumbai"]
print(student)
student[0] = "annu"
print(student)
#LIST MATHODS #hum isme word number kuch bhi le sakte hai
#1)append(any one)
list = [1,2,3]
list.append(4)
print(list)
#2)sort()
list = [2,3,1]
list.sort()
print(list)
#3)sort(reverse=true)
list = [1,2,3]
list.sort(reverse=True)
print(list)
#4)reverse()
list = [2,1,3]
list.reverse()
print(list)
#5)insert
list = [1,2,3]
list.insert(1,5)
list.insert(1,4)
print(list)
#6)remove 
list = [1,2,3,4]
list.remove(4)
print(list)
#7)pop(ind)
list = [1,2,3]
list.pop(0)
print(list)

#TUPLES IN PYTHON
tup = (1,2,3,4)        
print(type(tup))
print(tup[0])  
print(tup[0:4])     
tup = ()
print(type(tup))
print(tup)

tup = ("aman",)
print(tup)
print(type(tup))

#tuple methods
#index
tup = (1,2,3,4,)
print(tup.index(1))
print(tup.index(3))

#count
tup = (1,2,3,4,4)
print(tup.count(4))

#QUESTION
#1)
movies = []
mov1 = input("enter first movie: ")
mov2 = input("enter second movie: ")
mov3 = input("enter third movie: ")

movies.append(mov1)
movies.append(mov2)
movies.append(mov3)
print(movies)