"""
Day 4, part 2 - Passport Processing

https://adventofcode.com/2020/day/4

Usage: pipe your input into the script
"""

__author__ = "Francesco Mecatti"

import sys
import re

def main():
    count: int = 0
    count_valid_num_fields: int = 0
    required_fields: List[str] = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
    hcl_re = re.compile(r'^[0-9|a-f]{6}$')
    pid_re = re.compile(r'^[0-9]{9}$')
    valid_ecl: List[str] = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
    buf: str = ''
    l: List[str] = None
    d: Dict[str, str] = None
    for line in sys.stdin:
        line = line.strip()
        if line:  # If line is not blank
            buf += line + " "  # 'key: value ' -> final space
        else:
            # print(buf)
            l = re.split(r' |:', buf.strip())
            l = [ele for index, ele in enumerate(l) if index%2 == 0]
            # print(l)
            s: Set[str] = set(l) ^ set(required_fields) 
            # print(s)
            if not s or (len(s) == 1 and s.pop() == 'cid'):  # Valid NUMBER of fields
                count_valid_num_fields += 1
                l = re.split(r' |:', buf.strip())
                d = {k[0]: k[1] for i, k in enumerate(zip(l, l[1:])) if i%2 == 0}
                # print(d)
                if 1920 <= int(d[required_fields[0]]) <= 2002:
                    if 2010 <= int(d[required_fields[1]]) <= 2020:
                        if 2020 <= int(d[required_fields[2]]) <= 2030:
                            if (d[required_fields[3]][-2:] in ('cm', 'in')):
                                if (d[required_fields[3]][-2:] == 'cm' and 150 <= int(d[required_fields[3]][:-2]) <= 193) or (d[required_fields[3]][-2:] == 'in' and 59 <= int(d[required_fields[3]][:-2]) <= 76):
                                    if d[required_fields[4]][0] == '#' and hcl_re.match(d[required_fields[4]][1:]):
                                        if d[required_fields[5]] in valid_ecl:
                                            if pid_re.match(d[required_fields[6]]):
                                                count += 1
            buf = ''
    # print(count_valid_num_fields)
    print(count)

if __name__ == "__main__":
    main()
