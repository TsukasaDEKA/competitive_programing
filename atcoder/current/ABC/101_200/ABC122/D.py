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
        input = """3"""
        output = """61"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """4"""
        output = """230"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """100"""
        output = """388130742"""
        self.assertIO(input, output)

def resolve():
  from collections import defaultdict

  # 解説 AC
  # dp[S]: 末尾 3 文字が S の時の場合数
  # dp[S] => dp[S'] の遷移は S + <A or C or G or T> の 4 文字が良いパターンである時のみ行う。
  # 良くないパターン: *AGC, *GAC, *ACG, A*GC, AG*C
  # N 回ループして総和が答え。

  inf = 10**18+1
  mod = 10**9+7

  N = int(input())
  # illegal: ダメなパターン
  illegal = set()
  for p in ["AGC", "GAC", "ACG"]:
    for c in  ["A", "C", "G", "T", "*"]:
      illegal.add(c+p)

  for c in  ["A", "C", "G", "T"]:
    illegal.add("AG"+c+"C")
    illegal.add("A"+c+"GC")

  dp = defaultdict(int)
  dp["***"] = 1
  for _ in range(N):
    temp = defaultdict(int)
    keys = dp.keys()
    for key in keys:
      for c in ["A", "C", "G", "T"]:
        if key+c in illegal: continue
        temp[key[1:]+c] += dp[key]
        if temp[key[1:]+c] >= mod: temp[key[1:]+c]%=mod
    dp = temp
  
  print(sum(dp.values())%mod)

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()