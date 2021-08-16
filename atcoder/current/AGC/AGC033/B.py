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
        input = """2 3 3
2 2
RRL
LUD"""
        output = """YES"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """4 3 5
2 2
UDRRR
LLDUD"""
        output = """NO"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """5 6 11
2 1
RLDRRUDDLRL
URRDRLLDLRD"""
        output = """NO"""
        self.assertIO(input, output)

def resolve():
  inf = 10**18+1
  # 縦と横で分離して考えられる。
  # 高橋君が L 方向に落とせる条件は、
  # Sw - [S[:i]に含まれる L] + [T[:i]に含まれる R] < 0 である i が存在することである。
  # 同じように R 方向に落とせる条件は
  # (W - Sw) - [S[:i]に含まれる R] + [T[:i]に含まれる L] < 0である i が存在することである。
  # これを 縦の分もやれば良いのでは？
  from collections import defaultdict
  LUDR = "LUDR"
  H, W, N = map(int, input().split(" "))
  Sh, Sw = [int(x) for x in input().split(" ")]
  S = list(input())
  T = list(input())

  Uh = Dh = Sh
  Rw = Lw = Sw
  for i in range(N):
    if S[i] == "L": Lw-=1
    if S[i] == "R": Rw+=1
    if S[i] == "U": Uh-=1
    if S[i] == "D": Dh+=1
    # print(Lw, Rw, Uh, Dh)
    if Lw <= 0 or Rw > W or Uh <= 0 or Dh > H:
      print("NO")
      return
    if T[i] == "L": Rw = max(Rw-1, 1)
    if T[i] == "R": Lw = min(Lw+1, W)
    if T[i] == "U": Dh = max(Dh-1, 1)
    if T[i] == "D": Uh = min(Uh+1, H)

  print("YES")

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

dh = [0, -1, 0, 1]
dw = [-1, 0, 1, 0]

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()