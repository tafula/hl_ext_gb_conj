from scipy import signal
import os.path
import sys

basepath = os.path.dirname(__file__)

# primes up to N
filepath = os.path.abspath(os.path.join(basepath, "..", "params.txt"))
N = 10**int(open(filepath).read().split()[1])


#####################################
##   F i l e   F u n c t i o n s   ##
#####################################

# separate words from file
def splita( f):
	everything = f.read()
	return everything.split()

# load primes.txt
def takeprimes( n, vet):
	primes = []
	for x in vet:
		if (int(x) <= n): primes.append(int(x))
		else: break
	return primes


#################
##   M a i n   ##
#################

filepath = os.path.abspath(os.path.join(basepath, "..", "lists", "primes.txt"))
primes = takeprimes(N, splita(open(filepath)))

filepath = os.path.abspath(os.path.join(basepath, "..", "lists", "r2ns.txt"))
f = open(filepath, 'w+')
f.truncate()

count = 0
Y = [0 for x in range(N+1)]
for p in primes:
	Y[p] = 1
	if p > count:
		print p
		count += 10000

Y.pop(0)

print "convolving..."

# Fast Fourier
xRTWO = signal.fftconvolve(Y, Y, mode='full') 

# Write terms into file
count = 0
for r2 in xRTWO:
	f.write(str(int(r2)+1) + ' ')
	count += 1
	if count > N: break


