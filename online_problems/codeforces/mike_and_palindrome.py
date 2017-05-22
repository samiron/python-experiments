# http://codeforces.com/contest/798/problem/A
import sys
import fileinput


def process(str):
    _debug(str, ())
    letters = list(str)
    i = 0
    j = len(letters) - 1
    while letters[j] == "\n":
        j -= 1

    changes = 0
    while i < j:
        if letters[i] != letters[j]:
            changes += 1
        j -= 1
        i += 1

    if changes == 0 and i == j:
        changes = 1

    _print(changes)


def _print(changes):
    if changes == 1:
        print "YES"
    else:
        print "NO"


#   Main parts   #
def _debug(string, params):
    if SPUDEBUG:
        print string % params


SPUDEBUG = False
INPUT = None
if len(sys.argv) > 2:
    INPUT = sys.argv[1]

INH = fileinput.FileInput(files=INPUT)
l1 = INH.readline().rstrip().strip()
while l1:
    process(l1)
    l1 = INH.readline()

INH.close()
