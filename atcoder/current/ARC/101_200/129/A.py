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
        input = """2 1 2"""
        output = """1"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """10 2 19"""
        output = """10"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """1000000000000000000 1 1000000000000000000"""
        output = """847078495393153025"""
        self.assertIO(input, output)

def resolve():
  N, L, R = map(int, input().split(" "))
  len_N = N.bit_length()
  len_R = R.bit_length()
  ans = 0
  for b in reversed(range(len_N)):
    # b 桁目を 1 で固定した時に条件を満たすか判定する。
    if N&(1<<b):
      # L, R の範囲に含まれる個数を求める。
      max_ = min((1<<(b+1))-1, R)
      min_ = max((1<<(b)), L)
      # print(bin(1<<b), max_, min_)
      ans += max(max_-min_+1, 0)
  print(ans)


import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()