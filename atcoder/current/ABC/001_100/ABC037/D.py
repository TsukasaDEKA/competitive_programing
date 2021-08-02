import sys
from io import StringIO
import unittest

class TestClass(unittest.TestCase):
    maxDiff = None
    def assertIO(self, input, output):
        stdout, stdin = sys.stdout, sys.stdin
        sys.stdout, sys.stdin = StringIO(), StringIO(input)
        resolve()
        sys.stdout.seek(0)
        out = sys.stdout.read()[:-1]
        sys.stdout, sys.stdin = stdout, stdin
        self.assertEqual(out, output)

    def test_Sample_Input_1(self):
        input = """2 3
1 4 5
2 4 9"""
        output = """18"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """6 6
1 3 4 6 7 5
1 2 4 8 8 7
2 7 9 2 7 2
9 4 2 7 6 5
2 8 4 6 7 6
3 7 9 1 2 7"""
        output = """170"""
        self.assertIO(input, output)

def resolve():
  # 開始地点が決まってれば DFS で一発だけど、好きな升目から開始できるのが困る。
  # 升目の数は 10**6 程度まであるので O(1) で求めたい。
  H, W = map(int, input().split(" "))
  F = [[int(x) for x in input().split(" ")] for _ in range(H)]


  print()

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()