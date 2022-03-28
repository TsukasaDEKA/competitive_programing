import re
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
acb"""
        output = """Yes"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """aabb
bbaa"""
        output = """No"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """abcde
abcde"""
        output = """Yes"""
        self.assertIO(input, output)

def resolve():
  S = list(input())
  T = list(input())
  if S == T:
    print("Yes")
    return

  N = len(S)
  for i in range(N-1):
    s = [x for x in S]
    s[i], s[i+1] = s[i+1], s[i]
    if s == T:
      print("Yes")
      return

  print("No")

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()