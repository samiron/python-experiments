import sys
import fileinput

FIRST_OUTPUT = False


def process(length, numbers):
    global FIRST_OUTPUT
    FIRST_OUTPUT = True

    n = int(length)
    all_numbers = numbers.split()

    div_2 = (n-1)/2
    if(n % 2) == 0:
        middle_pair = [div_2, div_2+1]
        last_iteration = n -1;
    else:
        middle_pair = [div_2, div_2]
        last_iteration = n

    pairs = [0, n-1]
    pointer = 1
    for i in range(0, last_iteration):
        _print(all_numbers[pairs[pointer]])
        FIRST_OUTPUT = False
        if pairs == middle_pair:
            if pairs[0]+1 == pairs[1]:
                pointer = not pointer
                _print(all_numbers[pairs[pointer]])
                pointer = not pointer
                pairs[0] += 1
                pairs[1] -= 1

        pairs[0] += 1
        pairs[1] -= 1
        pointer = not pointer

    print


def _print(count):
    global FIRST_OUTPUT
    if not FIRST_OUTPUT:
        sys.stdout.write(" ")
    sys.stdout.write(count)
    sys.stdout.flush()


##################
#   Main parts   #
##################
INPUT = None
if len(sys.argv) > 2:
    INPUT = sys.argv[1]

f = fileinput.FileInput(files=INPUT)
l1 = f.readline()
while l1:
    l2 = f.readline()
    process(l1, l2)
    l1 = f.readline()

f.close()
