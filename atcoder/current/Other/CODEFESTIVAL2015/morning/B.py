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

    def test_入力例1(self):
        input = """8
abacbabc"""
        output = """2"""
        self.assertIO(input, output)

    def test_入力例2(self):
        input = """8
abababab"""
        output = """0"""
        self.assertIO(input, output)

    def test_入力例3(self):
        input = """5
abcde"""
        output = """5"""
        self.assertIO(input, output)

    def test_入力例4(self):
        input = """26
codefestivaltwozeroonefive"""
        output = """14"""
        self.assertIO(input, output)

def resolve():
  inf = 100+1
  # N <= 100 なので、i を 0 ~ N の間で動かして、S[:i]とS[i:]で LCS をやる。
  # 計算量はざっくり見積もりで 250 * 100 回以下なので間に合うはず。
  # 長さ 0 でも平方になることに注意する。
  N = int(input())
  S = list(input())

  # 繰り返しメモリ確保すると遅いので配列を使い回す。
  dp = [[0]*(N+1) for _ in range(N+1)]
  ans = inf

  for n in range(N):
    left = S[:n]
    right = S[n:]
    for i in range(len(left)+1):
      for j in range(len(right)+1):
        if i==0 or j==0:
          # i==0 or j==0 の時の答えは自明
          dp[i][j] = max(i, j)
          continue
          
        if left[i-1]==right[j-1]:
          # ここまで見ていった時に末尾が一致していたら、両末尾を取り除く必要は無いので、dp[i-1][j-1]になる。
          dp[i][j] = dp[i-1][j-1]
        else:
          # どっちかの末尾を除外。
          dp[i][j] = min(dp[i-1][j]+1, dp[i][j-1]+1)
    ans = min(ans, dp[len(left)][len(right)])
  print(ans)

# resolve()

if __name__ == "__main__":
    unittest.main()
