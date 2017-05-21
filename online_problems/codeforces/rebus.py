# http://codeforces.com/contest/
import sys
import fileinput


def process(equation):
    tokenized = equation.split()
    plus_count = 1
    minus_count = 0
    sum = int(tokenized[-1])

    for token in tokenized:
        if token == '+':
            plus_count += 1
        if token == '-':
            minus_count += 1

    #print "Plus: %s, Minus: %s, sum: %s" % (plus_count, minus_count, sum)

    minus_sub_total = minus_count
    plus_sub_total = sum + minus_sub_total

    #print "Minus sub total: %s, Plus sub total: %s" % (minus_sub_total, plus_sub_total)

    if plus_sub_total < sum or plus_sub_total > (plus_count*sum):
        _print()
    elif minus_count > 0 and minus_sub_total >= (minus_count*sum):
        _print()
    else:
        plus_unit_number = minus_unit_number = None
        plus_remainder = minus_remainder = None
        plus_numbers = minus_numbers = None

        if plus_count > 0:
            plus_unit_number = int(plus_sub_total / plus_count)
            plus_remainder = plus_sub_total - (plus_unit_number*plus_count)
            plus_numbers = [plus_unit_number] * plus_count
            if plus_remainder > 0:
                i = 0
                while plus_remainder > 0 and i < len(plus_numbers):
                    idiff = sum - plus_numbers[i]
                    portion = min(idiff, plus_remainder)
                    plus_numbers[i] += portion
                    plus_remainder -= portion
                    i += 1

        if minus_count > 0:
            minus_unit_number = int(minus_sub_total / minus_count)
            minus_remainder = minus_sub_total - (minus_unit_number*minus_count)
            minus_numbers = [minus_unit_number] * minus_count
            if minus_remainder > 0:
                minus_numbers[0] += minus_remainder

        #print "Plus unit number: %s, minus unit number: %s" % (plus_unit_number, minus_unit_number)
        #print "Plus remainder: %s, Minus remainder: %s" % (plus_remainder, minus_remainder)
        #print "Plus numbers: %s" % plus_numbers
        #print "Minus numbers: %s" % minus_numbers

        n = plus_numbers.pop()
        for i in range(0, len(tokenized)-2):
            token = tokenized[i]
            if token == '-':
                n = minus_numbers.pop()
            elif token == '+':
                n = plus_numbers.pop()
            elif token == '?':
                if n == 0 or n > sum:
                    tokenized = None
                    break
                tokenized[i] = n

        _print(tokenized)


def _print(tokenized=None):
    if tokenized is None:
        print "Impossible"
    else:
        print "Possible"
        for t in tokenized:
            print t,
        print


#   Main parts   #
INPUT = None
if len(sys.argv) > 2:
    INPUT = sys.argv[1]

INH = fileinput.FileInput(files=INPUT)
l1 = INH.readline()
while l1:
    process(l1)
    l1 = INH.readline()

INH.close()
