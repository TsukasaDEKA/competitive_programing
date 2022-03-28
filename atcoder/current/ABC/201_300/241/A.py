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
        input = """9 0 1 2 3 4 5 6 7 8"""
        output = """7"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """4 8 8 8 0 8 8 8 8 8"""
        output = """4"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """0 0 0 0 0 0 0 0 0 0"""
        output = """0"""
        self.assertIO(input, output)

def resolve():
  inf = 10**18+1
  A = [int(x) for x in input().split(" ")]
  ans = 0
  for i in range(3):
    ans = A[ans]
  print(ans)

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()