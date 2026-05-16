#DICTIONARY AND SET
marks = {
    "aman" : 100,
    "annu" : 76,
    "neela" : 56
}
print(marks,type(marks))
print(marks['neela'])

#properties of dictionaries
#1)it is unordered
#2)it is mutable
#3)it is indexed
#4)cannot contain duplicate keys

#DICTIONARY METHOD
#1)a.itemes
marks = {
    "aman" : 100,
    "annu" : 98,
    "neelu" : 45
}
print(marks.items())

#2)a.keys
marks = {
    "aman" : 45,
    "neelu" : 100,
    "annu" : 65
}
print(marks.keys())

#3)a.update
marks = {
    "neelu" : 200,
    "annu" : 100,
    "aman" : 50
}
marks.update({"aman": 60})
print(marks)
marks.update({"monali": 300})
print(marks)

#4)a.get
marks = {
    "aman" : 100,
    "neelu" : 50,
    "annu" : 25
}
print(marks.get("aman"))
#print(marks.get['aman2'])#error

#5)a.values
marks = {
    "aman" : 3,
    "annu" : 4,
    "neelu" : 5
}
print(marks.values())

#SET IN PYTHON
collection = {1,2,3,4}
print(collection)
print(type(collection))

collection = {1,2,2,3,3}
print(collection)
print(len(collection))
#empty set
num = set()
print(num)

#SET METHOD
#1)a.add
marks = set()
marks.add(2)
marks.add(4)
print(marks)

#2)a.remove
marks = {1,2,3,4}
marks.remove(2)
print(marks)

#3)a.clear
marks = {5,4,3,2,1}
marks.clear()
print(marks)

#4)a.pop
marks = {5,4,3,2,1}
marks.pop()
print(marks)

#5)a.union
set1 = {1,2,3}
set2 = {2,3,4}
print(set1.union(set2))

#6)a.intersection
set1 = {1,2,3}
set2 = {3,4,5}
print(set1.intersection(set2))