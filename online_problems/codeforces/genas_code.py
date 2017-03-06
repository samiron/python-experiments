import sys
import math
import fileinput


INPUT = None
if len(sys.argv) > 2:
    INPUT = sys.argv[1]

def _print(v):
    sys.stdout.write(str(v))
    sys.stdout.flush()

def process(line):
    l, r, k = [int(x) for x in line.split()]
    
    v = 1
    found = False
    while (v <= r):
        if(v >= l):
            found = True
            _print(v)
            _print(' ')
        v = v*k

    if found == False:
        _print(-1)
    _print("\n")


f = fileinput.input(files=(INPUT))
for line in f:
    process(line)
f.close()

