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
        input = """3 2
acp
ae"""
        output = """6"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """6 3
abbdcf
abc"""
        output = """-1"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """15 9
dnsusrayukuaiia
dujrunuma"""
        output = """45"""
        self.assertIO(input, output)

def resolve():
  from math import gcd
  # X の長さは最小公倍数
  N, M = map(int, input().split(" "))
  S = list(input())
  T = list(input())

  # X 上の文字で、S, T のどちらでも使うものがあるので、それと齟齬がないか確認する。
  # 例えば N, M = 4, 2 の時、S の 3 文字目と T の 2 文字目が共有される。
  if N < M:
    N, M = M, N
    S, T = T, S

  if T[0] != S[0]:
    print(-1)
    return

  # 最大公約数で割った値 * i < N, M文字目で重複する
  gcd_N_M = gcd(N, M)
  S_step = N//gcd_N_M
  T_step = M//gcd_N_M
  for i in range(gcd_N_M):
    if S[i*S_step] != T[i*T_step]:
      print(-1)
      return
  print(N*M//gcd_N_M)

resolve()

if __name__ == "__main__":
    unittest.main()
