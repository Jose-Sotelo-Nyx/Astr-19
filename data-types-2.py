#boolans

yes = True
print("type(yes): ", type(yes))

no = False
print("type(no): ", type(no))

#List: ordered and changeable

alpha_list = ['a','b','c']
print("type(alpha_list):", type(alpha_list))
print("type(alpha_list[0]):", type(alpha_list[0]))
alpha_list.append('d')
print(alpha_list)

# Tuple: order and unchangable
alpha_tuple = ('a','b','c')
print("type(alpha_tuple): ",type(alpha_tuple))

try:
	alpha_tuple[2] = 'd'
except TypeError:
	print("Cannot change tuple")