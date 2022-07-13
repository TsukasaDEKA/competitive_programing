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
        input = """ATCODER"""
        output = """3"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """HATAGAYA"""
        output = """5"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """SHINJUKU"""
        output = """0"""
        self.assertIO(input, output)

def resolve():
  AGCT = set(list("AGCT"))
  S = list(input()) + ["E"]
  N = len(S)
  ans = 0
  count = 0
  for i in range(N):
    if S[i] in AGCT:
      count += 1
    else:
      ans = max(ans, count)
      count = 0
  print(ans)

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()