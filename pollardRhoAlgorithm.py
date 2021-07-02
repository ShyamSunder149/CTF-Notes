# pollard rho algorithm for integer factorization

from itertools import count
from math import gcd
import sys

number, x = 1020304, 2								#number = number to be factorized x = 2

for cycle in count(1):								#count(1) = starts counting from 1 with a step of 1 till infinity
    y = x
    for i in range(2 ** cycle):						# for i in range 2^cycle
        x = (x * x + 1) % number
        factor = gcd(x - y, number)
        if factor > 1:
            print(factor)
            sys.exit()
