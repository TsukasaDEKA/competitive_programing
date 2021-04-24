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
        input = """4 2
1 1 3 4"""
        output = """11"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """6 3
10 10 10 -10 -10 -10"""
        output = """360"""
        self.assertIO(input, output)

#     def test_Sample_Input_3(self):
#         input = """3 1
# 1 1 1"""
#         output = """0"""
#         self.assertIO(input, output)

    def test_Sample_Input_4(self):
        input = """10 6
1000000000 1000000000 1000000000 1000000000 1000000000 0 0 0 0 0"""
        output = """999998537"""
        self.assertIO(input, output)

def resolve():
  def extgcd(a, b):
    if b:
      g, y, x = extgcd(b, a % b)
      y -= (a // b)*x
      return g, x, y
    return a, 1, 0

  # ソートした場合、
  # minX が i 番目の数字になる組み合わせは (N-i)C(K-1) 個
  # maxX が i 番目の数字になる組み合わせは (i-1)C(K-1) 個
  # O(N) で解ける

  mod = 10**9+7
  N, K = map(int, input().split(" "))
  A = sorted([int(x) for x in input().split(" ")])

  if K  == 1:
    print(0)
    return

  p = mod - 2
  comb = [0]*N
  comb[K-1] = 1
  for i in range(K, N):
    _, _, b = extgcd(mod, i-K+1)
    b %= mod
    comb[i] = (i*comb[i-1])*b
    if comb[i]>=mod: comb[i] %= mod

  ans = 0
  for i in range(N):
    ans += A[i]*(comb[i]-comb[N-i-1])%mod
    if ans >= mod: ans%=mod

  print(ans)

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
    unittest.main()
