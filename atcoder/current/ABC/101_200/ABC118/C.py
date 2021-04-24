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
        input = """4
2 10 8 40"""
        output = """2"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """4
5 13 8 1000000000"""
        output = """1"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """3
1000000000 1000000000 1000000000"""
        output = """1000000000"""
        self.assertIO(input, output)

def resolve():
  # なんとなく最大公約数っぽい
  # 余が
  N = int(input())
  A = [int(x) for x in input().split(" ")]
  from math import gcd

  ans = A[0]
  for a in A[1:]:
    ans = gcd(ans, a)
  print(ans)

resolve()

if __name__ == "__main__":
    unittest.main()
