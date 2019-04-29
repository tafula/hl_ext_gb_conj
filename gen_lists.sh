#!/bin/sh

echo -n "Generating primes.txt... "
python generators/primegen.py -s > /dev/null 2>&1
echo "OK."

echo -n "Generating phis.txt... "
python generators/phigen.py -s > /dev/null 2>&1
echo "OK."

echo -n "Generating r2ns.txt... "
python generators/r2gen.py -s > /dev/null 2>&1
echo "OK."


