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
        input = """BBBWW"""
        output = """1"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """WWWWWW"""
        output = """0"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """WBWBWBWBWB"""
        output = """9"""
        self.assertIO(input, output)

def resolve():
  S = list(input())
  N = len(S)
  ans = 0
  for i in range(N-1):
    if S[i] == "B" and S[i+1] == "W": ans+=1
    if S[i] == "W" and S[i+1] == "B": ans+=1

  print(ans)

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()