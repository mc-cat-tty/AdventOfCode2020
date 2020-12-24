"""
Day 7, part 2 - Handy Haversacks

https://adventofcode.com/2020/day/7

Usage: pipe your input into the script
"""

__author__ = "Francesco Mecatti"

import sys
import re
from typing import Dict, List

class Rule:
    def __init__(self, num: int, desc: str) -> None:
        self.desc: str = desc
        self.num: int = num

def walk_dict(d: Dict[str, List[str]], starting_key: str) -> int:
    if not d.get(starting_key):
        return 0
    counter: int = 0
    for rule in d[starting_key]:
        counter += rule.num
        counter += walk_dict(d, rule.desc) * rule.num
    return counter

def main():
    line_pattern = re.compile(r'(.+?) bags contain (.+)')
    rules: Dict[str, List[str]] = dict()
    for line in sys.stdin:
        line = line.strip()
        if not line:  # Blank line
            continue
        parsed_line: Tuple[str] = line_pattern.match(line).groups()
        # print(parsed_line)
        container_color: str = parsed_line[0]
        contained: str = parsed_line[1]
        if contained != 'no other bags.':
            rules[container_color] = list()
            contained_bags: List[str] = contained.split(',')
            contained_bags = list(map(lambda x: x.strip(' \n.'), contained_bags))
            for bag in contained_bags:
                bag = bag.rpartition(' ')[0]
                n: int = int(bag.partition(' ')[0])
                color: str = bag.partition(' ')[2]
                rules[container_color].append(Rule(n, color))
    print(walk_dict(rules, 'shiny gold'))

if __name__ == "__main__":
    main()
