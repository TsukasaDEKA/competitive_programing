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
        input = """10 10 10
1 1 1"""
        output = """1000"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """10 3 1
2 1 1"""
        output = """15"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """5 10 3
2 5 3"""
        output = """5"""
        self.assertIO(input, output)

    def test_Sample_Input_4(self):
        input = """8 8 8
1 1 9"""
        output = """0"""
        self.assertIO(input, output)

def resolve():
  from itertools import permutations

  N = [int(x) for x in input().split(" ")]
  M = [int(x) for x in input().split(" ")]

  if max(N) < max(M) or min(N) < min(M):
    print(0)
    return
  ans = 0
  # 対応する辺を決めて全探索。
  for tar in permutations(range(3), 3):
    temp = 1
    for i in range(3):
      temp *= N[i]//M[tar[i]]
    ans = max(ans, temp)
  print(ans)

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()