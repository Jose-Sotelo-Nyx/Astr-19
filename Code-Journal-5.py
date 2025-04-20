import numpy as np
from tabulate import tabulate
from astropy.table import Table
def fsin(x):
	return np.sin(x)

def main():
	x = np.linspace(0,2*np.pi,1000)
	y = fsin(x)

	table_data = [(a,b) for a, b in zip(x,y)]
	table_headers = ["x","sine(x)"]
	comparison_table = tabulate(table_data,tablefmt="grid", headers=table_headers, 
		floatfmt=".3f")

	print(table_data)
	print(comparison_table)

if __name__ == '__main__':
	main()