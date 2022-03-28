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
        input = """5
4 4 9 7 5"""
        output = """5"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """6
4 5 4 3 3 5"""
        output = """8"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """10
9 4 6 1 9 6 10 6 6 8"""
        output = """39"""
        self.assertIO(input, output)

    def test_Sample_Input_4(self):
        input = """2
1 1"""
        output = """0"""
        self.assertIO(input, output)

def resolve():
  N = int(input())
  L = sorted([int(x) for x in input().split(" ")])
  count = 0
  for i in range(N-2):
    for j in range(i+1, N-1):
      for k in range(j+1, N):
        if L[i] == L[j] or L[j]==L[k]: continue
        if L[i]+L[j] <= L[k]: continue
        count+=1
  print(count)

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()