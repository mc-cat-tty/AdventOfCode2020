"""
Day 8, part 2 - Handheld Halting

https://adventofcode.com/2020/day/8

Usage: pipe your input into the script
"""

__author__ = "Francesco Mecatti"

import sys

class Instruction:
    def __init__(self, op: str, val: int):
        self.op: str = op
        self.val: int = val

def main():
    accumulator: int = 0
    instructions: List[Instruction] = list()
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        op: str = line.split(' ')[0]
        val: int = int(line.split(' ')[1])
        instructions.append(Instruction(op, val))

    i: int = 0
    exec_n: List[int] = [0] * len(instructions)
    while True:
        exec_n[i] += 1
        if exec_n[i] > 1:
            for index in range(len(instructions)-1, 0, -1):
                if exec_n[index] > 0:
                    i = index
                    print(i)
                    break
            if instructions[i].op == 'nop':
                instructions[i].op = 'jmp'
            elif instructions[i].op == 'jmp':
                instructions[i].op = 'nop'
            break

        if instructions[i].op == 'jmp':
            i += instructions[i].val - 1
        i += 1

    i = 0
    while i < len(instructions):
        if instructions[i].op == 'acc':
            accumulator += instructions[i].val
        if instructions[i].op == 'jmp':
            i += instructions[i].val - 1
        i += 1

    print(accumulator)
        

if __name__ == "__main__":
    main()
