x = [0.0,3.0,5.0,2.5,3.7,2.5]#Declare a list of floats

print("x is", x)
print("type(x): ", type(x))

#remove the third element
x.pop(2)
print("x is ", x)

#adding an element at the end
x.append(1.2)
print("x.append(2) ",x)

#remove a specific elemnt
x.remove(2.5)
print("x.remove(2.5) ", x)

#make copy of a list
y = x.copy()
print("y = x.copy()?", y)

#how many elements are 0.0
y.count(0.0)
print("y.count(0.0)?", y.count(0.0))

#get the index of an specific element
y.index(3.7)
print("y.incdex(3.7)?", y.index(3.7))

#sort the list

y.sort()
print("y.sort()?", y)

#reverse the list
y.reverse()
print("y.reverse()?",y)

#erase the content of the list
y.clear()
print("y.clear()?",y)
print(type(y))








