# http://codeforces.com/contest/664/problem/C
import sys
import fileinput

"""
Imagine a number system that starts from 1989
Starting from this point, for first 10 numbers
the last most single digit will be used as "y".
for next 100 number (10 - 99) last two digits will be used
as "y".
Following table lists the valid ranges from each length of
"y". It can be observed form below that either "y" directly
belong to a range or we just need to add a "1" to next the 
original year.
"""

RANGES = [[1989, 1998],             #         0 - 9
          [1999, 2098],             #        10 - 99
          [2099, 3098],             #       100 - 999
          [3099, 13098],            #      1000 - 9999
          [13099, 113098],          #     10000 - 99999
          [113099, 1113098],        #    100000 - 999999
          [1113099, 11113098],      #   1000000 - 9999999
          [11113099, 111113098],    #  10000000 - 99999999
          [111113099, 1111113098]   # 100000000 - 999999999
          ]


def _calculate(yearfix):
    length = len(yearfix)
    (start, end) = RANGES[length - 1]
    _debug("Year fix: %6s, Range: [%s, %s]", (yearfix, start, end))

    if length <= 3:
        for year in range(start, end+1):
            if str(year).endswith(yearfix):
                return str(year)
    else:
        if start <= int(yearfix) <= end:
            return yearfix
        else:
            return "1"+yearfix
    return "nothing"


def process(n):
    n = int(n)
    while n > 0:
        parts = INH.readline().strip().split('\'')
        yearfix = parts[1]
        _print(_calculate(yearfix))
        n -= 1


def _print(output):
    print output


#   Main parts   #
def _debug(string, params):
    if SPUDEBUG:
        print string % params


SPUDEBUG = False
INPUT = None
if len(sys.argv) > 2:
    INPUT = sys.argv[1]

INH = fileinput.FileInput(files=INPUT)
n = INH.readline().strip()
while n:
    process(n)
    n = INH.readline()

INH.close()
