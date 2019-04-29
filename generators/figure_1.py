import matplotlib.pyplot as plt
from math import *
import os.path
import sys

basepath = os.path.dirname(__file__)

# phis up to N
filepath = os.path.abspath(os.path.join(basepath, "..", "params.txt"))
N = 10**int(open(filepath).read().split()[5])


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

# primality test
def isprime(n):
	ret = 1
	for i in range(2, int(floor(sqrt(n))+1)):
		if (n % i == 0):
			ret = 0
			break
	return ret

# gcd
def gcd(a, b):
	if (a % b == 0): return b
	else: return gcd(b, a % b)

# euler totient
def phi(n):
	v_phi = 1
	Dn = []
	lim = sqrt(n)
	for p in primes:
		if n == 1: break
		elif p <= lim:
			while n % p == 0:
				Dn.append(p)
				n /= p
		else:
			Dn.append(n)
			break
	while len(Dn) > 0:
		p = Dn[0]
		exp = 0
		while p in Dn:
			exp += 1
			Dn.remove(p)
		v_phi *= p**exp - p**(exp-1)
	return v_phi

# distinct prime divisor function
def omega(n):
	cont = 0
	for p in primes:
		if p > sqrt(n): break
		if n % p == 0:
			cont += 1
	return cont

	
#################
##   M a i n   ##
#################

filepath = os.path.abspath(os.path.join(basepath, "..", "lists", "primes.txt"))
primes = vectorize(N, splita(open(filepath)))

X = range(N+1)

#array xPIE
xPIE = [0]
i = 0
for n in range(1, N+1):
	try:
		if n < primes[i]: xPIE.append( i)
		else:
			i += 1
			xPIE.append( i)
	except IndexError:
		xPIE.append( i)

print "xPIE\n"

#array xPHI
xPHI = [0]
for n in range(1, N+1):
	xPHI.append( phi(n))
	
print "xPHI\n"
		
#array xOMEG		
xOMEG = [0]
for n in range(1, N+1):
	xOMEG.append( omega(n))
	
print "xOMEG\n"


# get rid of odd numbers
Y = []
for x in X:
	if x % 2 == 0: Y.append(x)
X = Y

	
#arrays xPW e x2PHI2
xPW = []
for n in X:
	xPW.append( xPIE[n] - xOMEG[n])

x2PHI2 = []
for n in X:
	x2PHI2.append( xPHI[n]/2)


# plot
params = {'axes.labelsize': 30,
         'axes.titlesize': 30,
         'xtick.labelsize': 30,
         'ytick.labelsize': 30}

plt.rcParams.update(params)

plt.xlabel('2n')
plt.text(50000, 19000, r'$\varphi(2n)/2$', fontsize=40, color='b')
plt.text(75000, 4000, r'$\pi(2n)-\omega(2n)$', fontsize=40, color='r')
plt.plot(X,x2PHI2, marker='.', linestyle = '', color='b')
plt.plot(X,xPW, linestyle = '-', color='r')
plt.show()




