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
        input = """3 998244353"""
        output = """7 15"""
        self.assertIO(input, output)

    # def test_Sample_Input_2(self):
    #     input = """16 999999937"""
    #     output = """46 1016 14288 143044 1079816 6349672 29622112 110569766 330377828 784245480 453609503 38603306 44981526 314279703 408855776"""
    #     self.assertIO(input, output)

def resolve():
  def comb_mod(n,r,mod):
    if n-r<r:
      r=n-r
    N=n
    R=r
    u=1
    d=1
    for i in range(r):
      u*=N
      u%=mod
      N-=1
      d*=R
      d%=mod
      R-=1
    return u*pow(d,mod-2,mod)%mod

  inf = 10**18+1
  # N が 3000 で P が素数。
  # N 番目の列に含まれる頂点につながっているへんのうち、どれか一つを切ることはできる。
  # 頂点を i 個選んでから * 3 倍する？
  # 右端を選んだ場合とそうで無い場合を足す。
  # 右端を選んだ場合だけ 4 パターンになるのが厄介。

  N, P = map(int, input().split(" "))

  for i in range(1, N):
    # 末尾を選ばないパターン
    select = comb_mod(N-2, i, P) if N-2 >= i else 0
    ans = select*pow(3, i, P)

    print(ans)
    # 末尾固定で他を選ぶパターン
    select = comb_mod(N-2, i-1, P) if N-2 >= i-1 else 0
    ans += 4*select*pow(3, i-1, P)

    print(ans)



import sys
sys.setrecursionlimit(500*500)

from math import gcd
from functools import reduce
from itertools import product
from itertools import combinations
from itertools import accumulate # 累積和作るやつ
from collections import deque
from collections import defaultdict
from heapq import heappop, heappush
from bisect import bisect_left

alpha2num = lambda c: ord(c) - ord('a')
num2alpha = lambda c: chr(c+97)
popcnt = lambda x: bin(x).count("1")

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()