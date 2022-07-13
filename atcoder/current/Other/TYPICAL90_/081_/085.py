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
        input = """42"""
        output = """5"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """7"""
        output = """1"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """192"""
        output = """16"""
        self.assertIO(input, output)

    def test_Sample_Input_4(self):
        input = """7420738100000"""
        output = """16"""
        self.assertIO(input, output)

def resolve():
  # 一見愚直にやると間に合わないように見えるけど、
  # a は 1 ~ sqrt(N) の範囲、b は a ~ sqrt(N//a) の範囲でしか動かない。
  # c = N//(a*b) となるので、それが b 以上かどうかチェックすれば良い。
  N = int(input())

  ans = 0
  max_a = int(-(-(N**(1/3))//1))
  for a in range(1, max_a+1):
    if N%a != 0: continue
    temp_a = N//a
    max_b = int(-(-temp_a**0.5//1))
    for b in range(a, max_b+1):
      if (temp_a)%b != 0: continue
      c = temp_a//b
      if c >= b:
        ans += 1
  print(ans)

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()