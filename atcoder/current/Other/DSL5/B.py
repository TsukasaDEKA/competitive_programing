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
        input = """2
0 0 3 2
2 1 4 3"""
        output = """2"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """2
0 0 2 2
2 0 4 2"""
        output = """1"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """3
0 0 2 2
0 0 2 2
0 0 2 2"""
        output = """3"""
        self.assertIO(input, output)

import numpy as np

def resolve():
  # 多分 imos 的な解き方
  N = int(input())
  max_val = 1001
  table = np.array([[0]*(max_val+1) for _ in range(max_val+1)])
  for _ in range(N):
    x1, y1, x2, y2 = [int(x)+1 for x in input().split(" ")]
    table[x1][y1]+=1
    table[x2][y1]-=1
    table[x1][y2]-=1
    table[x2][y2]+=1

  # 積分する。
  ans = 0
  for i in range(1, max_val):
    for j in range(1, max_val):
      table[i][j] += table[i][j-1] + table[i-1][j] - table[i-1][j-1]
      ans = max(ans, table[i][j])
    if ans==N: break
  print(ans)

resolve()

if __name__ == "__main__":
  unittest.main()