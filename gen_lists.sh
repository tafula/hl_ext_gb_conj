#!/bin/sh

echo -n "Generating primes.txt...\n"
if python2 generators/primegen.py ; then
    echo "\rOK.      \n"
fi

echo -n "Generating phis.txt...\n"
if python2 generators/phigen.py ; then
    echo "\rOK.      \n"
fi

echo -n "Generating r2ns.txt...\n"
if python2 generators/r2gen.py ; then
    echo "\rOK.                  "
fi


