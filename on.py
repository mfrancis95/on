from argparse import ArgumentParser
import sys
import subprocess

parser = ArgumentParser("on")
parser.add_argument("-a", action = "store_true")

group = parser.add_mutually_exclusive_group()
group.add_argument("-eq", action = "store_true")
group.add_argument("-ne", action = "store_true")

parser.add_argument("value")
parser.add_argument("command", nargs = "+")
args = parser.parse_args()

call = subprocess.Popen if args.a else subprocess.call
value = args.value.strip()
if args.ne:
    compare = lambda line: line.strip() != value
else:
    compare = lambda line: line.strip() == value
process = " ".join(args.command)

for line in filter(compare, sys.stdin):
    call(process, shell = True)
