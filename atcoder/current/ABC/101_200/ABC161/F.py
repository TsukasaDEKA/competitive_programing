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
        input = """6"""
        output = """3"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """3141"""
        output = """13"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """314159265358"""
        output = """9"""
        self.assertIO(input, output)

    def test_Sample_Input_4(self):
        input = """2"""
        output = """1"""
        self.assertIO(input, output)

def resolve():
  # K = 1 は無限ループする。
  # 入力例を見ると条件を満たす K は意外と少なかったりする。
  # K = N, N-1 の時、N-1 != 1 であれば条件を満たす。
  # K = 2 は必ず条件を満たす。
  # N が 1 になる一手まえの K, K+1 は必ず通過する。
  # K**X == N の場合、条件を満たす。N = 27 の場合、 3 は条件を満たす。
  # 素因数分解して、素数が 1 種類だった場合、その素数は K になりうる。
  # X*K+1 == N の場合、条件を満たす。
  # 19 = 3*3*2+1 で考えてみる。
  # K = 3 の時、16, 13, 10, 7, 4, 1 で条件を満たす。
  # K = 4 の時、15, 11, 7, 3 で条件を満たさない。
  # N-=K をしたとして、N%K に変化はないため、ずっと N-=K を繰り返す事になる。
  # これは、N%=K と同義である。
  # この問題は、N
  from collections import defaultdict
  N = int(input())
  ans = set()
  if N-1 >= 2: ans.add(N-1)
  ans.add(N)
  for i in range(2, int(-(-N**0.5//1))+1):
    n = N
    while n > 1:
      if n%i == 0:
        n//=i
      if n%i == 1:
        ans.add(i)
        break
      if n%i > 1:
        break
    if (N-1)%i: continue
    ans.add(i)
    ans.add((N-1)//i)
  print(len(ans))

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()