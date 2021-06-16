import sys
from io import StringIO
from typing import Pattern
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
3 1 5"""
        output = """15"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """4
1 1 1 1"""
        output = """10"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """10
866111664 178537096 844917655 218662351 383133839 231371336 353498483 865935868 472381277 579910117"""
        output = """279919144"""
        self.assertIO(input, output)


def resolve():
  # 各要素に何回 - を付けられるかを考える。
  # 先頭は正で固定。
  mod = 10**9+7
  N = int(input())
  A = [int(x) for x in input().split(" ")]
  dp = [[0]*2 for _ in range(N)]
  # dp[i][j] := 長さ i の配列があって、i 番目の数字の符号を正にするか負にするかの場合数 (j == 0 の時が正、j == 1 が負)
  # 先頭は正で固定なので、dp[0] = [1, 0]
  dp[0][0] = 1
  for i in range(1, N):
    # i-1 番目の符号が正負のどちらでも、 i 番目の符号を正にすることができる。
    dp[i][0] = (dp[i-1][0]+dp[i-1][1])%mod
    # i-1 番目の符号が負の場合、i 番目の符号を負にすることはできない。
    dp[i][1] = dp[i-1][0]%mod
  
  # count : 良い式の総数。
  count = sum(dp[-1])
  # 先頭は符号が負になることはないので 良い式の総数 * A[0] から始める。
  ans = count*A[0]
  for i in range(1, N):
    # i 番目の数字の符号が負になる場合数は
    # <前から符号を決めていって i 番目の数字の符号が負になる場合数> * < i 番目以降の数字の符号を決めていった時の場合数> になる。
    # 前から符号を決めていって i 番目の数字の符号が負になる場合数は dp[i][1]。
    # i 番目以降の数字の符号を決めていった時の場合数は i 番目の符号が負であることを勘案すると、
    # i+1 番目の数字の符号は負にならないため、先頭が正で固定されている状態だと見なすことができる。
    # これは A[i+1:N] のを逆順に見た時に最後の数字の符号が正である場合数 dp[N-i-1][0] と同じになる。
    # つまり、i 番目の数字の符号が負になる場合数 = dp[i][1]*dp[N-i-1][0]
    mul = (count-2*dp[i][1]*dp[N-i-1][0])%mod
    ans += (mul*A[i])%mod
    if ans >= mod: ans%=mod
  print(ans)

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
    unittest.main()
