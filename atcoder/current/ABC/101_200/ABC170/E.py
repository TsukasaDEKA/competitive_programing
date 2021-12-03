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
        input = """6 3
8 1
6 2
9 3
1 1
2 2
1 3
4 3
2 1
1 2"""
        output = """6
2
6"""
        self.assertIO(input, output)

    def test_Sample_Input_2(self):
        input = """2 2
4208 1234
3056 5678
1 2020
2 2020"""
        output = """3056
4208"""
        self.assertIO(input, output)

#####ide_ele#####
# ide_ele = 0 # 区間和、最大公約数
# ide_ele = 1 # 区間積
ide_ele = float('inf') # 最小値
# ide_ele = - float('inf') # 最大値
#################

class SegTree:
  """
  init(init_val, ide_ele): 配列init_valで初期化 O(N)
  update(k, x): k番目の値をxに更新 O(logN)
  query(l, r): 区間[l, r)をsegfuncしたものを返す O(logN)
  """
  def __init__(self, init_val, segfunc, ide_ele):
    """
    init_val: 配列の初期値
    segfunc: 区間にしたい操作
    ide_ele: 単位元
    n: 要素数
    num: n以上の最小の2のべき乗
    tree: セグメント木(1-index)
    """
    n = len(init_val)
    self.segfunc = segfunc
    self.ide_ele = ide_ele
    self.num = 1 << (n - 1).bit_length()
    self.tree = [ide_ele] * 2 * self.num
    # 配列の値を葉にセット
    for i in range(n):
      self.tree[self.num + i] = init_val[i]
    # 構築していく
    for i in range(self.num - 1, 0, -1):
      self.tree[i] = self.segfunc(self.tree[2 * i], self.tree[2 * i + 1])

  def update(self, k, x):
    """
    k番目の値をxに更新
    k: index(0-index)
    x: update value
    """
    # 葉の部分が前半に入っている。+= self.numをすることで元になる配列要素に移動
    k += self.num
    self.tree[k] = x
    while k > 1:
      # k >> 1 == k // 2 (index k の親の index)
      # k ^ 1 : 末尾を xor する。偶数だったら +1、奇数だったら -1 する。k インデックス(子)の片割れ
      self.tree[k >> 1] = self.segfunc(self.tree[k], self.tree[k ^ 1])
      k >>= 1

  def query(self, l, r):
    """
    [l, r)のsegfuncしたものを得る
    l: index(0-index)
    r: index(0-index)
    """
    res = self.ide_ele

    l += self.num
    r += self.num
    while l < r:
      # l & 1 => l が 奇数 (ペアの右側) だったら 1:
      if l & 1:
        res = self.segfunc(res, self.tree[l])
        l += 1
      # r が奇数 = r-1 が偶数。なので、子のペアの左を見ることになる。
      if r & 1:
        res = self.segfunc(res, self.tree[r - 1])
      # l // 2
      l >>= 1
      r >>= 1
    return res

def resolve():
  from heapq import heappop, heappush
  # セグツリーっぽい。
  # 幼稚園のそれぞれの最もレートの高い幼児のレートをセグツリーで管理すればいける。
  # 問題は転園の処理。
  # heapq で管理してみる。
  N, Q = map(int, input().split(" "))
  P = 2*10**5
  SCORE = [0]*N
  BELONG_TO = [0]*N
  RANKING = [[] for _ in range(P)]
  for i in range(N):
    A, B = [int(x)-1 for x in input().split(" ")]
    A+=1
    BELONG_TO[i] = B
    SCORE[i] = A
    heappush(RANKING[B], (-A, i))

  seg = SegTree([ide_ele]*P, min, ide_ele)
  # 初回の答えを求める
  for i in range(P):
    if len(RANKING[i]) == 0: continue
    score, _ = RANKING[i][0]
    seg.update(i, -score)

  for _ in range(Q):
    C, to_ = [int(x)-1 for x in input().split(" ")]

    # 退園処理
    from_, BELONG_TO[C] = BELONG_TO[C], to_

    # ランキングを更新
    heappush(RANKING[to_], (-SCORE[C], C))
    for p in [to_, from_]:
      while RANKING[p]:
        score, top = RANKING[p][0]
        if BELONG_TO[top] == p: break
        # ランキングトップがその園に所属していない場合、ランキングから除外する。
        _ = heappop(RANKING[p])
      # 園児がいない場合は inf, いる場合はランキングトップのスコアを seg tree に登録する。
      score = ide_ele if len(RANKING[p]) == 0 else -(RANKING[p][0][0])
      seg.update(p, score)

    # 答え
    print(seg.query(0, P))

import sys
if sys.argv[-1] == './Main.py':
  resolve()

if __name__ == "__main__":
  unittest.main()