import numpy as np
import PIL
import sys


class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items)-1]

    def size(self):
        return len(self.items)


def dec2bin(n: int) -> list:
    remstack = Stack()
    result = []

    while n > 0:
        remstack.push(n % 2)
        n //= 2

    while remstack.size() > 0:
        result.append(remstack.pop())

    return result


binstr = lambda n: format(n, 'b')

binlist = lambda n: list(format(n, 'b'))

binint = lambda n: int(binstr(n))

bin3 = lambda n: format(n, '03b')
bin8 = lambda n: format(n, '08b')

# binn
i2nb = lambda n, x: format(x f'0{int(n)}')
b2i = lambda n: int(n, 2)

patterns = tuple(i2nb(3,x) for x in range(8))
def pattern(pat: str) -> int:
    pats = tuple(i2nb(3,x) for x in range(8))

class Rule:
    def __init__(self, wcode: int):
        self.wolf_code = wcode

def cell_check(cell, row)
def apply_rule(row: list, rule: int) -> list:
    pat = [0, 0, 0]
    for x in range(len(row)):
        if x == 0:
            pat[0] = 0, pat[1] = row[x]


if __name__ == '__main__':
    inn = int(sys.argv[1])
    print(f"decimal: {inn}")
    out = dec2bin(inn)
    outs = ''
    for x in out:
        outs = outs + str(x)
    print(f"binary: {outs}")
