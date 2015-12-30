from argparse import ArgumentParser
import sys
from subprocess import call

parser = ArgumentParser("on")

group = parser.add_mutually_exclusive_group()
group.add_argument("-eq", action = "store_true")
group.add_argument("-ne", action = "store_true")

parser.add_argument("value")
parser.add_argument("command", nargs = "+")
args = parser.parse_args()

value = args.value
if args.ne:
    compare = lambda line: line != value
else:
    compare = lambda line: line == value
process = " ".join(args.command)

for line in sys.stdin:
    if compare(line.rstrip()):
        call(process, shell = True)
