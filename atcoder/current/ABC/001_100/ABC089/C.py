import sys
from io import StringIO
import unittest


class TestClass(unittest.TestCase):
    def assertIO(self, input, output):
        stdout, stdin = sys.stdout, sys.stdin
        sys.stdout, sys.stdin = StringIO(), StringIO(input)
        resolve()
        sys.stdout.seek(0)
        out = sys.stdout.read()[:-1]
        sys.stdout, sys.stdin = stdout, stdin
        self.assertEqual(out, output)

    def test_入力例_1(self):
        input = """5
MASHIKE
RUMOI
OBIRA
HABORO
HOROKANAI"""
        output = """2"""
        self.assertIO(input, output)

    def test_入力例_2(self):
        input = """4
ZZ
ZZZ
Z
ZZZZZZZZZZ"""
        output = """0"""
        self.assertIO(input, output)

    def test_入力例_3(self):
        input = """5
CHOKUDAI
RNG
MAKOTO
AOKI
RINGO"""
        output = """7"""
        self.assertIO(input, output)

def resolve():
from itertools import combinations
from collections import Counter
d=Counter([list(input())[0] for _ in range(int(input()))])
print(sum([d[a]*d[b]*d[c] for a, b, c in combinations(list("MARCH"), 3)]))

# resolve()

if __name__ == "__main__":
    unittest.main()
