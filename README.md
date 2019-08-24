# Python scripts for figures in:
### *"An elementary heuristic for Hardy–Littlewood extended Goldbach's conjecture"* [arXiv:1508.05702](https://arxiv.org/abs/1508.05702)
 
----
## Description
### Fixed files
* *generators/\*gen.py*: Generators of lists (phi(n), primes and r\_{P,2}(n), described below).

* *generators/figure_\*.py*: Generators of images (described below)

* *params.txt:* Tells generators the upper limit of each list or image (default: primes up to 10^7 [primegen.py], Goldbach's comet up to 10^6 [figure_2.py], values of phi(n) up to 10^5 [phigen.py and figure1.py])

----
### Generated files
#### Images
* *imgs/figure_1.png:* Comparison between the graphs of phi(n) and pi(n)-omega(n), for even n <= 10^5.

* *imgs/figure_2.png:* Graph of the function r\_{P,2}(n), which counts the in how many ways n can be written as the sum of two primes (counting repetition), for even n <= 10^6.

* *imgs/figure_3.png:* Graph of the ratio between r\_{P,2}(n) and Hardy--Littlewood's conjectured estimate, for even n <= 10^7.

#### Lists
* *lists/phis.txt:* Values of Euler's totient function phi(n) for n <= 10^5, separated by space.

* *lists/primes.txt:* List of primes <= 10^7, separated by space.

* *lists/r2ns.txt:* Values of r\_{P,2}(n) for n <= 10^7, separated by space.

----
## How to run

### Linux
 1. Run gen_lists.sh
 2. Run gen_imgs.sh
 
### Not-linux
 1. Run generators/phigen.py
 2. Run generators/primegen.py
 3. Run generators/r2gen.py
 4. Run generators/figure_i.py (i = 1,2,3)
 
In both cases, lists are stored in ~/lists and images are stored in ~/imgs.

----
## Dependencies

All the Python scripts were written for Python 2.7. Apart from standard Python libraries, [SciPy](https://www.scipy.org/) and [Matplotlib](https://matplotlib.org/) are necessary to run the scripts.

----
## Time estimate

All programs run pretty fast (less than 30 secs), with the notable exception of *figure_3.py*. For a basis of comparison, a laptop with the specs
* *Processor:* Intel(R) Core(TM) i3-5005U CPU @ 2.00GHz,
* *Memory:* 4GiB, clock 1600MHz (0.6ns),
* *HDD:* WDC WD5000LPCX-6 500GB,

running *figure_3.py* for n up to 10^7 takes approximately 1h40mins.
