# http://codeforces.com/contest/
import sys
import fileinput


def _is_match_by_rotation(ref_chars, chrs, start_point):
    i = 0
    j = start_point
    l = len(ref_chars)

    while i < l:
        if ref_chars[i] != chrs[j]:
            return False
        j = (j+1) % l
        i += 1
    return True


def _calculate_distance(reference, str):
    if reference == str:
        return 0
    _debug("Calculating distance between: %s %s", (reference, str))
    ref_chars = list(reference)
    chrs = list(str)

    start_point = 0
    match_point = None
    while start_point < len(ref_chars):
        if _is_match_by_rotation(ref_chars, chrs, start_point):
            match_point = start_point
            break
        start_point += 1

    _debug("distance: %s", match_point)
    return match_point


def process(count):
    count = int(count)
    strings = []
    while count > 0:
        strings.append(INH.readline().strip())
        count -= 1

    ref_index = 0
    min_sum = sys.maxint
    is_minus_one = False
    while ref_index < len(strings) and not is_minus_one:
        b_index = 0
        distance = 0
        while b_index < len(strings):
            if ref_index != b_index:
                d = _calculate_distance(strings[ref_index], strings[b_index])
                if d is None:
                    is_minus_one = True
                    break
                else:
                    distance += d
            b_index += 1
        min_sum = min(min_sum, distance)
        ref_index += 1

    if is_minus_one:
        print "-1"
    else:
        print min_sum


def _print():
    pass


#   Main parts   #
def _debug(string, params):
    if SPUDEBUG:
        print string % params


SPUDEBUG = False
INPUT = None
if len(sys.argv) > 2:
    INPUT = sys.argv[1]

INH = fileinput.FileInput(files=INPUT)
l1 = INH.readline()
while l1:
    process(l1)
    l1 = INH.readline()

INH.close()
