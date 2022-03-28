from collections import defaultdict
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
        input = """2
3 1
1 2"""
        output = """2"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """2
1 1
2 2"""
        output = """0"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """20
1937 3980 2689 1208 3640 1979 581 2271 4229 3948 3708 1522 4161 4661 3797 96 3388 3395 2920 2247
4485 2580 174 1156 3770 3396 3558 3500 3494 479 269 3383 1230 1711 3545 3919 134 475 3796 1017"""
        output = """476"""
        self.assertIO(input, output)


def resolve():
  mod = 998244353
  # A を昇順に並び替えて、左から取っていく。
  # 今までのインデックスを覚えておく。
  # A1 を取る時、B1 の組み合わせは 1 パターンで、合計値も 1 パターン
  # A2 を取る時、B2 は必ず取らなければいけない。新しい B を足して A2 を超えない組み合わせは二分探索で求められる。
  # A に同値が含まれていた場合は・・・問題ない？

  N = int(input())
  A = [int(x) for x in input().split(" ")]
  sortedA = sorted([(x, i) for i, x in enumerate(A)])
  maxA = max(A)
  B = [int(x) for x in input().split(" ")]
  B = [B[i] for _, i in sortedA]

  ans = 0
  table = [0]*(maxA+1)
  table[0] = 1
  for i in range(N):
    (a, _), b = sortedA[i], B[i]
    if a-b >= 0: ans += sum(table[:a-b+1])
    if ans >= mod: ans%=mod

    for j in reversed(range(maxA-b+1)):
      table[j+b] += table[j]
      if table[j+b] >= mod: table[j+b]%=mod

  print(ans)


import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()