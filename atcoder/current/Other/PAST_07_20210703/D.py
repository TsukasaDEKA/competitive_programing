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
        input = """9
ixixixixi"""
        output = """...x...xi"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """6
auxuxa"""
        output = """a...xa"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """15
gxgaxixuxexoxxx"""
        output = """gxgaxixuxexoxxx"""
        self.assertIO(input, output)


def resolve():
  inf = 10**18+1
  N = int(input())
  S = list(input())

  pattarn = set(["axa", "ixi", "uxu", "exe", "oxo"])
  i = 0
  while i < N-2:
    if "".join(S[i:i+3]) in pattarn:
      for j in range(i, i+3):
        S[j] = "."
      i+=2
    i+=1
  print("".join(S))

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()