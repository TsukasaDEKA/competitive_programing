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
        input = """5 5
1
2
3
4
5"""
        output = """1 2 3 5 4"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """7 7
7
7
7
7
7
7
7"""
        output = """1 2 3 4 5 7 6"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """10 6
1
5
2
9
6
6"""
        output = """1 2 3 4 5 7 6 8 10 9"""
        self.assertIO(input, output)

def resolve():
  from collections import defaultdict

  N, Q = map(int, input().split(" "))
  balles = [x for x in range(N)]
  to_i = defaultdict(int)
  for i in range(N):
    to_i[i] = i

  for _ in range(Q):
    X = int(input())-1
    index = min(N-2, to_i[X])
    left, right = balles[index], balles[index+1]
    to_i[left], to_i[right] = index+1, index
    balles[index], balles[index+1] = right, left

  print(*[x+1 for x in balles], sep=" ")

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()