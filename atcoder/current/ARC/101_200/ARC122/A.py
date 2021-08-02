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
  # 先頭には一回も - がつかない。
  mod = 10**9+7
  N = int(input())
  A = [int(x) for x in input().split(" ")]
  dp = [[0]*2 for _ in range(N)]
  dp[0][0] = dp[0][1] = 1
  for i in range(1, N):
    dp[i][0] = (dp[i-1][0]+dp[i-1][1])%mod
    dp[i][1] = dp[i-1][0]%mod
  
  count = dp[-1][0]
  ans = count*A[0]
  for i in range(1, N):
    val = (count-2*dp[i-1][1]*dp[N-i-1][1])%mod
    ans += (val*A[i])%mod
    if ans >= mod: ans%=mod
  print(ans)


import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
    unittest.main()
