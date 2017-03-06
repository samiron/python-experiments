import sys
import math
import fileinput


INPUT = None
if len(sys.argv) > 2:
    INPUT = sys.argv[1]
    
def process(line):
    


def _print(v):
    sys.stdout.write(str(v))
    sys.stdout.flush()


f = fileinput.input(files=(INPUT))
for line in f:
    process(line)
f.close()

