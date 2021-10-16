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
        input = """3 7
1 6 3"""
        output = """14"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """4 9
7 4 0 3"""
        output = """46"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """1 0
1000000000000"""
        output = """1000000000000"""
        self.assertIO(input, output)

def resolve():
  inf = 10**18+1
  # bit にして全部の桁を上位桁から見ていって、0 と 1 のどちらが多いか確認する。
  # 多い方の数字を反転して仮置きする。
  # もしその桁を仮置きした時に、その数字が K より大きかったら 0 に、小さかったらそのまま採用する。
  # それを繰り返していって X を求める。
  # その X と全ての A を使って答えを求める。
  N, K = map(int, input().split(" "))
  A = [int(x) for x in input().split(" ")]
  X = 0
  for b in reversed(range(40)):
    count1 = len(["" for a in A if a&(1<<b)])
    if 2*count1 < N and X+(1<<b) <= K: X += 1<<b

  ans = 0
  for a in A:
    ans += a^X

  print(ans)

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()