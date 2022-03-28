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

    # def test_Sample_Input_1(self):
    #     input = """36"""
    #     output = """8"""
    #     self.assertIO(input, output)

    # def test_Sample_Input_2(self):
    #     input = """91"""
    #     output = """3"""
    #     self.assertIO(input, output)

    # def test_Sample_Input_3(self):
    #     input = """314159265358979323846264338327950288419716939937551058209749445923078164062862089986280348253421170"""
    #     output = """243"""
    #     self.assertIO(input, output)

    # def test_Sample_Input_4(self):
    #     input = """55"""
    #     output = """10"""
    #     self.assertIO(input, output)

    def test_Sample_Input_5(self):
        input = """65"""
        output = """9"""
        self.assertIO(input, output)

def resolve():
  inf = 10**18+1
  # DPっぽい
  # S を末尾から見ていった時に Si 枚支払ってその桁を丁度解消するか、1 枚支払って 10-Si 枚をお釣りでもらうか選べる。
  # 末尾から最適な値を選んでいけば良さそう。
  # Si が 4 以下の場合、支払う金額のその桁を Si にしてやることで枚数が少なくなる。
  # Si が 6 以上の場合、お釣りをもらった方が良い。
  # Si が 5 の場合が問題。S = 5 の場合、10 支払うよりも 5 支払った方が枚数が少ない。
  # S = 55 の場合、55 支払う時 (10 枚支払いでお釣り 0 枚) と 100 支払う(1 枚支払いでお釣り 9 枚)ときで枚数の合計が同じになる。
  # S = 65 の場合、105 支払うと 6 枚支払いでお釣り 4 枚で合計 10 枚。 100 支払うと 1 枚支払いでお釣りが 3+5 で合計 9 枚。
  # S = 45 の場合、50 支払うと 5 枚支払いでお釣り 5 枚で合計 10 枚。45 支払うと 9 枚支払いでお釣りが 0 枚で合計 9 枚
  # Si が 5 の時、その左側が 4 以下ならお釣りをもらう (0 にする) 方がいいし、そうでないなら 5 を払ってしまった方が良い。
  S = [0]+[int(x) for x in list(input())]
  N = len(S)
  dp = [[0]*2 for _ in range(N)]
  dp[0][0], dp[0][1] = 0, 1
  for i in range(1, N):
    dp[i][0] = min(dp[i-1][0]+S[i], dp[i-1][1]+(10-S[i]))
    dp[i][1] = min(dp[i-1][0]+S[i], dp[i-1][1]+(10-S[i]))

  print(*dp)

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()