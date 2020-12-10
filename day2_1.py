"""
Day 1, part 1 - Report Repair

https://adventofcode.com/2020/day/1

Usage: pipe your input into the script
"""

__author__ = "Francesco Mecatti"

import re, sys

count = 0

for ele in sys.stdin:
    print(ele)
    r = re.match("(\d+)-(\d+) (\w): (\w+)", ele).groups()
    Nmin = r[0]
    Nmax = r[1]
    L = r[2]
    W = r[3]
    if W.count(L) >= int(Nmin) and W.count(L) <= int(Nmax):
            count += 1

print(count)
