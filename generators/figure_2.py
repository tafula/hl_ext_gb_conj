import matplotlib.pyplot as plt
from math import *
import os.path
import sys

basepath = os.path.dirname(__file__)

# goldbach's comet limit
filepath = os.path.abspath(os.path.join(basepath, "..", "params.txt"))
N = 10**int(open(filepath).read().split()[3])


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

	
#################
##   M a i n   ##
#################
	
filepath = os.path.abspath(os.path.join(basepath, "..", "lists", "r2ns.txt"))
xRTWO = vectorize(N, splita(open(filepath)))
print "xRTWO\n"

X = range(2, N)

# get rid of odd numbers
Y = []
for x in X:
	if x % 2 == 0: Y.append(x)


# array to be ploted
xSIM = []
for n in Y:
	xSIM.append( xRTWO[n-2] )
	if n % 10000 == 0: print n  #printing to keep track of progress


# plot
params = {'axes.labelsize': 30,
         'axes.titlesize': 30,
         'xtick.labelsize': 30,
         'ytick.labelsize': 30}

plt.rcParams.update(params)
plt.ticklabel_format(style='sci', axis='x', scilimits=(0,0))
plt.ticklabel_format(style='sci', axis='y', scilimits=(0,0))

plt.xlabel('n (even)')
plt.ylabel(r'$r_{\mathbb{P},2}(n)$')
plt.plot(Y,xSIM, marker=',', linestyle='', color='b')
plt.show()

	
