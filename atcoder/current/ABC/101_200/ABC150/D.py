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
        input = """2 50
6 10"""
        output = """2"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """3 100
14 22 40"""
        output = """0"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """5 1000000000
6 6 2 6 2"""
        output = """166666667"""
        self.assertIO(input, output)

def resolve():
  from collections import defaultdict
  from math import gcd
  from functools import reduce
  def lcm_base(x, y):
    return (x * y) // gcd(x, y)

  def lcm(*numbers):
    return reduce(lcm_base, numbers, 1)

  N, M = map(int, input().split(" "))
  A = sorted([int(x)//2 for x in input().split(" ")])
  agg = set()

  # 含まれる 2 の個数がバラバラである時、半公倍数は存在しない。
  for a in A:
    count = 0
    while a%2==0:
      count+=1
      a//=2
    agg.add(count)
    if len(agg) >= 2:
      print("0")
      return

  # 最小公倍数を求めて、M をそれで割る
  g = lcm(*A)
  ans = ((M//g)+1)//2
  print(ans)

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()