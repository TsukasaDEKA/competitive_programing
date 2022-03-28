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
        input = """998244353"""
        output = """143"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """1000000007"""
        output = """49483"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """1"""
        output = """1"""
        self.assertIO(input, output)

    def test_Sample_Input_4(self):
        input = """998984374864432412"""
        output = """2003450165"""
        self.assertIO(input, output)

def resolve():
  inf = 10**18+1
  N = int(input())
  ans = inf
  # b で全探索
  for b in range(60):
    b_ = pow(2, b)
    a = N//b_
    c = N-a*b_
    ans = min(ans, a+b+c)

  print(ans)

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
    unittest.main()
