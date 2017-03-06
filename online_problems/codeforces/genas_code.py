import sys
import math
import fileinput

INPUT = None
if len(sys.argv) > 2:
    INPUT = sys.argv[1]

def _is_beautiful_number(number):
    n = len(number)
    return number == ("1" + "0" * (n-1))

def process(l1, l2):
    countries = int(l1)
    all_tanks = l2.split()
    
    zeros = 0
    ugly_num="1"
    for tank_count in all_tanks:
        if _is_beautiful_number(tank_count):
            zeros += len(tank_count) - 1
        elif tank_count == "0":
            print 0
            return
        else:
            ugly_num = tank_count
            
    print ugly_num + "0" * zeros
            
            

def _print(v):
    sys.stdout.write(str(v))
    sys.stdout.flush()


f = fileinput.FileInput(files=(INPUT))
l1 = f.readline()
while(l1):
    l2 = f.readline()
    process(l1, l2)
    l1 = f.readline()
    
f.close()

