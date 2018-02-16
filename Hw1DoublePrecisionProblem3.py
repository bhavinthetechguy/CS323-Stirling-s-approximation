import math
import numpy as np
factorial = 1
print "Factorial" ,"\tStirling" ,"\t\tAB Error" ,"\t\tRE Error"
for n in range(1,11):
	factorial *= n
	sl = math.sqrt(2*math.pi*n)*(n/math.e)**n
	x = np.float64(sl)
	ae = abs(factorial - x)
	re = abs(ae/factorial)
	print factorial ,"\t",'  ', x ,"\t",'   ', ae ,"\t",'    ', re
	
