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
        input = """4
2 4 4 3"""
        output = """4
3
3
4"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """2
1 2"""
        output = """2
1"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """6
5 5 4 4 3 3"""
        output = """4
4
4
4
4
4"""
        self.assertIO(input, output)

def resolve():
  # N は偶数
  N = int(input())
  X = [int(x) for x in input().split(" ")]
  sortedX = sorted(X)
  base = sortedX[N//2-1]
  for i in range(N):
    if X[i] <= base:
      print(sortedX[N//2])
      continue
    print(sortedX[N//2-1])

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()