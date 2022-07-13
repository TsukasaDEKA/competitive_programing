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
        input = """5
3
AXA
6
ABCZAZ
30
QWERTYUIOPASDFGHJKLZXCVBNMQWER
28
JVIISNEOXHSNEAAENSHXOENSIIVJ
31
KVOHEEMSOZZASHENDIGOJRTJVMVSDWW"""
        output = """24
29
212370247
36523399
231364016"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """1
6
ABCZAZ"""
        output = """29"""
        self.assertIO(input, output)

def resolve():
  alpha2num = lambda c: ord(c) - ord('A')
  mod = 998244353

  T = int(input())
  for _ in range(T):
    N = int(input())
    S = [x for x in list(input())]

    # S の前半分を反転した回文を X_ とする。
    # X_ よりも辞書順で小さい回文は S よりも小さい。
    # X_ が S よりも小さいとは限らない点に注意する。
    X_ = [S[min(i, N-1-i)] for i in range(N)]

    ans = 0
    # X_ 未満の回文の個数を数える。
    # L: 回文の前半分の長さ ( N が奇数の場合は真ん中の文字を含む。)
    L = (N+1)//2
    for i in range(L):
      # alpha2num(X_[i]): X_[i] よりも小さな文字の個数。
      # X[i] を X_[i] 未満にすると、それ以降の文字は回文という条件を満たす限り自由に選べる
      # => 26**<残りの自由に選べる文字数> を答えに足す。
      ans += alpha2num(X_[i]) * pow(26, L-i-1, mod)
      if ans >= mod: ans%=mod

    # X_ が条件を満たす場合、X_ 分も答えに追加する。
    if "".join(X_) <= "".join(S):
      ans += 1

    print(ans%mod)

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()