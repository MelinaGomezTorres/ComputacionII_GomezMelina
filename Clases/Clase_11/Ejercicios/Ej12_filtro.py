import argparse
import sys

parser = argparse.ArgumentParser()
parser.add_argument("--min", type=int, required=True)
args = parser.parse_args()

for line in sys.stdin:
    num = int(line.strip())
    if num > args.min:
        print(num)
