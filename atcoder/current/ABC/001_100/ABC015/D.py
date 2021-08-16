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
        input = """10
3 2
4 20
3 40
6 100"""
        output = """140"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """10
5 4
9 10
3 7
3 1
2 6
4 5"""
        output = """18"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """22
5 3
5 40
8 50
3 60
4 70
6 80"""
        output = """210"""
        self.assertIO(input, output)

def resolve():
  # 部分和の最大化問題。
  # ナップザック問題系
  # dp[i][w] := i 番目までの画像の中で w 以下になる組み合わせを選んだ時の価値の最大値
  # K 枚って制約を忘れてた。どうすんだこれ。
  # dp[i][w][k] := i 番目までの画像の中で w 以下になる組み合わせを k 枚まで選んだ時の価値の最大値で間に合うか・・・？間に合いそう。
 
  inf = 10**18+1
  W = int(input())
  N, K = map(int, input().split(" "))
  IMAGES = [[int(x) for x in input().split(" ")] for _ in range(N)]
 
  dp = [[0]*(K+1) for _ in range(W+1)]
 
  a, b = IMAGES[0]
  for w in range(a, W+1):
    dp[w][1] = b
 
  for i in range(1, N):
    a, b = IMAGES[i]
    for w in reversed(range(a, W+1)):
      dp_w = dp[w]
      dp_w_a = dp[w-a]
      for k in range(1, min(i+1, K)+1):
        if dp_w[k] < dp_w_a[k-1]+b: dp_w[k] = dp_w_a[k-1]+b

  print(max(dp[-1]))

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()