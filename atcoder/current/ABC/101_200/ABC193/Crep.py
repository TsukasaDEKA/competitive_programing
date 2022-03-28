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
        input = """8"""
        output = """6"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """100000"""
        output = """99634"""
        self.assertIO(input, output)

def resolve():
  N = int(input())
  ans = N
  used = set()
  for n in range(2, int(-(-N**0.5//1))+1):
    v = n*n
    while v <= N:
      if v not in used:
        ans-=1
        used.add(v)
      v*=n
  print(ans)

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()