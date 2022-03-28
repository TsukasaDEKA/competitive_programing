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
        input = """3
abc"""
        output = """1"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """6
abcabc"""
        output = """-1"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """7
atcoder"""
        output = """-1"""
        self.assertIO(input, output)

    def test_Sample_Input_4(self):
        input = """19
bcabcabcabcabcabcab"""
        output = """9"""
        self.assertIO(input, output)

def resolve():
  N = int(input())
  S = list(input())
  if N%2==0:
    print(-1)
    return

  center = N//2
  for i in range(N//2+1):
    if i == 0:
      if S[center] != "b":
        print(-1)
        return
      continue

    l = center-i
    r = center+i
    if i%3 == 0 and (S[l] != "b" or S[r] != "b"):
      print(-1)
      return
    if i%3 == 1 and (S[l] != "a" or S[r] != "c"):
      print(-1)
      return
    if i%3 == 2 and (S[l] != "c" or S[r] != "a"):
      print(-1)
      return

  print(N//2)

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()