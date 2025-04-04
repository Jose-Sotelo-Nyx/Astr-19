#define a dictionary data structure

#dictionnaries have a key value for each element
class_information = {
	"class" : "ASTR 19",
	"prof" : "Artem",
	"awesomeness": 9000

}

print("type(class_information):",type(class_information))
# get a value from the key
course = class_information["class"]
print("course: ",course)

# change a value via key
class_information["awesomeness"] +=1 #increment by 1
print(class_information)

#print dictionary elements by elemnt

for x in class_information.keys():
	print(x,class_information[x])




