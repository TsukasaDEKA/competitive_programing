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
        input = """4 330
0 1 10 100
1 0 20 200
10 20 0 300
100 200 300 0"""
        output = """2"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """5 5
0 1 1 1 1
1 0 1 1 1
1 1 0 1 1
1 1 1 0 1
1 1 1 1 0"""
        output = """24"""
        self.assertIO(input, output)

def resolve():
  # 全探索
  from itertools import permutations
  inf = 10**18

  N, K = map(int, input().split(" "))
  T = [[int(x) for x in input().split(" ")] for _ in range(N)]
  count = 0
  for nexts in permutations(range(1, N), N-1):
    k = 0
    current = 0
    for n in nexts:
      k+=T[current][n]
      current = n
    k+=T[current][0]
    if k==K: count+=1

  print(count)

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()