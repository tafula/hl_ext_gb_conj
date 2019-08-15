#!/bin/sh

echo -n "Generating figure_1.png...\n"
if python2 generators/figure_1.py ; then
    echo "\rOK.             \n"
fi

echo -n "Generating figure_2.png...\n"
if python2 generators/figure_2.py ; then
    echo "\rOK.              \n"
fi

echo -n "Generating figure_3.png...\n"
if python2 generators/figure_3.py ; then
    echo "\rOK.              \n"
fi


