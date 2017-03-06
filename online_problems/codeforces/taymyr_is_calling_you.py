import sys
import fractions
import math
import fileinput


def process(line):
    (n, m, z) = line.split()
    n = float(n)
    m = float(m)
    z = float(z)

    gcd = _lcm(n, m)
    count = math.floor(z/gcd)

    _print(int(count))


def _lcm(x, y):
    lcm = (x * y) // fractions.gcd(x, y)
    return lcm


def _print(count):
    print count


##################
#   Main parts   #
##################
INPUT = None
if len(sys.argv) > 2:
    INPUT = sys.argv[1]

f = fileinput.FileInput(files=INPUT)
l1 = f.readline()
while l1:
    process(l1)
    l1 = f.readline()

f.close()
