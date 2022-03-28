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
        input = """abc
ijk"""
        output = """Yes"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """z
a"""
        output = """Yes"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """ppq
qqp"""
        output = """No"""
        self.assertIO(input, output)

    def test_Sample_Input_4(self):
        input = """atcoder
atcoder"""
        output = """Yes"""
        self.assertIO(input, output)

def resolve():
  alpha2num = lambda c: ord(c) - ord('a')

  inf = 10**18+1
  S = [alpha2num(s) for s in list(input())]
  T = [alpha2num(s) for s in list(input())]

  N = len(S)
  diff = (T[0]-S[0])%26
  for i in range(N):
    if (T[i]-S[i])%26 != diff:
      print("No")
      return

  print("Yes")

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()