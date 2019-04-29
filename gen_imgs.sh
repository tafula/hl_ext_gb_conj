#!/bin/sh

echo -n "Generating figure_1.png... "
python generators/figure_1.py -s > /dev/null 2>&1
echo "OK."

echo -n "Generating figure_2.png... "
python generators/figure_2.py -s > /dev/null 2>&1
echo "OK."

echo -n "Generating figure_3.png... "
python generators/figure_3.py -s > /dev/null 2>&1
echo "OK."


