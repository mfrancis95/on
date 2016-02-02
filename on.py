from argparse import ArgumentParser
from re import match
import subprocess
from itertools import filterfalse
import sys

operators = {
    "eq": lambda line: line.strip() == value,
    "ne": lambda line: line.strip() != value,
    "like": lambda line: match(value, line.strip()),
    "gt": lambda line: int(line) > value,
    "lt": lambda line: int(line) < value,
    "gte": lambda line: int(line) >= value,
    "lte": lambda line: int(line) <= value
}

parser = ArgumentParser("on")
parser.add_argument("-a", "--async", action = "store_true")
parser.add_argument("-n", "--not", action = "store_true")
parser.add_argument("operator", choices = operators.keys())
parser.add_argument("value")
parser.add_argument("command", nargs = "+")
parser.add_argument("-q", "--quit", action = "store_true")
args = vars(parser.parse_args())

call = subprocess.Popen if args["async"] else subprocess.call
filter = filterfalse if args["not"] else filter
value = args["value"].strip()
operator = args["operator"]
if operator not in ("eq", "ne", "like"):
    value = int(value)
operator = operators[operator]
process = " ".join(args["command"])
quit = args["quit"]

for line in filter(operator, sys.stdin):
    call(process, shell = True)
    if quit:
        break
