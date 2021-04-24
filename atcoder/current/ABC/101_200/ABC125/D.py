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
-10 5 -4"""
        output = """19"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """5
10 -4 -8 -11 3"""
        output = """30"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """11
-1000000000 1000000000 -1000000000 1000000000 -1000000000 0 1000000000 -1000000000 1000000000 -1000000000 1000000000"""
        output = """10000000000"""
        self.assertIO(input, output)

    def test_Sample_Input_4(self):
        input = """22
-1000000000 1000000000 -1000000000 1000000000 -1000000000 0 1000000000 -1000000000 1000000000 -1000000000 1000000000 -1000000000 1000000000 -1000000000 1000000000 -1000000000 0 1000000000 -1000000000 1000000000 -1000000000 1000000000"""
        output = """0"""
        self.assertIO(input, output)

def resolve():
  inf = 10**10+1
  N = int(input())
  A = [int(x) for x in input().split(" ")]
  # 0 が含まれている場合、全てを正にできる。
  # 含まれていない場合、任意の偶数個の Ai を正にできる
  # 負の値が奇数個の時、絶対値が最小の Ai を負にすることで最大値が出せる。
  # N == 2 の場合、大きい方を正、小さい方を負にすることで最大値を出せる。
  zero_found = False
  minimam_abs_a = inf
  include_even_negative = True
  sum_abs_a = 0
  for a in A:
    abs_a = abs(a)
    sum_abs_a += abs_a
    minimam_abs_a = min(minimam_abs_a, abs_a)
    if a == 0: zero_found=True
    # 負の値が偶数個含まれているか
    if a < 0: include_even_negative = not include_even_negative
  
  if not zero_found and not include_even_negative:
    sum_abs_a -= 2*minimam_abs_a
  print(sum_abs_a)
  
resolve()

if __name__ == "__main__":
    unittest.main()
