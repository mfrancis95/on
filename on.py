from argparse import ArgumentParser
import sys
import subprocess

parser = ArgumentParser("on")
parser.add_argument("-a", "--async", action = "store_true")

group = parser.add_mutually_exclusive_group()
group.add_argument("-eq", action = "store_true")
group.add_argument("-ne", action = "store_true")

parser.add_argument("value")
parser.add_argument("command", nargs = "+")
parser.add_argument("-q", action = "store_true")
args = parser.parse_args()

call = subprocess.Popen if args.async else subprocess.call
value = args.value.strip()
if args.ne:
    compare = lambda line: line.strip() != value
else:
    compare = lambda line: line.strip() == value
process = " ".join(args.command)
quit = args.q

for line in filter(compare, sys.stdin):
    call(process, shell = True)
    if quit:
        break
