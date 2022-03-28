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
        input = """chokuou"""
        output = """YES"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """kuccho"""
        output = """NO"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """atcoder"""
        output = """NO"""
        self.assertIO(input, output)

def resolve():
  S = list(input())
  N = len(S)
  for i in range(N):
    if i < N-1:
      if S[i:i+2] == ["c", "h"]:
        S[i+1] = "o"
        continue
    if S[i] == "o" or S[i] == "k" or S[i] == "u": continue
    print("NO")
    return
  print("YES")

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()