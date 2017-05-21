# http://codeforces.com/contest/664/problem/C
import sys
import fileinput


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
    yearfix_int = int(yearfix)
    (start, end) = RANGES[length - 1]
    _debug("Year fix: %6s, Range: [%s, %s]", (yearfix, start, end))

    if length <= 3:
        for year in range(start, end+1):
            if str(year).endswith(yearfix):
                return str(year)
    else:
        if start <= yearfix_int <= end:
            return yearfix
        else:
            prefix = 1
            candidate = str(prefix) + yearfix
            while int(candidate) <= end:
                prefix += 1
                candidate = str(prefix) + yearfix
            return candidate

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
