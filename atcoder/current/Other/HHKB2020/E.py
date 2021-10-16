from collections import defaultdict
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
        input = """1 5
..#.."""
        output = """48"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """2 3
..#
#.."""
        output = """52"""
        self.assertIO(input, output)

def resolve():
  from collections import defaultdict

  mod = 10**9+7
  # あるマスが照らされるパターンを考える。
  # あるマスの上下左右の障害物にあたるまでのマス
  # + そのマス自身のどれかにランプが置かれている場合にそのマスが照らされる。
  # また、その他のマスに関しては自由に状態を選ぶことができる。
  H, W = map(int, input().split(" "))
  S = [[x == "." for x in list(input())] for _ in range(H)]

  TOTAL = 0
  for s in S:
    TOTAL+=s.count(True)

  COUNT = [[-3]*W for _ in range(H)]
  # 右
  for h in range(H):
    val = 0
    for w in range(W):
      if S[h][w]:
        val+=1
        COUNT[h][w]+=val
      else: val = 0
  # 左
  for h in range(H):
    val = 0
    for w in reversed(range(W)):
      if S[h][w]:
        val+=1
        COUNT[h][w]+=val
      else: val = 0
  # 上
  for w in range(W):
    val = 0
    for h in range(H):
      if S[h][w]:
        val+=1
        COUNT[h][w]+=val
      else: val = 0
  # 下
  for w in range(W):
    val = 0
    for h in reversed(range(H)):
      if S[h][w]:
        val+=1
        COUNT[h][w]+=val
      else: val = 0

  cache = defaultdict(int)
  # ans = 0
  diff = 0
  for h in range(H):
    count_h = COUNT[h]
    for w in range(W):
      if S[h][w]:
        if count_h[w] not in cache:
          cache[count_h[w]] = pow(2, TOTAL-count_h[w], mod)
        diff += cache[count_h[w]]
        if diff >= mod: diff%=mod
        # if count_h[w] not in cache:
        #   cache[count_h[w]] = (pow(2, TOTAL-count_h[w], mod)*(pow(2, count_h[w], mod)-1))%mod
        # ans += cache[count_h[w]]
        # if ans >= mod: ans%=mod

  ans = (TOTAL*pow(2, TOTAL, mod))%mod - diff
  print(ans%mod)

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()