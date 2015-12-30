from argparse import ArgumentParser
import sys
from subprocess import call

parser = ArgumentParser("on")
parser.add_argument("value")
parser.add_argument("command", nargs = "+")
args = parser.parse_args()

value = args.value
process = " ".join(args.command)
for line in sys.stdin:
    if line.rstrip() == value:
        call(process, shell = True)
