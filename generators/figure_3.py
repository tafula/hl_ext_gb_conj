import scipy.integrate as integrate
import matplotlib.pyplot as plt
from math import *
import os.path
import sys

basepath = os.path.dirname(__file__)

# Twin primes constant
C2 = 0.660161815846869573927812110014

# values up to N
filepath = os.path.abspath(os.path.join(basepath, "..", "params.txt"))
N = 10**int(open(filepath).read().split()[1])


#####################################
##   F i l e   F u n c t i o n s   ##
#####################################

# separate words from file
def splita( f):
	everything = f.read()
	return everything.split()

# take array from file
def vectorize( n, vet):
	vector = []
	for x in vet:
		if (int(x) <= n): vector.append(int(x))
		else: break
	return vector


#################################################
##   A r i t h m e t i c   F u n c t i o n s   ##
#################################################

# Hardy-Littlewood factor
def hlfactor(n):
	prod = 1
	for p in primes:
		if p > sqrt(n): break
		else:
			if (p > 2) and (n % p == 0): prod *= float(p-1)/(p-2)
	return prod

# integral[2..n-2] dt/(log t)(log n-t)
def int_factor(n):
	return integrate.quad(lambda t: (1/log(n-t))*(1/log(t)), 2, n-2)[0]


	
#################
##   M a i n   ##
#################
	
filepath = os.path.abspath(os.path.join(basepath, "..", "lists", "primes.txt"))
primes = vectorize(N, splita(open(filepath)))

filepath = os.path.abspath(os.path.join(basepath, "..", "lists", "r2ns.txt"))
xRTWO = vectorize(N, splita(open(filepath)))
print "xRTWO\n"

X = range(2,N)

# get rid of odd numbers
Y = []
for x in X:
	if x % 2 == 0: Y.append(x)


# array to be ploted
xSIM = []
for n in Y:
	try:	
		xSIM.append( (xRTWO[n-2])/( 2 * C2 * hlfactor(n) * int_factor(n) ) )
	except (ZeroDivisionError, ValueError):
		xSIM.append(1)

	if n % 10000 == 0: print n #printing to keep track of progress


# plot
params = {'axes.labelsize': 30,
         'axes.titlesize': 30,
         'xtick.labelsize': 30,
         'ytick.labelsize': 30}

plt.rcParams.update(params)
plt.ticklabel_format(style='sci', axis='x', scilimits=(0,0))

plt.xlabel('n (even)')
plt.ylabel('ratio')
plt.ylim((0,2))

plt.plot(Y,xSIM, marker=',', linestyle='', color='r')
plt.show()

	
