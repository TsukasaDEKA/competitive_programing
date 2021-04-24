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
        input = """5
6 9 4 2 11"""
        output = """11 6"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """2
100 0"""
        output = """100 0"""
        self.assertIO(input, output)


def resolve():
  inf = 10**10+1
  N = int(input())
  A = [int(x) for x in input().split(" ")]
  max_A = max(A)
  half_max_A = max_A/2

  a_r = 0
  min_diff = inf
  for a in A:
    if a == max_A: continue
    if abs(half_max_A-a) < min_diff:
       min_diff = abs(half_max_A-a)
       a_r = a
  print(max_A, a_r)
resolve()

if __name__ == "__main__":
    unittest.main()
