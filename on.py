import sys
from subprocess import call

if len(sys.argv) >= 3:
    value = sys.argv[1]
    process = " ".join(sys.argv[2:])
    for line in sys.stdin:
        if line.rstrip() == value:
            call(process, shell = True)
