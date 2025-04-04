import numpy as np


#integers
i = 10 # dec;are an integer
print("type(i) = ", type(i))

a_i = np.zeros(i,dtype=int) # declare an array of integers
print("a_i: ",a_i)
print("type(a_i): ", type(a_i))

print("type(a_i[0]):", type(a_i[0]))

# floats
x = 19.10 # declare a float
print("type(x): ", type(x))

y = 1.9e2 #float in scientific notation, quivalent to 1.9 * 10 ** 2
print("type(y): ", type(y))

z = np.zeros(i,dtype=float) # declaring an array of floats
print("z:", z)
print("(type(z):", type(z))
print("type(z[0]):", type(z[0]))

print("a_i + z =", a_i+z)