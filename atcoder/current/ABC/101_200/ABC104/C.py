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
        input = """2 700
3 500
5 800"""
        output = """3"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """2 2000
3 500
5 800"""
        output = """7"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """2 400
3 500
5 800"""
        output = """2"""
        self.assertIO(input, output)

    def test_Sample_Input_4(self):
        input = """5 25000
20 1000
40 1000
50 1000
30 1000
1 1000"""
        output = """66"""
        self.assertIO(input, output)

def resolve():
  inf = 10**18+1
  # DP でいけそう。
  # dp[i][j] := i 番目までを選んだ時に得点が j 以上になる最小枚数。
  D, G = map(int, input().split(" "))
  G//=100

  POINTS = []
  for i in range(D):
    P, C = [int(x) for x in input().split(" ")]
    POINTS.append((P, C//100))

  dp = [[inf]*(G+1) for _ in range(D+1)]
  for i in range(D+1):
    dp[i][0] = 0

  for i in range(1, D+1):
    P, C = POINTS[i-1]
    # 問題分の得点
    for p in range(1, P+1):
      for g in range((p-1)*i+1, min(G, p*i)+1):
        dp[i][g] = min(p, dp[i-1][g])

    # ボーナス分の得点
    for g in range(P*i+1, min(G, P*i+C)+1):
      dp[i][g] = min(P, dp[i-1][g])
    
    # i 番目の問題だけでなく、~ i-1 番目までの問題を組み合わせて解いた場合の得点
    for g in range(P*i+C+1, G+1):
      dp[i][g] = min(P+dp[i-1][g-P*i-C], dp[i-1][g], inf)

  print(dp[-1][-1])

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()