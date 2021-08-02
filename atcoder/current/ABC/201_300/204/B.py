import sys
from io import StringIO
import unittest


class TestClass(unittest.TestCase):
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
6 17 28"""
        output = """25"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """4
8 9 10 11"""
        output = """1"""
        self.assertIO(input, output)

def resolve():
  inf = 10**18+1
  N = int(input())
  A = [int(x) for x in input().split(" ")]
  ans = 0

  for a in A:
    if a > 10: ans+=(a-10)
  print(ans)

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
    unittest.main()
