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
        input = """2
2
3"""
        output = """6"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """5
2
5
10
1000000000000000000
1000000000000000000"""
        output = """1000000000000000000"""
        self.assertIO(input, output)

def resolve():
  from math import gcd
  from functools import reduce
  def lcm_base(x, y):
    return (x * y) // gcd(x, y)
  # T1 ~ TN の最小公倍数が答え。
  # Python の gcd で間に合うか微妙だけどやってみる。
  N = int(input())
  ans = 1
  for _ in range(N):
    ans = lcm_base(ans, int(input()))
  print(ans)

resolve()

if __name__ == "__main__":
    unittest.main()
