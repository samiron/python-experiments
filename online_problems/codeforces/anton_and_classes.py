# http://codeforces.com/contest/785/problem/B
import sys
import fileinput

MAX_TIME = 1000000001  # 10^9+1


def process(cmaxs, cmine, pmaxs, pmine):
    _print(max((pmaxs - cmine), (cmaxs - pmine)))


def _print(diff):
    print max(0, diff)


def analyze_schedule(schedule, max_start, min_end):
    (s, e) = schedule.split()
    s = int(s)
    e = int(e)
    if s >= max_start:
        max_start = s
    if e <= min_end:
        min_end = e

    return [max_start, min_end]


#   Main parts   #
INPUT = None
if len(sys.argv) > 2:
    INPUT = sys.argv[1]

INH = fileinput.FileInput(files=INPUT)
n = INH.readline()

while n:
    n = int(n)
    chs_min_end = MAX_TIME
    chs_max_start = -1
    while n:
        (chs_max_start, chs_min_end) = analyze_schedule(INH.readline(), chs_max_start, chs_min_end)
        n -= 1

    prg_min_end = MAX_TIME
    prg_max_start = -1
    m = int(INH.readline().rstrip())
    while m:
        (prg_max_start, prg_min_end) = analyze_schedule(INH.readline(), prg_max_start, prg_min_end)
        m -= 1
    process(chs_max_start, chs_min_end, prg_max_start, prg_min_end)
    n = INH.readline()

INH.close()
