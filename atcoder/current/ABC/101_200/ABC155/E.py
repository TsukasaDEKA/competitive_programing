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
        input = """36"""
        output = """8"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """91"""
        output = """3"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """314159265358979323846264338327950288419716939937551058209749445923078164062862089986280348253421170"""
        output = """243"""
        self.assertIO(input, output)

    def test_Sample_Input_4(self):
        input = """55"""
        output = """10"""
        self.assertIO(input, output)

    def test_Sample_Input_5(self):
        input = """65"""
        output = """9"""
        self.assertIO(input, output)

def resolve():
  inf = 10**18+1
  # DPっぽい
  # S を末尾から見ていった時に Si 枚支払ってその桁を丁度解消するか、1 枚支払って 10-Si 枚をお釣りでもらうか選べる。
  # 末尾から最適な値を選んでいけば良さそう。
  # dp[i][d] :=  i 桁目まで確定した状態で、その桁で支払う場合の枚数 (d = 0) 、上の桁で 1 枚多く支払う場合にもらうお釣りの枚数 (d = 1)
  S = [int(x) for x in list(input())][::-1]
  N = len(S)
  dp = [[0]*2 for _ in range(N)]
  dp[0][0], dp[0][1] = S[0], 10 - S[0]
  for i in range(1, N):
    # その桁で支払う場合
    dp[i][0] = min(dp[i-1][0]+S[i], dp[i-1][1]+S[i]+1)

    # 上の桁で 1 枚多く支払ってもらう場合
    dp[i][1] = min(dp[i-1][0]+(10-S[i]), dp[i-1][1]+(10-S[i])-1)

  print(min(dp[-1][0], dp[-1][1]+1))

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()