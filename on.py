from argparse import ArgumentParser
import sys
import subprocess

parser = ArgumentParser("on")
parser.add_argument("-a", "--async", action = "store_true")
parser.add_argument("operator", choices = ["eq", "ne", "gt", "lt", "gte", "lte"])

parser.add_argument("value")
parser.add_argument("command", nargs = "+")
parser.add_argument("-q", action = "store_true")
args = parser.parse_args()

operators = {
    "eq": lambda line: line.strip() == value,
    "ne": lambda line: line.strip() != value,
    "gt": lambda line: int(line) > value,
    "lt": lambda line: int(line) < value,
    "gte": lambda line: int(line) >= value,
    "lte": lambda line: int(line) <= value
}

call = subprocess.Popen if args.async else subprocess.call
value = args.value.strip()
operator = args.operator
if operator not in ("eq", "ne"):
    value = int(value)
operator = operators[operator]
process = " ".join(args.command)
quit = args.q

for line in filter(operator, sys.stdin):
    call(process, shell = True)
    if quit:
        break
