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
        input = """AtCoder"""
        output = """Yes"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """Aa"""
        output = """Yes"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """atcoder"""
        output = """No"""
        self.assertIO(input, output)

    def test_Sample_Input_4(self):
        input = """Perfect"""
        output = """No"""
        self.assertIO(input, output)

def resolve():
  alpha2num = lambda c: ord(c) - ord('a')

  from collections import defaultdict

  inf = 10**18+1
  S = list(input())
  N = len(S)
  big = 0
  small = 0
  count = defaultdict(int)
  for i in range(N):
    count[S[i]] += 1
    if count[S[i]] > 1:
      print("No")
      return
    if S[i] <= "Z":
      big += 1
    else:
      small += 1

  print("Yes" if big >= 1 and small >= 1 else "No")


import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()