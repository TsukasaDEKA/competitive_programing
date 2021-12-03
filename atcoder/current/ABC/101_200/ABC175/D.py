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
        input = """5 2
2 4 5 1 3
3 4 -10 -8 8"""
        output = """8"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """2 3
2 1
10 -7"""
        output = """13"""
        self.assertIO(input, output)

    def test_Sample_Input_3(self):
        input = """3 3
3 1 2
-1000 -2000 -3000"""
        output = """-1000"""
        self.assertIO(input, output)

    def test_Sample_Input_4(self):
        input = """10 58
9 1 6 7 8 4 3 2 10 5
695279662 988782657 -119067776 382975538 -151885171 -177220596 -169777795 37619092 389386780 980092719"""
        output = """29507023469"""
        self.assertIO(input, output)

def resolve():
  from collections import deque
  from itertools import accumulate
  # 移動について ~~一本道 なので単純に並べ替えるだけで良い。~~ => 閉路があり得る。というか順列なので必ず閉路。
  # 複数の閉路が存在する可能性があって、閉路間の移動はできない。
  # 閉路のポイント合計が負の時 => 区間和が最大になる長さ K 未満の区間だけを通るのが最適。
  # 閉路のポイント合計が正の時 => できるだけ周回した後、区間和が最大になる区間を通るのが最適。
  # => 閉路の長さが K 以上の時は長さが K 以下の区間和の最大を求める。
  # => 閉路の長さが K 未満の時は以下の 2 パターンのどちらか大きい方を使う。
  # <ポイント合計>*(K//閉路の長さ) + K%<閉路の長さ>以下の区間和の最大値
  # <ポイント合計>*((K//閉路の長さ)-1) + 閉路の全区間における区間和の最大値
  # 上記のパターンをまとめると以下の 3 つを比較すれば良い。
  # 閉路の長さを l とすると、
  # min(K, l) 以下の長さの区間和最大値
  # <ポイント合計>*(K//l) + K%l 以下の区間和の最大値
  # <ポイント合計>*max(0, ((K//l)-1)) + min(K+l*(K//l), l) 以下の区間和の最大値

  # 要素数が 5000 なので
  inf = 10**18+1
  N, K = map(int, input().split(" "))
  P = [int(x)-1 for x in input().split(" ")]
  C = [int(x) for x in input().split(" ")]

  # 閉路を構築する。
  nexts = deque()
  checked = [False]*N
  loops = []
  for i in range(N):
    if checked[i]: continue
    checked[i] = True
    temp = []
    nexts.append(i)
    while nexts:
      current = nexts.popleft()
      temp.append(current)
      if checked[P[current]]: continue
      checked[P[current]] = True
      nexts.append(P[current])
    loops.append(temp)

  # print(loops)
  ans = -inf
  for loop in loops:
    # 累積和
    sums = [0]+list(accumulate([C[i] for i in loop]+[C[i] for i in loop]))
    n = len(loop)
    # interval_sums[l]: 長さ l の区間和の最大値
    interval_sums = [-inf]*(n+1)
    for r in range(1, len(sums)):
      for length in range(1, min(n, r)+1):
        l = r-length
        temp = sums[r]-sums[l]
        if temp > interval_sums[length]:
          interval_sums[length] = temp

    for i in range(1, n+1):
      interval_sums[i] = max(interval_sums[i], interval_sums[i-1])

    # 今見てる閉路の最大値をとる。
    # total: 一周した時のポイント累計
    total = sums[n]
    temp_ans = max(interval_sums[min(K, l)], total*(K//l)+interval_sums[K%l], total*max(0, (K//l)-1) + interval_sums[min(K+l*(K//l), l)])
    if temp_ans > ans: ans = temp_ans

  print(ans)

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()