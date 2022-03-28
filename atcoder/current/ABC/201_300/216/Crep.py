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
        input = """5"""
        output = """AABA"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """14"""
        output = """BBABBAAAB"""
        self.assertIO(input, output)

def resolve():
  inf = 10**18+1
  N = int(input())
  ans = []
  while N > 0:
    if N%2:
      ans.append("A")
      N-=1
    else:
      ans.append("B")
      N//=2
  ans = ans[::-1]
  print("".join(ans))

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()