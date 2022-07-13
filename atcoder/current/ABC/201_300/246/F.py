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
        input = """2 2
ab
ac"""
        output = """7"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """4 3
abcdefg
hijklmnop
qrstuv
wxyz"""
        output = """1352"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """5 1000000000
abc
acde
cefg
abcfh
dghi"""
        output = """346462871"""
        self.assertIO(input, output)

def resolve():
  from numpy import logical_and
  popcnt = lambda x: bin(x).count("1")
  alpha2num = lambda c: ord(c) - ord('a')

  inf = 10**18+1
  mod = 998244353
  N, L = map(int, input().split(" "))
  S = []
  for _ in range(N):
    bitS = 0
    for s in list(input()):
      bitS += 1<<alpha2num(s)
    S.append(bitS)
  
  # 入力可能な文字列の組み合わせを求める。
  ans = 0
  for bit in range(1, 1<<N):
    # temp: 使える文字
    temp = logical_and([S[i] for i in range(N) if (1<<i)&bit])

    # 使えるキーの段数が奇数の場合、答えに足す。
    if popcnt(bit)%2:
      ans += pow(popcnt(temp), L, mod)
    else:
      ans -= pow(popcnt(temp), L, mod)

    ans%=mod
  print(ans)

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()