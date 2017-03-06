import sys
import math
import fileinput

IN_FILE= None
if len(sys.argv) > 2:
    IN_FILE = sys.argv[1]

INPUT = fileinput.FileInput(files=(IN_FILE))

def process(n, xc, yc):
    max_distance = -1
    min_distance = sys.maxint
    while(n > 0):
        n -= 1
        x, y = [int(x) for x in INPUT.readline().split()]
        distance = math.sqrt((xc - x)**2 + (yc - y)**2)
        if(distance > max_distance):
            max_distance = distance
        if(distance < min_distance):
            min_distance = distance
            
    output = ((max_distance ** 2 ) * math.pi) - (( min_distance ** 2 ) * math.pi)
    print output
            

def _print(v):
    sys.stdout.write(str(v))
    sys.stdout.flush()


line = INPUT.readline()
while(line):
    n, xc, yc = [int(x) for x in line.split()]
    process(n, xc, yc)
    line = INPUT.readline()
INPUT.close()

