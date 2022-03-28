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
3 4 6"""
        output = """10"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """5
7 46 11 20 11"""
        output = """90"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """7
994 518 941 851 647 2 581"""
        output = """4527"""
        self.assertIO(input, output)

def resolve():
  N = int(input())
  A = sorted([int(x) for x in input().split(" ")])

  ans = 0
  for i in range(N):
    ans += A[i] - 1
  print(ans)

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()