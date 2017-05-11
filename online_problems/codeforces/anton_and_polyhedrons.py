import sys
import fileinput
# http://codeforces.com/contest/785/problem/A
SIDES = {
    "Tetrahedron": 4,
    "Cube": 6,
    "Octahedron": 8,
    "Dodecahedron": 12,
    "Icosahedron": 20
}


def process(n):
    global INH
    global SIDES
    faces = 0
    n = int(n)
    for i in range(0, n):
        faces += SIDES[INH.readline().rstrip()]
    _print(faces)


def _print(faces):
    print faces


##################
#   Main parts   #
##################
INPUT = None
if len(sys.argv) > 2:
    INPUT = sys.argv[1]

INH = fileinput.FileInput(files=INPUT)
l1 = INH.readline()
while l1:
    process(l1)
    l1 = INH.readline()

INH.close()
